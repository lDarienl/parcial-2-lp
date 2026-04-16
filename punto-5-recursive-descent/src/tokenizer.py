from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Token:
    kind: str
    lexeme: str
    line: int
    column: int


class TokenizeError(ValueError):
    pass


def tokenize(source: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0
    line = 1
    col = 1
    n = len(source)

    def advance(ch: str) -> None:
        nonlocal i, line, col
        i += 1
        if ch == "\n":
            line += 1
            col = 1
        else:
            col += 1

    while i < n:
        ch = source[i]
        if ch.isspace():
            advance(ch)
            continue

        def emit(kind: str, lex: str) -> None:
            tokens.append(Token(kind, lex, line, col))

        if ch.isalpha() or ch == "_":
            start = i
            start_col = col
            while i < n and (source[i].isalnum() or source[i] == "_"):
                advance(source[i])
            lex = source[start:i]
            kw = {
                "if": "IF",
                "else": "ELSE",
            }.get(lex, "ID")
            tokens.append(Token(kw, lex, line, start_col))
            continue

        if ch.isdigit():
            start = i
            start_col = col
            while i < n and source[i].isdigit():
                advance(source[i])
            if i < n and source[i] == ".":
                advance(source[i])
                if i >= n or not source[i].isdigit():
                    raise TokenizeError(f"Decimal inválido en línea {line}, columna {col}")
                while i < n and source[i].isdigit():
                    advance(source[i])
            lex = source[start:i]
            tokens.append(Token("NUM", lex, line, start_col))
            continue

        single = {
            "=": "ASSIGN",
            ";": "SEMICOLON",
            "(": "LP",
            ")": "RP",
            "{": "LBRACE",
            "}": "RBRACE",
            "+": "PLUS",
            "-": "MINUS",
            "*": "MUL",
            "/": "DIV",
        }
        if ch in single:
            emit(single[ch], ch)
            advance(ch)
            continue

        raise TokenizeError(f"Carácter inválido '{ch}' en línea {line}, columna {col}")

    tokens.append(Token("EOF", "", line, col))
    return tokens
