"""Ejecuta un archivo .nosql o lee del stdin y muestra el resultado del último GET."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from nosql_dsl import InMemoryCrudInterpreter, parse_program


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Intérprete DSL NoSQL CRUD (demo en memoria).")
    p.add_argument(
        "archivo",
        nargs="?",
        help="Ruta al script; si se omite, se lee de stdin.",
    )
    p.add_argument(
        "--solo-parse",
        action="store_true",
        help="Solo validar sintaxis (no ejecutar).",
    )
    args = p.parse_args(argv)

    if args.archivo:
        source = Path(args.archivo).read_text(encoding="utf-8")
    else:
        source = sys.stdin.read()

    if args.solo_parse:
        parse_program(source)
        print("OK: sintaxis válida.")
        return 0

    vm = InMemoryCrudInterpreter()
    vm.run(source)
    print(json.dumps(vm.last_read, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
