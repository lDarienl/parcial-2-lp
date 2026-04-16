import pytest

from recursive_descent import ParseError, parse


def test_assign_only():
    parse("x = 1;")


def test_if_without_else():
    parse("if (1) { y = 2; }")


def test_if_with_else():
    parse("if (0) { a = 1; } else { b = 2; }")


def test_nested_if():
    parse("if (1) { if (0) { x = 1; } else { x = 2; } z = 3; }")


def test_expr_with_ops():
    parse("x = (1 + 2) * 3 - 4 / 2;")


def test_missing_semicolon():
    with pytest.raises(ParseError):
        parse("x = 1")


def test_bad_start_stmt():
    with pytest.raises(ParseError):
        parse("1 = 2;")
