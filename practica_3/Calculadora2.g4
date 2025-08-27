grammar Calculadora2;

prog: expresion EOF ;

// Reglas con precedencia
expresion
    : expresion '^' expresion           # Potencia
    | expresion ('*'|'/') expresion     # MultDiv
    | expresion ('+'|'-') expresion     # AddSub
    | '-' expresion                     # Negativo
    | '+' expresion                     # Positivo
    | '(' expresion ')'                 # Parentesis
    | funcion                           # Funcion
    | NUMBER                            # Numero
    ;

funcion
    : ID '(' expresion ')'
    ;

// Tokens
NUMBER : [0-9]+ ('.' [0-9]+)? ;
ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
WS     : [ \t\r\n]+ -> skip ;
