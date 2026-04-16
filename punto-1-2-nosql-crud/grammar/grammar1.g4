/*
 * DSL NoSQL CRUD — ver especificación en README.md del repositorio.
 * ANTLR4, objetivo Python 3.
 */
grammar grammar1;

// --- Programa -------------------------------------------------------------

programa
    : instruccion+ EOF
    ;

instruccion
    : createStmt ';'
    | readStmt ';'
    | updateStmt ';'
    | deleteStmt ';'
    ;

createStmt
    : INSERT INTO ID VALUES objeto
    ;

readStmt
    : GET FROM ID (WHERE condiciones)?
    ;

updateStmt
    : UPDATE ID SET ID ASSIGN valor WHERE condiciones
    ;

deleteStmt
    : DELETE FROM ID WHERE condiciones
    ;

// --- Documento JSON-like --------------------------------------------------

objeto
    : '{' ( par ( ',' par )* )? '}'
    ;

par
    : clave ':' valor
    ;

clave
    : STRING
    | ID
    ;

array
    : '[' ( valor ( ',' valor )* )? ']'
    ;

valor
    : STRING
    | NUMBER
    | TRUE
    | FALSE
    | NULL_
    | objeto
    | array
    | ID
    ;

// --- Condiciones (booleanas + comparación) -------------------------------

condiciones
    : expr
    ;

expr
    : expr OR andExpr
    | andExpr
    ;

andExpr
    : andExpr AND notExpr
    | notExpr
    ;

notExpr
    : NOT notExpr
    | primaryExpr
    ;

primaryExpr
    : '(' expr ')'
    | comparacion
    ;

comparacion
    : valor opComp valor
    ;

opComp
    : EQ
    | NE
    | GT
    | LT
    | GE
    | LE
    ;

// --- Lexer ----------------------------------------------------------------

INSERT  : 'INSERT';
INTO    : 'INTO';
VALUES  : 'VALUES';
GET     : 'GET';
FROM    : 'FROM';
WHERE   : 'WHERE';
UPDATE  : 'UPDATE';
SET     : 'SET';
DELETE  : 'DELETE';

AND : A N D;
OR  : O R;
NOT : N O T;

TRUE  : T R U E;
FALSE : F A L S E;
NULL_ : N U L L;

EQ : '==';
NE : '!=';
GE : '>=';
LE : '<=';
GT : '>';
LT : '<';
ASSIGN : '=';

NUMBER
    : INT ('.' INT)?
    ;

STRING
    : '"' ( ESC | ~[\\"\r\n] )* '"'
    ;

INVALID_ID
    : [0-9]+ [_a-zA-Z] [_a-zA-Z0-9]*
    ;

ID
    : [_a-zA-Z] [_a-zA-Z0-9]*
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> channel(HIDDEN)
    ;

WS
    : [ \t\r\n]+ -> channel(HIDDEN)
    ;

fragment INT : [0-9]+;

fragment ESC
    : '\\' ( ["\\/bfnrt] | 'u' HEX HEX HEX HEX )
    ;

fragment HEX : [0-9a-fA-F];

fragment A : [aA];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
