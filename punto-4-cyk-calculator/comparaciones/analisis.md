# Punto 4 — Análisis de la comparación CYK vs predictivo

## Qué responde este archivo

El enunciado pide **comparar el rendimiento** de dos parsers sobre el **mismo** tipo de entrada. Aquí se documenta **cómo** se midió y **por qué** se interpretan así los resultados guardados en `resultados.csv`.

## Metodología (cómo)

- **Entrada:** expresiones de la forma `1+2*3+4*…` con un número creciente de **operaciones** (`ops`). Así crece \(n\) (tokens/caracteres) de forma controlada.  
- **Medición:** tiempo promedio por corrida (`runs` repeticiones) con `time.perf_counter()` en Python, para suavizar ruido de una sola ejecución.  
- **Salida:** por cada tamaño, `cyk_ms`, `predictive_ms` y `ratio = cyk_ms / predictive_ms`.

**Por qué promediar:** una sola medición mezcla ruido (planificador del SO, caché). El promedio no da complejidad formal, pero sí la **tendencia** que el enunciado pide comparar.

## Resultados de referencia (qué)

Archivo: `resultados.csv` (generado con `max-ops=120`, `step=20`, `runs=25` en la corrida documentada).

## Interpretación (por qué)

1. **Teoría:** CYK llena una tabla de tamaño \(\Theta(n^2)\) de celdas y cada celda puede combinar \(\Theta(n)\) cortes → **\(O(n^3)\)**. El descenso recursivo sin backtracking recorre la cadena una vez por nivel de reglas acotado → **\(O(n)\)** para esta gramática.  
2. **Práctica:** al subir `ops`, el tiempo del CYK crece **mucho más rápido** que el del predictivo; el `ratio` sube porque el costo cúbico domina antes que el lineal.  
3. **Por qué el ratio no es constante:** además de \(n\), influyen constantes grandes del CYK (conjuntos en Python, tablas) y efectos de hardware/caché; lo importante para el informe es la **tendencia**, no un factor fijo “teórico” \(n^2\) medido al pie de la letra en milisegundos.

## Conclusión

Para una calculadora (o un front-end de expresiones) con entradas largas, el **predictivo** es el enfoque razonable en implementaciones reales; el **CYK** es útil como ejercicio de algoritmo y como recordatorio de costo cuando la gramática está en CNF y se usa tabla completa.
