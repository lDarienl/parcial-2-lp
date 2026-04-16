from antlr4 import CommonTokenStream, InputStream
from antlr4.Token import Token

from nosql_dsl.generated.grammar1Lexer import grammar1Lexer


def test_invalid_id_token():
    lexer = grammar1Lexer(InputStream("123bad"))
    t = lexer.nextToken()
    assert t.type == grammar1Lexer.INVALID_ID


def test_numero_luego_id_separados():
    lexer = grammar1Lexer(InputStream("190 moto"))
    stream = CommonTokenStream(lexer)
    stream.fill()
    visibles = [
        t
        for t in stream.tokens
        if t is not None and t.channel == Token.DEFAULT_CHANNEL and t.type != Token.EOF
    ]
    assert visibles[0].type == grammar1Lexer.NUMBER
    assert visibles[1].type == grammar1Lexer.ID
