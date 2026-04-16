# Punto 5 — Descenso recursivo y algoritmo de emparejamiento (`match`)

## Qué pide el enunciado

1. **Algoritmo de emparejamiento** para un parser **descendente recursivo** (típicamente la función `match` / `eat` sobre el token actual).  
2. **Gramática** que incluya **asignación** y **condicionales**.  
3. **Pruebas** (aquí: tests automáticos) que validen sintaxis aceptada y rechazada.

## Por qué existe `match`

En descenso recursivo, cada regla **espera** terminales concretos (`;`, `=`, `if`, …).  
**Cómo funciona `match`:** si el token actual tiene el tipo esperado, **consume** (avanza el índice); si no, **error sintáctico** con mensaje claro.

**Por qué:** centraliza la comprobación de terminales y evita duplicar lógica en cada regla; es el “pegamento” entre lexer y parser.

## Gramática implementada (qué y por qué LL(1))

Programa y sentencias:

- `program → stmt_list EOF`  
- `stmt_list → stmt stmt_list | ε` (ε al llegar a `EOF` o al cerrar un bloque con `}`)  
- `stmt → assign | if_stmt`  
- `assign → ID '=' expr ';'`  
- `if_stmt → IF '(' expr ')' block else_opt`  
- `else_opt → ELSE block | ε`  
- `block → '{' stmt_list '}'`

Expresión (precedencia `* /` sobre `+ -`, paréntesis):

- `expr → term (('+'|'-') term)*`  
- `term → factor (('*'|'/') factor)*`  
- `factor → NUM | ID | '(' expr ')'`

**Por qué es LL(1) para elegir `stmt`:** el primer token de `assign` es siempre `ID`; el de `if_stmt` es `IF`. No hay ambigüedad con un solo símbolo de lookahead.

**Detalle importante (cómo):** la lista de sentencias **no** puede usar la misma condición de fin en el programa raíz que dentro de `{ ... }`. En la raíz se para en **EOF**; dentro del bloque se para antes de **`}`** y luego `match('RBRACE')` cierra el bloque. **Por qué:** si mezclas criterios, o fallas en programas válidos o aceptas basura.

## Archivos

| Archivo | Rol |
|---------|-----|
| `src/tokenizer.py` | Palabras clave (`if`, `else`), `ID`, `NUM`, operadores, llaves, `;`, token `EOF`. |
| `src/recursive_descent.py` | Parser + `match` / `advance` + `parse()` de entrada. |
| `tests/test_parser.py` | Casos válidos e inválidos. |

---

## Cómo ejecutarlo

**Windows:**

```powershell
cd punto-5-recursive-descent
python -m pip install pytest
python -m pytest -q
```

**Ubuntu / Linux:**

```bash
cd punto-5-recursive-descent
python3 -m pip install pytest
python3 -m pytest -q
```

Para usar el parser desde código, añade `src` al path de importación (`PYTHONPATH=src` o ejecuta tests como arriba).

## Ejemplo válido

```
x = 1;
if (x) {
  y = x + 2;
} else {
  y = 0;
}
```
