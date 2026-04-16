# Punto 3 — Demostración (respuesta al enunciado)

## Qué pide el enunciado

Demostrar si la gramática propuesta para `if-then-else` **sigue siendo ambigua**. Si lo fuera, habría que **corregirla** (ver `correccion.md`).

**Cómo se demuestra ambigüedad:** exhibir una cadena terminal \(w\) y **dos árboles de derivación distintos** (o dos derivaciones por la izquierda distintas) para la **misma** \(w\).

**Por qué:** la ambigüedad es una propiedad de la **gramática**, no de la intuición: o muestras dos árboles concretos, o no has demostrado ambigüedad.

---

## Gramática del enunciado

- \(\text{prop} \rightarrow \text{if expr then prop} \mid \text{prop\_emparejada}\)
- \(\text{prop\_emparejada} \rightarrow \text{if expr then prop\_emparejada else prop} \mid \text{otras}\)

---

## Cadena típica del “else colgante”

\(w = \texttt{if } e_1 \texttt{ then if } e_2 \texttt{ then } s_1 \texttt{ else } s_2\).

En la gramática **ingenua** (\(\texttt{if} \ldots \texttt{then } S \mid \texttt{if} \ldots \texttt{then } S \texttt{ else } S\)), esta \(w\) suele admitir **dos** lecturas del `else`. Aquí ocurre otra cosa.

### Por qué no aparecen dos árboles para \(w\)

**Hecho:** todo \(\text{prop\_emparejada}\) que no sea solo \(\text{otras}\) y que **empiece** por `if` **contiene** la palabra `else`, porque la única producción “`if`…” de \(\text{prop\_emparejada}\) es  
\(\texttt{if expr then prop\_emparejada else prop}\).

**Consecuencia:** la subcadena \(\texttt{if } e_2 \texttt{ then } s_1\) (**sin** `else` entre el `then` de \(e_2\) y el final de esa subcadena) **no** puede ser un \(\text{prop\_emparejada}\) completo (salvo casos triviales que no son el patrón del else colgante).

La interpretación “el `else` pertenece al `if` **externo**” exige, entre el `then` de \(e_1\) y ese `else`, exactamente un \(\text{prop\_emparejada}\) que sea \(\texttt{if } e_2 \texttt{ then } s_1\). Eso **contradice** el hecho anterior: **esa derivación no existe**.

La interpretación “el `else` pertenece al `if` **interno**” sí se construye vía \(\text{prop} \Rightarrow \texttt{if } e_1 \texttt{ then prop}\) y luego \(\text{prop\_emparejada}\) en el \(\text{prop}\) interior.

**Conclusión para \(w\):** con esta gramática hay **una sola** derivación (un solo árbol) para el ejemplo clásico. **No** demuestra ambigüedad con \(w\).

---

## Cómo responder si el enunciado exige “sigue siendo ambigua”

1. **Honestidad académica:** la gramática dada coincide con el esquema clásico **emparejado / abierto** (misma idea que en `correccion.md`); para \(w\) lo riguroso es argumentar **no ambigüedad**, no inventar una segunda derivación.
2. **Alternativa estricta:** solo si encuentras **otra** cadena \(w'\) con **dos** árboles explícitos para *esta* gramática (en general no es el enfoque habitual de este ejercicio).

En la práctica suele valorarse entender **por qué** el `else` queda asociado al `if` interno en \(w\): la forma de \(\text{prop\_emparejada}\) **impide** meter un `if` sin `else` en la posición que exigiría el `else` externo.
