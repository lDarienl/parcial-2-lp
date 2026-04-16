from __future__ import annotations

import time

from cyk_parser import CykCalculator
from predictive_parser import PredictiveCalculator


def make_expression(ops: int) -> str:
    # Mezcla suma y producto para evitar casos triviales.
    # ops=4 -> "1+2*3+4*5"
    parts = ["1"]
    for i in range(2, ops + 2):
        op = "+" if i % 2 == 0 else "*"
        parts.append(op)
        parts.append(str(i))
    return "".join(parts)


def _avg_ms(fn, expr: str, runs: int) -> float:
    start = time.perf_counter()
    for _ in range(runs):
        fn(expr)
    end = time.perf_counter()
    return ((end - start) / runs) * 1000.0


def run_benchmark(max_ops: int = 200, step: int = 20, runs: int = 20):
    cyk = CykCalculator()
    predictive = PredictiveCalculator()
    rows = []
    for ops in range(step, max_ops + 1, step):
        expr = make_expression(ops)
        cyk_ms = _avg_ms(cyk.parse_and_eval, expr, runs)
        pred_ms = _avg_ms(predictive.parse_and_eval, expr, runs)
        rows.append(
            {
                "ops": ops,
                "chars": len(expr),
                "cyk_ms": cyk_ms,
                "predictive_ms": pred_ms,
                "ratio": (cyk_ms / pred_ms) if pred_ms > 0 else float("inf"),
            }
        )
    return rows
