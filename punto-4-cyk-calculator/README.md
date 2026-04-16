## Punto 4 - CYK vs Predictivo

Implementación pedida:

- `src/cyk_parser.py`: parser CYK (programación dinámica) con gramática en CNF.
- `src/predictive_parser.py`: parser predictivo (descenso recursivo).
- `src/benchmark.py`: comparación de rendimiento.
- `src/main.py`: CLI para evaluar expresiones y correr benchmark.

### Gramática (informal)

- `expr -> expr + term | term`
- `term -> term * factor | factor`
- `factor -> NUM | ( expr )`

La versión CYK usa una transformación a CNF con no terminales auxiliares.

### Ejecutar pruebas

```powershell
cd punto-4-cyk-calculator
python -m pip install pytest
python -m pytest -q
```

### Evaluar una expresión

```powershell
cd punto-4-cyk-calculator/src
python main.py "2 + 3 * (4 + 1)" --parser cyk
python main.py "2 + 3 * (4 + 1)" --parser predictive
```

### Benchmark de rendimiento

```powershell
cd punto-4-cyk-calculator/src
python main.py --benchmark --max-ops 200 --step 20 --runs 20
```

Salida en CSV por consola: `ops,chars,cyk_ms,predictive_ms,ratio`.
