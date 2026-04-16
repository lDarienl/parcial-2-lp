from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List, Optional

from nosql_dsl.generated.grammar1Parser import grammar1Parser
from nosql_dsl.generated.grammar1Visitor import grammar1Visitor
from nosql_dsl.parser import parse_program


def _unquote_string(raw: str) -> str:
    if len(raw) < 2 or raw[0] != '"' or raw[-1] != '"':
        return raw
    inner = raw[1:-1]
    out: list[str] = []
    i = 0
    while i < len(inner):
        ch = inner[i]
        if ch != "\\" or i + 1 >= len(inner):
            out.append(ch)
            i += 1
            continue
        nxt = inner[i + 1]
        esc = {"n": "\n", "r": "\r", "t": "\t", '"': '"', "\\": "\\", "/": "/"}.get(nxt)
        if esc is not None:
            out.append(esc)
            i += 2
            continue
        if nxt == "u" and i + 5 < len(inner):
            hex_part = inner[i + 2 : i + 6]
            try:
                out.append(chr(int(hex_part, 16)))
                i += 6
                continue
            except ValueError:
                pass
        out.append(nxt)
        i += 2
    return "".join(out)


class InMemoryCrudInterpreter(grammar1Visitor):
    """Motor en memoria: colecciones como listas de documentos (dict)."""

    def __init__(self) -> None:
        self.collections: Dict[str, List[dict]] = defaultdict(list)
        self.last_read: List[dict] = []

    def run(self, source: str) -> None:
        tree = parse_program(source)
        self.last_read = []
        self.visit(tree)

    def visitPrograma(self, ctx: grammar1Parser.ProgramaContext):
        for ins in ctx.instruccion():
            self.visitInstruccion(ins)

    def visitInstruccion(self, ctx: grammar1Parser.InstruccionContext):
        if ctx.createStmt() is not None:
            return self.visitCreateStmt(ctx.createStmt())
        if ctx.readStmt() is not None:
            return self.visitReadStmt(ctx.readStmt())
        if ctx.updateStmt() is not None:
            return self.visitUpdateStmt(ctx.updateStmt())
        if ctx.deleteStmt() is not None:
            return self.visitDeleteStmt(ctx.deleteStmt())
        return None

    def visitCreateStmt(self, ctx: grammar1Parser.CreateStmtContext):
        coll = ctx.ID().getText()
        doc = self._objeto_to_dict(ctx.objeto())
        self.collections[coll].append(doc)

    def visitReadStmt(self, ctx: grammar1Parser.ReadStmtContext):
        coll = ctx.ID().getText()
        docs = list(self.collections.get(coll, []))
        if ctx.WHERE() is not None:
            cond = ctx.condiciones().expr()
            docs = [d for d in docs if self._eval_expr(cond, d)]
        self.last_read = docs

    def visitUpdateStmt(self, ctx: grammar1Parser.UpdateStmtContext):
        coll = ctx.ID(0).getText()
        field = ctx.ID(1).getText()
        new_val = self._valor_to_python(ctx.valor(), field_ref_doc=None)
        cond = ctx.condiciones().expr()
        for doc in self.collections[coll]:
            if self._eval_expr(cond, doc):
                doc[field] = new_val

    def visitDeleteStmt(self, ctx: grammar1Parser.DeleteStmtContext):
        coll = ctx.ID().getText()
        cond = ctx.condiciones().expr()
        self.collections[coll] = [d for d in self.collections[coll] if not self._eval_expr(cond, d)]

    def _objeto_to_dict(self, ctx: grammar1Parser.ObjetoContext) -> dict:
        out: dict = {}
        for par in ctx.par():
            key = self._clave_text(par.clave())
            out[key] = self._valor_to_python(par.valor(), field_ref_doc=None)
        return out

    def _clave_text(self, ctx: grammar1Parser.ClaveContext) -> str:
        if ctx.STRING() is not None:
            return _unquote_string(ctx.STRING().getText())
        return ctx.ID().getText()

    def _valor_to_python(self, ctx: grammar1Parser.ValorContext, field_ref_doc: Optional[dict]) -> Any:
        if ctx.STRING() is not None:
            return _unquote_string(ctx.STRING().getText())
        if ctx.NUMBER() is not None:
            text = ctx.NUMBER().getText()
            return float(text) if "." in text else int(text)
        if ctx.TRUE() is not None:
            return True
        if ctx.FALSE() is not None:
            return False
        if ctx.NULL_() is not None:
            return None
        if ctx.objeto() is not None:
            return self._objeto_to_dict(ctx.objeto())
        if ctx.array() is not None:
            return [self._valor_to_python(v, field_ref_doc) for v in ctx.array().valor()]
        if ctx.ID() is not None:
            name = ctx.ID().getText()
            if field_ref_doc is not None:
                return field_ref_doc.get(name)
            return name
        raise RuntimeError("valor sin alternativa reconocida")

    def _eval_expr(self, ctx: grammar1Parser.ExprContext, doc: dict) -> bool:
        if ctx.OR() is not None:
            return self._eval_expr(ctx.expr(), doc) or self._eval_and(ctx.andExpr(), doc)
        return self._eval_and(ctx.andExpr(), doc)

    def _eval_and(self, ctx: grammar1Parser.AndExprContext, doc: dict) -> bool:
        if ctx.AND() is not None:
            return self._eval_and(ctx.andExpr(), doc) and self._eval_not(ctx.notExpr(), doc)
        return self._eval_not(ctx.notExpr(), doc)

    def _eval_not(self, ctx: grammar1Parser.NotExprContext, doc: dict) -> bool:
        if ctx.NOT() is not None:
            return not self._eval_not(ctx.notExpr(), doc)
        return self._eval_primary(ctx.primaryExpr(), doc)

    def _eval_primary(self, ctx: grammar1Parser.PrimaryExprContext, doc: dict) -> bool:
        if ctx.expr() is not None:
            return self._eval_expr(ctx.expr(), doc)
        return self._eval_comparacion(ctx.comparacion(), doc)

    def _eval_comparacion(self, ctx: grammar1Parser.ComparacionContext, doc: dict) -> bool:
        left = self._valor_to_python(ctx.valor(0), doc)
        right = self._valor_to_python(ctx.valor(1), doc)
        op = ctx.opComp()
        if op.EQ() is not None:
            return left == right
        if op.NE() is not None:
            return left != right
        if op.GT() is not None:
            return left > right
        if op.LT() is not None:
            return left < right
        if op.GE() is not None:
            return left >= right
        if op.LE() is not None:
            return left <= right
        raise RuntimeError("operador de comparación no reconocido")
