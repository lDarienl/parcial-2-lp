# Parcial 2 — Lenguajes de programación y transducción

Repositorio con la resolución integral del parcial: gramática NoSQL (ANTLR), análisis de ambigüedad, comparación de rendimiento CYK vs Predictivo, y parser descendente manual.

## Estructura de carpetas

```text
parcial-2-lp/
├── README.md                 ← Este archivo
├── venv/                     ← Entorno virtual (no incluido en git)
├── punto-1-2-nosql-crud/     Puntos 1 y 2: DSL CRUD + ANTLR + Python
│   ├── grammar/              Gramática .g4
│   ├── scripts/              Scripts de generación (Bash/PS)
│   ├── src/                  Código fuente del intérprete
│   └── tests/                Pruebas unitarias (pytest)
├── punto-3-ambiguedad/       Punto 3: Análisis teórico (Markdown)
├── punto-4-cyk-calculator/   Punto 4: CYK vs Predictivo + Benchmark
│   ├── src/                  Implementación de algoritmos
│   └── comparaciones/        Resultados y análisis de rendimiento
└── punto-5-recursive-descent/ Punto 5: Descenso recursivo + match
    ├── src/                  Código del parser manual
    └── tests/                Pruebas de gramática
```

## Resumen de cada punto

| Carpeta | Contenido |
|---------|-----------|
| **punto-1-2-nosql-crud** | Diseño de gramática NoSQL e implementación con **ANTLR4**. Incluye un intérprete en memoria con soporte para operaciones CRUD completas y filtrado dinámico. |
| **punto-3-ambiguedad** | Demostración de la ambigüedad del `if-then-else` y corrección mediante la técnica de sentencias emparejadas (*matched/unmatched*). |
| **punto-4-cyk-calculator** | Implementación del algoritmo **CYK** ($O(n^3)$) y un parser **predictivo** ($O(n)$) para comparar empíricamente la eficiencia de la programación dinámica frente a técnicas LL(1). |
| **punto-5-recursive-descent** | Implementación manual de un parser descendente recursivo utilizando una función **`match`** para validar la sintaxis de asignaciones y condicionales. |

---

## Configuración Inicial (Ubuntu / EC2)

Antes de ejecutar los puntos, prepara el entorno virtual en la raíz del proyecto:

```bash
sudo apt update && sudo apt install -y python3-venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

---

## Ejecución por Puntos

### Punto 1 y 2 — NoSQL CRUD (ANTLR4)

1. **Instalar dependencias y generar parser:**
```bash
cd punto-1-2-nosql-crud
pip install -r requirements.txt pytest
chmod +x scripts/generate_parser_ubuntu.sh
./scripts/generate_parser_ubuntu.sh
```

2. **Ejecutar Pruebas Unitarias:**
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
pytest tests/
```

3. **Probar el intérprete con un script `.nosql`:**
```bash
python3 src/main.py tests/test_crud.nosql
```

---

### Punto 3 — Ambigüedad (Documentación)

Este punto es de carácter teórico. Los archivos detallan la lógica de resolución del problema del *dangling else*:
* `demostracion.md`: Prueba de la ambigüedad en la gramática original.
* `correccion.md`: Propuesta de gramática jerarquizada no ambigua.

---

### Punto 4 — CYK vs Predictivo (Benchmark)

1. **Ejecutar el Benchmark de rendimiento:**
```bash
cd punto-4-cyk-calculator/src
python3 main.py --benchmark --max-ops 120 --step 20 --runs 25
```
*Nota: Este comando generará una tabla comparativa demostrando la superioridad del parser predictivo en entradas largas.*

2. **Probar un cálculo específico:**
```bash
python3 main.py "5 + 10 * (2 + 3)" --parser cyk
```

---

### Punto 5 — Descenso Recursivo (Match)

1. **Validar la gramática (Asignaciones e IF/ELSE):**
```bash
cd punto-5-recursive-descent
pytest tests/
```

2. **Prueba rápida por consola:**
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python3 -c "from src.recursive_descent import parse; parse('x = 5; if (x) { y = 10; }'); print('Sintaxis válida')"
```

---

## Detalle Técnico del DSL
El lenguaje diseñado permite manipular documentos similares a JSON. Soporta:
- **Operaciones:** `INSERT INTO`, `GET FROM`, `UPDATE SET`, `DELETE FROM`.
- **Tipos de Datos:** Strings, Numbers, Booleans y Null.
- **Lógica:** Paréntesis para agrupación y operadores `AND`, `OR`, `NOT`.
- **Filtros:** Cláusula `WHERE` con operadores de comparación (`==`, `!=`, `>`, `<`, etc.).