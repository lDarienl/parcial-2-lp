# Punto 4 — CYK vs parser predictivo (calculadora)

## Qué pide el enunciado

1. **Parser CYK** para reconocer (y aquí también **evaluar**) expresiones de calculadora.  
2. **Parser predictivo** del mismo lenguaje.  
3. **Pruebas de rendimiento** y **comparación** entre ambos.

## Por qué dos implementaciones

- **CYK:** tabla dinámica; exige gramática en **CNF**; tiempo típico **\(O(n^3)\)** en el número de tokens \(n\). Sirve como algoritmo general cuando la gramática está en CNF y se quiere decisión de pertenencia sin construir a mano un parser específico.  
- **Predictivo (descenso recursivo):** guía el análisis con el **token actual** (y lookahead si hace falta); para esta gramática el recorrido es **\(O(n)\)** porque cada token se examina un número constante de veces.

**Idea clave:** mismo lenguaje superficial, **distinto costo algorítmico**; la comparación debe mostrar esa brecha al crecer \(n\).

## Qué hay en esta carpeta

| Ruta | Función |
|------|---------|
| `src/cyk_parser.py` | CYK + evaluación sobre CNF auxiliar. |
| `src/predictive_parser.py` | Descenso recursivo LL(1) clásico (`expr` / `term` / `factor`). |
| `src/tokenizer.py` | Lexer común (`NUM`, `+`, `*`, `(`, `)`). |
| `src/benchmark.py` | Genera expresiones de longitud creciente y mide tiempos. |
| `src/main.py` | CLI: evaluar una expresión o `--benchmark`. |
| `tests/test_calculators.py` | Misma semántica en ambos parsers + errores. |
| `comparaciones/` | `resultados.csv` + `analisis.md` (corrida de referencia). |

## Gramática (informal del lenguaje)

- `expr → expr + term | term`  
- `term → term * factor | factor`  
- `factor → NUM | ( expr )`  

El CYK usa una **transformación a CNF** (no terminales extra); el predictivo implementa **directamente** la precedencia (`*` antes que `+`).

---

## Cómo ejecutarlo

### Pruebas unitarias

**Windows (PowerShell):**

```powershell
cd punto-4-cyk-calculator
python -m pip install pytest
python -m pytest -q
```

**Ubuntu / Linux:**

```bash
cd punto-4-cyk-calculator
python3 -m pip install pytest
python3 -m pytest -q
```

### Evaluar una expresión

Desde `src` (el `PYTHONPATH` implícito es el directorio de trabajo al ejecutar `main.py` ahí):

```powershell
cd punto-4-cyk-calculator\src
python main.py "2 + 3 * (4 + 1)" --parser cyk
python main.py "2 + 3 * (4 + 1)" --parser predictive
```

```bash
cd punto-4-cyk-calculator/src
python3 main.py "2 + 3 * (4 + 1)" --parser cyk
```

### Benchmark (comparación de rendimiento)

```powershell
cd punto-4-cyk-calculator\src
python main.py --benchmark --max-ops 200 --step 20 --runs 20
```

Salida: CSV por consola `ops,chars,cyk_ms,predictive_ms,ratio`. Los mismos parámetros puedes volcarlos a archivo si lo pide la rúbrica.

---

## Limitación (honestidad técnica)

El benchmark mide **tiempo de pared** en Python: depende de CPU, caché, GC, etc. La **tendencia** (CYK empeora mucho más rápido) debe alinearse con **\(O(n^3)\) vs \(O(n)\)**; los números exactos del ratio pueden variar entre máquinas.
