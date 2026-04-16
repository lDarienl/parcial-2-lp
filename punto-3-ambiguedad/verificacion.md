## Cómo “comprobar” la demostración y la corrección (sin obligar a código)

### Demostración (ambigüedad o no)

- **Ambigüedad:** hace falta una cadena $w$ **concreta** y **dos** árboles de derivación (o dos derivaciones por la izquierda) diferentes que generen exactamente $w$.
- **No ambigüedad para una cadena concreta:** basta una **prueba de imposibilidad** de una de las interpretaciones (como la de `demostracion.md`: `prop_emparejada` no genera `if e2 then s1` sin `else` en el patrón del else colgante).

No es necesario un programa si el curso es teórico: la comprobación es **revisar la derivación paso a paso** en el pizarrón o en papel.

### Si quieren un complemento automático (opcional)

- Un **parser** (ANTLR, Bison, etc.) con la gramática del enunciado y la cadena `if e1 then if e2 then s1 else s2` (sustituyendo `e1`, `e2`, `s1`, `s2` por tokens) suele producir **un solo** árbol; eso **apoya** la conclusión de no ambigüedad para esa cadena, pero **no sustituye** la demostración matemática (el parser implementa una estrategia concreta de desambiguación + puede haber errores en la `.g4`).

### Qué archivo añadir en el repo

Este `verificacion.md` sirve como **guía de entrega**: indica qué constituye evidencia válida. Si el profesor pide obligatoriamente implementación, entonces sí tendría sentido un mini proyecto con gramática + prueba; para teoría de lenguajes, **los `.md` bien argumentados suelen bastar**.
