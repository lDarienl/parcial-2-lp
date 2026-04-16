from __future__ import annotations

import argparse

from benchmark import run_benchmark
from cyk_parser import CykCalculator, CykSyntaxError
from predictive_parser import PredictiveCalculator, PredictiveSyntaxError
from tokenizer import TokenizeError


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculadora con parser CYK y parser predictivo")
    parser.add_argument("expr", nargs="?", help='Expresión, ej: "2 + 3 * (4 + 1)"')
    parser.add_argument("--parser", choices=["cyk", "predictive"], default="predictive")
    parser.add_argument("--benchmark", action="store_true", help="Ejecuta comparación de rendimiento")
    parser.add_argument("--max-ops", type=int, default=200, help="Número máximo de operaciones")
    parser.add_argument("--step", type=int, default=20, help="Paso de crecimiento de tamaño")
    parser.add_argument("--runs", type=int, default=20, help="Corridas por tamaño")
    args = parser.parse_args()

    if args.benchmark:
        rows = run_benchmark(max_ops=args.max_ops, step=args.step, runs=args.runs)
        print("ops,chars,cyk_ms,predictive_ms,ratio")
        for row in rows:
            print(
                f"{row['ops']},{row['chars']},{row['cyk_ms']:.4f},"
                f"{row['predictive_ms']:.4f},{row['ratio']:.2f}"
            )
        return 0

    if not args.expr:
        parser.error("Debes pasar una expresión o usar --benchmark")

    try:
        if args.parser == "cyk":
            result = CykCalculator().parse_and_eval(args.expr)
        else:
            result = PredictiveCalculator().parse_and_eval(args.expr)
    except (TokenizeError, CykSyntaxError, PredictiveSyntaxError) as exc:
        print(f"Error: {exc}")
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
