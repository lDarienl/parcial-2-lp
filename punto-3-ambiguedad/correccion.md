# Punto 3 — Corrección (gramática no ambigua)

## Qué pide el enunciado (segunda parte)

Si la gramática fuera ambigua, hay que aplicar las **operaciones habituales** para obtener una **no ambigua**: separar lo que puede “quedar abierto” (un `if` sin `else` pendiente) de lo que va **emparejado** (cada `if` en ciertas posiciones va obligado con su `else` en la plantilla).

## Gramática estándar (por qué funciona)

Se usan dos no terminales (nombres del *Dragon Book*):

| Rol | Idea |
|-----|------|
| `matched_stmt` | Sentencias donde cada `if` introducido por la regla recursiva “cerrada” va con su `else` en la misma plantilla. |
| `unmatched_stmt` | Sentencias con al menos un `if` que puede quedar **sin** `else` “resuelto” en esa rama. |

$$
\begin{aligned}
\text{stmt} &\to \text{matched\_stmt} \mid \text{unmatched\_stmt} \\
\text{matched\_stmt} &\to \texttt{if expr then matched\_stmt else matched\_stmt} \mid \texttt{otras} \\
\text{unmatched\_stmt} &\to \texttt{if expr then stmt} \\
&\mid \texttt{if expr then matched\_stmt else unmatched\_stmt}
\end{aligned}
$$

**Por qué elimina el dangling else:** en \(\texttt{if } e_1 \texttt{ then } \boxed{\phantom{S}} \texttt{ else } \ldots\), lo que puede ir en \(\boxed{\phantom{S}}\) cuando debe ser “emparejado” **no** puede ser un `if` suelto sin reglas que fuercen su `else` en el lugar adecuado; la gramática **restringe** esa posición a `matched_stmt` donde la estructura del `else` está controlada.

## Cómo se relaciona con la gramática del enunciado

Renombrando:

| Enunciado | Rol |
|-----------|-----|
| `prop` | Mezcla “abierta + emparejada” → análogo a `stmt`. |
| `prop_emparejada` | Formas construidas solo con la plantilla `if … then … else …` (hasta llegar a `otras`) → análogo a `matched_stmt`. |

- `prop → if expr then prop` permite el caso **abierto** en la rama del `then` (como `unmatched_stmt → if expr then stmt`).
- `prop_emparejada → if expr then prop_emparejada else prop` obliga a que entre el `then` y el `else` haya algo **emparejable** por esa regla; el `else` cierra con un `prop` general.

**Conclusión:** la “corrección” de los libros y la del enunciado son la **misma idea** con distinto nombre; no es un algoritmo distinto, es la **misma restricción** hecha explícita para el análisis LL.

## Nombres alternativos (`prop_match` / `prop_open`)

Algunas guías escriben \(\text{prop} \to \text{prop\_match} \mid \text{prop\_open}\) con reglas equivalentes. **Misma técnica**, distinta etiqueta: sirve para explicar en clase sin depender del nombre `matched_stmt`.
