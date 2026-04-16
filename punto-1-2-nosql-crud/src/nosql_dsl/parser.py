from __future__ import annotations

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from nosql_dsl.generated.grammar1Lexer import grammar1Lexer
from nosql_dsl.generated.grammar1Parser import grammar1Parser


class ParseError(SyntaxError):
    def __init__(self, line: int, column: int, message: str) -> None:
        self.line = line
        self.column = column
        super().__init__(f"línea {line}, columna {column}: {message}")


class _ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        raise ParseError(line, column + 1, msg)


def parse_program(source: str) -> grammar1Parser.ProgramaContext:
    """Analiza un programa completo y devuelve el árbol `programa`."""
    lexer = grammar1Lexer(InputStream(source))
    lexer.removeErrorListeners()
    lexer.addErrorListener(_ThrowingErrorListener())
    stream = CommonTokenStream(lexer)
    parser = grammar1Parser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(_ThrowingErrorListener())
    tree = parser.programa()
    return tree
