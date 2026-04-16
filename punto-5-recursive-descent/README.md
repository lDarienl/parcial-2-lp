## Punto 5 — Descenso recursivo y `match`

### Qué se implementó

- **`match`**: consume el token actual si su tipo coincide con el esperado; si no, lanza `ParseError`.
- **Gramática LL(1)** con asignaciones (`ID = expr ;`), condicionales `if ( expr ) { ... }` y opcional `else { ... }`.
- **Expresiones** tipo calculadora: `+ - * /`, paréntesis, `NUM`, `ID`.

### Corrección respecto al borrador

1. **Lista de sentencias**: no se puede usar “hasta `}`” en el programa raíz. Se parametriza el fin de `stmt_list`: termina en **EOF** o en **`}`** (dentro de un bloque).
2. **`else` opcional**: con `if ... { }` solo, al salir del bloque el siguiente token puede ser `else`, otro `if`, un `ID`, `}` o EOF.
3. **Lexer propio**: el del punto 4 no traía `if`, `else`, `;`, `{`, `}`, ni `ID`.

### Pruebas

```powershell
cd punto-5-recursive-descent
python -m pip install pytest
python -m pytest -q
```

### Ejemplo de programa válido

```
x = 1;
if (x) {
  y = x + 2;
} else {
  y = 0;
}
```
