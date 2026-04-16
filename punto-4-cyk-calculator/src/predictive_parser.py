from __future__ import annotations

from tokenizer import Token, tokenize


class PredictiveSyntaxError(SyntaxError):
    pass


class PredictiveCalculator:
    def __init__(self) -> None:
        self.tokens: list[Token] = []
        self.pos = 0

    def parse_and_eval(self, expr: str) -> float:
        self.tokens = tokenize(expr)
        self.pos = 0
        if not self.tokens:
            raise PredictiveSyntaxError("La expresión está vacía")
        value = self._expr()
        if self.pos != len(self.tokens):
            tk = self.tokens[self.pos]
            raise PredictiveSyntaxError(f"Token inesperado '{tk.lexeme}'")
        return value

    def _peek(self) -> Token | None:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _eat(self, expected: str) -> Token:
        tk = self._peek()
        if tk is None or tk.kind != expected:
            got = "EOF" if tk is None else tk.lexeme
            raise PredictiveSyntaxError(f"Se esperaba {expected}, llegó {got}")
        self.pos += 1
        return tk

    # expr -> term (PLUS term)*
    def _expr(self) -> float:
        value = self._term()
        while True:
            tk = self._peek()
            if tk is None or tk.kind != "PLUS":
                break
            self._eat("PLUS")
            value += self._term()
        return value

    # term -> factor (MUL factor)*
    def _term(self) -> float:
        value = self._factor()
        while True:
            tk = self._peek()
            if tk is None or tk.kind != "MUL":
                break
            self._eat("MUL")
            value *= self._factor()
        return value

    # factor -> NUM | LP expr RP
    def _factor(self) -> float:
        tk = self._peek()
        if tk is None:
            raise PredictiveSyntaxError("Final inesperado de entrada")
        if tk.kind == "NUM":
            return self._eat("NUM").value or 0.0
        if tk.kind == "LP":
            self._eat("LP")
            value = self._expr()
            self._eat("RP")
            return value
        raise PredictiveSyntaxError(f"Factor inválido: '{tk.lexeme}'")
