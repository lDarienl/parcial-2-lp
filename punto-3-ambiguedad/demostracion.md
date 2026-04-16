## Punto 3 — ¿La gramática del enunciado sigue siendo ambigua?

Gramática propuesta:

- $\text{prop} \rightarrow \text{if expr then prop} \mid \text{prop\_emparejada}$
- $\text{prop\_emparejada} \rightarrow \text{if expr then prop\_emparejada else prop} \mid \text{otras}$

### 1. Qué habría que hacer para demostrar ambigüedad

Una gramática es **ambigua** si existe al menos una cadena terminal $w$ con **dos árboles de derivación distintos** (equivalentemente: dos derivaciones por la izquierda distintas). Hace falta exhibir **esa** $w$ y los **dos** árboles (o derivaciones), sin ambigüedad en el argumento.

### 2. La cadena clásica del “else colgante” no basta aquí

La cadena habitual es:

$$w = \texttt{if } e_1 \texttt{ then if } e_2 \texttt{ then } s_1 \texttt{ else } s_2$$

En la gramática ambigua “ingenua” ($S \to \texttt{if } E \texttt{ then } S \mid \texttt{if } E \texttt{ then } S \texttt{ else } S \mid \ldots$), esta cadena admite dos lecturas del `else`. **En la gramática del enunciado ocurre lo siguiente:**

**Lema (clave).** Todo símbolo derivable de $\text{prop\_emparejada}$ que **no** sea solo $\text{otras}$ y que **empiece** por `if` debe contener la palabra `else`. En efecto, la única producción de $\text{prop\_emparejada}$ que empieza por `if` es:

$$\text{if expr then prop\_emparejada else prop}$$

que introduce **siempre** un `else` en la cadena.

Por tanto, **no existe** una derivación de $\text{prop\_emparejada}$ cuya cadena sea exactamente $\texttt{if } e_2 \texttt{ then } s_1$ (un `if` interno **sin** `else`), salvo que $s_1$ sea en realidad $\text{otras}$ y no haya segundo `if` — lo cual no es el caso típico del ejemplo.

**Interpretación “el `else` va con el `if` externo”.** Haría falta una forma como:

$$\texttt{if } e_1 \texttt{ then } \underbrace{(\texttt{if } e_2 \texttt{ then } s_1)}_{\text{rama “then” del externo}} \texttt{ else } s_2$$

Es decir, entre el `then` del $e_1$ y el `else` que empareja al $e_1$, la subcadena debe ser derivable como **primer** $\text{prop\_emparejada}$ en una producción del tipo $\texttt{if } e_1 \texttt{ then prop\_emparejada else prop}$. Pero esa subcadena sería $\texttt{if } e_2 \texttt{ then } s_1$, y acabamos de ver que **no** puede provenir de $\text{prop\_emparejada}$.

Luego **esa segunda interpretación no es una derivación válida** en esta gramática.

**Interpretación “el `else` va con el `if` interno”.** Sí es posible, por ejemplo:

$$\text{prop} \Rightarrow \texttt{if } e_1 \texttt{ then prop} \Rightarrow \texttt{if } e_1 \texttt{ then prop\_emparejada} \Rightarrow \texttt{if } e_1 \texttt{ then (if } e_2 \texttt{ then prop\_emparejada else prop)} \Rightarrow \cdots \Rightarrow w$$

(con $\text{otras}$ para $s_1$ y $s_2$ según corresponda).

### 3. Conclusión respecto del enunciado

Para la cadena clásica $w$, **no** se obtienen dos árboles distintos: solo hay **una** derivación que termina en $w$. Por tanto, **esta gramática concreta no demuestra ambigüedad usando el ejemplo del else colgante**; de hecho, coincide con la idea estándar de separar lo “emparejado” ($\text{prop\_emparejada}$) de lo que puede quedar abierto ($\text{prop}$ en la rama del `then`).

Si el profesor exige textualmente “demuestre que sigue siendo ambigua”, hay dos salidas honestas en el examen:

1. **Señalar que el enunciado es engañoso:** la gramática dada es (salvo nombres) la **corrección** clásica; lo riguroso es demostrar **no** ambigüedad para $w$, o
2. Exhibir **otra** cadena $w'$ y **dos** árboles reales — lo cual, para *esta* gramática, no es trivial y puede no existir para el lenguaje generado (depende del lenguaje completo).

En la práctica, lo que suele valorarse es entender **por qué** el “else” queda forzado al `if` más interno en $w$: la restricción sobre $\text{prop\_emparejada}$ lo impide de otra forma.
