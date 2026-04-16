from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    kind: str
    lexeme: str
    value: float | None = None


class TokenizeError(ValueError):
    pass


def tokenize(expr: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0
    n = len(expr)
    while i < n:
        ch = expr[i]
        if ch.isspace():
            i += 1
            continue
        if ch.isdigit():
            j = i
            while j < n and expr[j].isdigit():
                j += 1
            if j < n and expr[j] == ".":
                j += 1
                if j >= n or not expr[j].isdigit():
                    raise TokenizeError(f"Número decimal inválido en posición {i + 1}")
                while j < n and expr[j].isdigit():
                    j += 1
            lex = expr[i:j]
            tokens.append(Token(kind="NUM", lexeme=lex, value=float(lex)))
            i = j
            continue
        if ch == "+":
            tokens.append(Token(kind="PLUS", lexeme=ch))
            i += 1
            continue
        if ch == "*":
            tokens.append(Token(kind="MUL", lexeme=ch))
            i += 1
            continue
        if ch == "(":
            tokens.append(Token(kind="LP", lexeme=ch))
            i += 1
            continue
        if ch == ")":
            tokens.append(Token(kind="RP", lexeme=ch))
            i += 1
            continue
        raise TokenizeError(f"Carácter inválido '{ch}' en posición {i + 1}")
    return tokens
