## Corrección (gramática no ambigua) — relación con el enunciado

La solución estándar en libros de compiladores (p. ej. *Dragon Book*) separa **sentencias emparejadas** (cada `if` tiene su `else` cuando hace falta) y **sentencias no emparejadas** / abiertas. Una forma equivalente es:

$$\begin{aligned}
\text{stmt} &\to \text{matched\_stmt} \mid \text{unmatched\_stmt} \\
\text{matched\_stmt} &\to \texttt{if expr then matched\_stmt else matched\_stmt} \mid \texttt{otras} \\
\text{unmatched\_stmt} &\to \texttt{if expr then stmt} \\
&\mid \texttt{if expr then matched\_stmt else unmatched\_stmt}
\end{aligned}$$

### Equivalencia con la gramática del enunciado

Si renombramos:

| Enunciado | Rol |
|-----------|-----|
| `prop` | Mezcla de sentencias “abiertas” y “emparejadas” → corresponde a `stmt`. |
| `prop_emparejada` | Solo formas donde cada `if` que abre con reglas de `prop_emparejada` va acompañado de `else` en la misma plantilla → corresponde a `matched_stmt`. |

Entonces:

- `prop → if expr then prop` es la rama “`if` sin emparejar en la rama then” (`unmatched` parcial).
- `prop → prop_emparejada` permite que la sentencia completa sea una sentencia emparejada.
- `prop_emparejada → if expr then prop_emparejada else prop` es `if expr then matched_stmt else stmt`: la rama del `then` debe ser **emparejada**; la del `else` puede ser cualquier `stmt` (abierta o no).

Esa es **exactamente** la restricción que elimina el “dangling else” para la cadena típica: no puedes colocar un `if` sin `else` “en medio” de un `if … else` externo cuando la gramática exige que esa posición sea `prop_emparejada`.

### La tabla “prop_match / prop_open” que suele escribirse en clase

Muchas guías presentan lo mismo con otros nombres:

$$\text{prop} \to \text{prop\_match} \mid \text{prop\_open}$$

con reglas análogas a `matched_stmt` y `unmatched_stmt`. Es **la misma idea** que el enunciado con `prop` y `prop_emparejada`; no es un “parche” distinto, sino una **reorganización** para que la lectura sea más clara.

### Resumen para el informe

- La gramática del **enunciado ya está diseñada para quitar la ambigüedad del `else` colgante** respecto de la gramática ingenua.
- La “corrección” de los libros **no contradice** al enunciado: la **refina** en notación (`matched` / `unmatched` o `match` / `open`) y demuestra por qué funciona.

Si piden “operaciones para que no sea ambigua” pensando en la gramática **ingenua** de un solo no terminal, las operaciones son: **introducir un no terminal de sentencias emparejadas** y **restringir** dónde puede aparecer un `if` sin `else` (solo en ramas `then` controladas por estas reglas).
