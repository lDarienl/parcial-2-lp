import math

import pytest

from cyk_parser import CykCalculator, CykSyntaxError
from predictive_parser import PredictiveCalculator, PredictiveSyntaxError


@pytest.mark.parametrize(
    "expr,expected",
    [
        ("2+3", 5.0),
        ("2+3*4", 14.0),
        ("(2+3)*4", 20.0),
        ("2*(3+4*2)", 22.0),
        ("10+20+30", 60.0),
    ],
)
def test_same_result(expr, expected):
    cyk_val = CykCalculator().parse_and_eval(expr)
    pred_val = PredictiveCalculator().parse_and_eval(expr)
    assert math.isclose(cyk_val, expected, rel_tol=1e-9)
    assert math.isclose(pred_val, expected, rel_tol=1e-9)


@pytest.mark.parametrize("expr", ["", "2+", "(*3)", "2+()", "(2+3"])
def test_invalid_expressions(expr):
    with pytest.raises((CykSyntaxError, ValueError)):
        CykCalculator().parse_and_eval(expr)
    with pytest.raises((PredictiveSyntaxError, ValueError)):
        PredictiveCalculator().parse_and_eval(expr)
