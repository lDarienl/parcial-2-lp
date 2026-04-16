from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

from tokenizer import Token, tokenize


class CykSyntaxError(SyntaxError):
    pass


@dataclass(frozen=True)
class Node:
    symbol: str
    i: int
    j: int
    split: Optional[int] = None
    left_symbol: Optional[str] = None
    right_symbol: Optional[str] = None
    terminal: Optional[str] = None


class CykCalculator:
    """
    CYK para una gramática de calculadora en CNF (sumas, productos y paréntesis).
    Tokens terminales: NUM, PLUS, MUL, LP, RP.
    """

    # Producciones binarias A -> B C
    _binary_rules: Dict[Tuple[str, str], Set[str]] = {
        ("E", "A1"): {"S", "E"},
        ("T", "A2"): {"S", "E", "T"},
        ("LP", "A3"): {"S", "E", "T", "G"},
        ("PLUS", "T"): {"A1"},
        ("MUL", "G"): {"A2"},
        ("E", "RP"): {"A3"},
    }

    # Producciones terminales A -> a
    _terminal_rules: Dict[str, Set[str]] = {
        "NUM": {"S", "E", "T", "G"},
        "PLUS": {"PLUS"},
        "MUL": {"MUL"},
        "LP": {"LP"},
        "RP": {"RP"},
    }

    def parse_and_eval(self, expr: str) -> float:
        tokens = tokenize(expr)
        if not tokens:
            raise CykSyntaxError("La expresión está vacía")
        table, back = self._cyk(tokens)
        n = len(tokens)
        if "S" not in table[0][n - 1]:
            raise CykSyntaxError("La expresión no pertenece a la gramática de la calculadora")
        root = self._build_node("S", 0, n - 1, back)
        return self._eval_node(root, tokens, back)

    def _cyk(self, tokens: List[Token]):
        n = len(tokens)
        table: List[List[Set[str]]] = [[set() for _ in range(n)] for _ in range(n)]
        back: Dict[Tuple[str, int, int], Node] = {}

        # Base: largo 1
        for i, tk in enumerate(tokens):
            for lhs in self._terminal_rules.get(tk.kind, set()):
                table[i][i].add(lhs)
                back[(lhs, i, i)] = Node(symbol=lhs, i=i, j=i, terminal=tk.kind)

        # Subcadenas de largo >= 2
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    left_set = table[i][k]
                    right_set = table[k + 1][j]
                    if not left_set or not right_set:
                        continue
                    for b in left_set:
                        for c in right_set:
                            for a in self._binary_rules.get((b, c), set()):
                                if a not in table[i][j]:
                                    table[i][j].add(a)
                                    back[(a, i, j)] = Node(
                                        symbol=a,
                                        i=i,
                                        j=j,
                                        split=k,
                                        left_symbol=b,
                                        right_symbol=c,
                                    )
        return table, back

    def _build_node(self, symbol: str, i: int, j: int, back: Dict[Tuple[str, int, int], Node]) -> Node:
        key = (symbol, i, j)
        if key not in back:
            raise CykSyntaxError(f"No hay derivación para {symbol}[{i},{j}]")
        return back[key]

    def _eval_node(self, node: Node, tokens: List[Token], back: Dict[Tuple[str, int, int], Node]) -> float:
        if node.terminal is not None:
            tk = tokens[node.i]
            if node.symbol in {"S", "E", "T", "G"} and tk.kind == "NUM":
                return tk.value or 0.0
            # Los terminales PLUS/MUL/LP/RP no se evalúan numéricamente.
            return 0.0

        assert node.split is not None
        assert node.left_symbol is not None
        assert node.right_symbol is not None

        left = self._build_node(node.left_symbol, node.i, node.split, back)
        right = self._build_node(node.right_symbol, node.split + 1, node.j, back)

        # Semántica para no terminales auxiliares.
        if node.symbol == "A1":  # PLUS T -> retorna valor de T (sumando se aplica en E)
            return self._eval_node(right, tokens, back)
        if node.symbol == "A2":  # MUL G -> retorna valor de G (producto se aplica en T)
            return self._eval_node(right, tokens, back)
        if node.symbol == "A3":  # E RP -> retorna valor de E (ignora RP)
            return self._eval_node(left, tokens, back)

        if node.symbol in {"S", "E"}:
            if node.left_symbol == "E" and node.right_symbol == "A1":
                return self._eval_node(left, tokens, back) + self._eval_node(right, tokens, back)
            if node.left_symbol == "T" and node.right_symbol == "A2":
                return self._eval_node(left, tokens, back) * self._eval_node(right, tokens, back)
            if node.left_symbol == "LP" and node.right_symbol == "A3":
                return self._eval_node(right, tokens, back)
            raise CykSyntaxError("Árbol inválido para símbolo E/S")

        if node.symbol in {"T", "G"}:
            if node.left_symbol == "T" and node.right_symbol == "A2":
                return self._eval_node(left, tokens, back) * self._eval_node(right, tokens, back)
            if node.left_symbol == "LP" and node.right_symbol == "A3":
                return self._eval_node(right, tokens, back)
            raise CykSyntaxError("Árbol inválido para símbolo T/G")

        raise CykSyntaxError(f"Símbolo no esperado en evaluación: {node.symbol}")
