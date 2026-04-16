## Análisis de rendimiento: CYK vs Predictivo

Configuración usada:

- `max-ops=120`
- `step=20`
- `runs=25`
- Expresiones del tipo `1+2*3+4*...`

Resultados en `resultados.csv`.

Observaciones:

1. El parser predictivo crece de forma aproximadamente lineal con el tamaño de la entrada.
2. El parser CYK aumenta mucho más rápido al crecer la longitud de la cadena.
3. En las pruebas, CYK termina entre `50x` y `~890x` más lento que el predictivo.

Conclusión:

- La comparación empírica coincide con la teoría:
  - CYK: complejidad cúbica `O(n^3)`.
  - Predictivo LL(1)/descenso recursivo: complejidad lineal `O(n)` para esta gramática.
- Para entradas grandes, el parser predictivo es claramente más apropiado para una calculadora.
