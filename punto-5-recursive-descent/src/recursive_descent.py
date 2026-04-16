from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional

from tokenizer import Token, tokenize


class ParseError(SyntaxError):
    pass


@dataclass
class RecursiveDescentParser:
    """
    Parser descendente recursivo LL(1) con función de emparejamiento `match`.

    Gramática (informal):

        program     -> stmt_list EOF
        stmt_list   -> stmt stmt_list | ε
        stmt        -> assign | if_stmt
        assign      -> ID '=' expr ';'
        if_stmt     -> 'if' '(' expr ')' block else_opt
        else_opt    -> 'else' block | ε
        block       -> '{' stmt_list '}'
        expr        -> term (('+' | '-') term)*
        term        -> factor (('*' | '/') factor)*
        factor      -> NUM | ID | '(' expr ')'

    ε en stmt_list: al encontrar EOF o '}' (fin de bloque actual).
    """

    source: str
    tokens: List[Token] = field(init=False)
    pos: int = field(init=False, default=0)

    def __post_init__(self) -> None:
        self.tokens = tokenize(self.source)
        self.pos = 0

    def _peek(self) -> Token:
        return self.tokens[self.pos]

    def advance(self) -> None:
        if self._peek().kind != "EOF":
            self.pos += 1

    def match(self, expected: str) -> Token:
        """Empareja un terminal: consume si coincide; si no, error."""
        tok = self._peek()
        if tok.kind == expected:
            self.advance()
            return tok
        raise ParseError(
            f"línea {tok.line}, columna {tok.column}: se esperaba {expected}, "
            f"llegó {tok.kind} ({tok.lexeme!r})"
        )

    def parse_program(self) -> None:
        self._stmt_list(self._at_eof)
        self.match("EOF")

    def _at_eof(self) -> bool:
        return self._peek().kind == "EOF"

    def _at_block_end(self) -> bool:
        return self._peek().kind == "RBRACE"

    def _stmt_list(self, end: Callable[[], bool]) -> None:
        while not end():
            self._stmt()

    def _stmt(self) -> None:
        tok = self._peek()
        if tok.kind == "ID":
            self._assign()
        elif tok.kind == "IF":
            self._if_stmt()
        else:
            raise ParseError(
                f"línea {tok.line}, columna {tok.column}: se esperaba ID o IF, "
                f"llegó {tok.kind} ({tok.lexeme!r})"
            )

    def _assign(self) -> None:
        self.match("ID")
        self.match("ASSIGN")
        self._expr()
        self.match("SEMICOLON")

    def _if_stmt(self) -> None:
        self.match("IF")
        self.match("LP")
        self._expr()
        self.match("RP")
        self._block()
        if self._peek().kind == "ELSE":
            self.match("ELSE")
            self._block()

    def _block(self) -> None:
        self.match("LBRACE")
        self._stmt_list(self._at_block_end)
        self.match("RBRACE")

    # expr -> term (('+'|'-') term)*
    def _expr(self) -> None:
        self._term()
        while self._peek().kind in ("PLUS", "MINUS"):
            self.advance()
            self._term()

    # term -> factor (('*'|'/') factor)*
    def _term(self) -> None:
        self._factor()
        while self._peek().kind in ("MUL", "DIV"):
            self.advance()
            self._factor()

    # factor -> NUM | ID | '(' expr ')'
    def _factor(self) -> None:
        tok = self._peek()
        if tok.kind == "NUM":
            self.match("NUM")
        elif tok.kind == "ID":
            self.match("ID")
        elif tok.kind == "LP":
            self.match("LP")
            self._expr()
            self.match("RP")
        else:
            raise ParseError(
                f"línea {tok.line}, columna {tok.column}: factor inválido, "
                f"llegó {tok.kind} ({tok.lexeme!r})"
            )


def parse(source: str) -> None:
    RecursiveDescentParser(source).parse_program()
