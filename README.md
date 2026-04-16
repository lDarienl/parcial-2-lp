# Parcial 2 — Lenguajes de programación y transducción

Repositorio con los puntos del parcial: gramática e implementación NoSQL (ANTLR), ambigüedad del `if`, comparación CYK vs predictivo, y parser descendente con `match`.

## Estructura de carpetas

```text
parcial-2-lp/
├── README.md                 ← Este archivo
├── .gitignore
├── punto-1-2-nosql-crud/     Puntos 1 y 2: DSL CRUD + ANTLR + Python
│   ├── grammar/
│   ├── scripts/              generate_parser.ps1, generate_parser_ubuntu.sh
│   ├── src/
│   ├── tests/
│   ├── tools/                JAR de ANTLR (opcional en git; ver .gitignore)
│   ├── pyproject.toml
│   └── requirements.txt
├── punto-3-ambiguedad/       Punto 3: demostración y corrección (markdown)
├── punto-4-cyk-calculator/   Punto 4: CYK vs parser predictivo + benchmark
│   ├── src/
│   ├── tests/
│   ├── comparaciones/
│   └── pyproject.toml
└── punto-5-recursive-descent/  Punto 5: descenso recursivo + match
    ├── src/
    ├── tests/
    └── pyproject.toml
```

## Resumen de cada punto

| Carpeta | Contenido |
|---------|-----------|
| **punto-1-2-nosql-crud** | Diseño de gramática (CRUD NoSQL estilo documentos) e implementación con **ANTLR4** y Python: lexer/parser generados, intérprete en memoria y pruebas. |
| **punto-3-ambiguedad** | Análisis de una gramática `if-then-else` / emparejamiento: demostración, corrección equivalente a la forma *matched/unmatched*, y notas de verificación (solo documentación). |
| **punto-4-cyk-calculator** | Parser **CYK** (CNF) y parser **predictivo** para una calculadora; script de **benchmark** y resultados comparativos en `comparaciones/`. |
| **punto-5-recursive-descent** | Algoritmo de emparejamiento **`match`** en un parser **descendente recursivo** LL(1): asignaciones, `if` / `else` y expresiones aritméticas. |

---

## Cómo ejecutar cada punto

### Requisitos comunes

- **Python 3.10+** (recomendado crear un venv en la raíz o dentro de cada carpeta de proyecto).

**Windows (PowerShell), ejemplo de venv en la raíz del repo:**

```powershell
cd "ruta\al\parcial-2-lp"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Ubuntu / Linux:**

```bash
cd /ruta/al/parcial-2-lp
python3 -m venv .venv
source .venv/bin/activate
```

---

### Punto 1 y 2 — `punto-1-2-nosql-crud`

1. **Instalar dependencias**

```powershell
cd punto-1-2-nosql-crud
python -m pip install -r requirements.txt pytest
```

2. **Regenerar el parser ANTLR** (solo si cambias `grammar/grammar1.g4` o clonas sin los `.py` generados). Necesitas **Java** en el `PATH`.

**Windows:**

```powershell
cd punto-1-2-nosql-crud
.\scripts\generate_parser.ps1
```

**Ubuntu:**

```bash
cd punto-1-2-nosql-crud
chmod +x scripts/generate_parser_ubuntu.sh
./scripts/generate_parser_ubuntu.sh
```

3. **Pruebas**

```powershell
cd punto-1-2-nosql-crud
python -m pytest -q
```

4. **Ejecutar el intérprete** (`PYTHONPATH` debe incluir `src`):

```powershell
cd punto-1-2-nosql-crud
$env:PYTHONPATH = "src"
python src/main.py tests/test_crud.nosql
```

---

### Punto 3 — `punto-3-ambiguedad`

No hay código ejecutable: revisa los archivos Markdown (`demostracion.md`, `correccion.md`, `verificacion.md`) en un visor o en el IDE.

---

### Punto 4 — `punto-4-cyk-calculator`

```powershell
cd punto-4-cyk-calculator
python -m pip install pytest
python -m pytest -q
```

Evaluar una expresión (desde `src`):

```powershell
cd punto-4-cyk-calculator\src
python main.py "2 + 3 * (4 + 1)" --parser cyk
python main.py "2 + 3 * (4 + 1)" --parser predictive
```

Benchmark (imprime CSV por consola):

```powershell
cd punto-4-cyk-calculator\src
python main.py --benchmark --max-ops 200 --step 20 --runs 20
```

En Ubuntu, sustituye rutas con `/` y usa `python3` si aplica.

---

### Punto 5 — `punto-5-recursive-descent`

```powershell
cd punto-5-recursive-descent
python -m pip install pytest
python -m pytest -q
```

El parser se usa importando `parse` desde `recursive_descent` con `PYTHONPATH=src`, o ampliando el proyecto con un `main.py` si lo necesitas para la defensa.

---

## Detalle del DSL (punto 1)

El lenguaje permite operaciones **CRUD** sobre colecciones de documentos con sintaxis inspirada en SQL y valores tipo JSON. Palabras reservadas incluyen `INSERT`, `GET`, `UPDATE`, `DELETE`, `FROM`, `INTO`, `SET`, `WHERE`, literales (`STRING`, `NUMBER`, booleanos, `null`), operadores de comparación y lógicos (`AND`, `OR`, `NOT`), y comentarios `//`. La gramática completa está en `punto-1-2-nosql-crud/grammar/grammar1.g4`.
