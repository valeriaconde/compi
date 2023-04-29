grammar LittleDuck;

// PROGRAMA
programa: PROG ID SEMICOLON (vars)? cuerpo END;
//a: | vars;

// VARS
vars: VAR (tipo COLON var_id (COMMA var_id)* pnvar SEMICOLON)+ ;
pnvar: ;

var_id: ID ;

// CUERPO
cuerpo: OPENB estatuto* CLOSEB;

// TIPO
tipo: INT | FLOAT;

// ESTATUTO
estatuto: asigna 
        | condicion 
        | ciclo 
        | escritura;

// ASIGNA
asigna: asigna_var EQUALS exit_equals expresion SEMICOLON;
asigna_var: ID ;
exit_equals: ;

// EXPRESION
expresion: exp exit_exp h;
h: 
    | MORETHAN exit_morethan exp exit_exp
    | LESSTHAN exit_lessthan exp exit_exp
    | NOT exit_not exp exit_exp;
exit_morethan: ;
exit_lessthan: ;
exit_not: ;
exit_exp: ;

// CONDICION
condicion: SI OPENP exit_openp expresion CLOSEP exit_closep exit_si cuerpo m SEMICOLON exit_condition;
m: 
    | SINO exit_sino cuerpo;

exit_openp: ;
exit_closep: ;
exit_si: ;
exit_sino: ;
exit_condition: ;

// CICLO
ciclo: MIENTRAS exit_while OPENP exit_openp expresion CLOSEP exit_closep exit_si cuerpo SEMICOLON exit_endwhile;
exit_while: ;
exit_endwhile: ;

// ESCRITURA
escritura: PRINT OPENP exit_openp contenido CLOSEP exit_closep SEMICOLON;
contenido: expresion | STRING ;

// EXP
exp: termino exit_termino ((PLUS exit_plus | MINUS exit_minus) termino exit_termino)*;
exit_plus: ;
exit_minus: ;

// TERMINO
termino: factor exit_factor ((TIMES exit_times | DIVISION exit_division) factor exit_factor)*;
exit_times: ;
exit_division: ;
exit_termino: ;
exit_factor: ;

// FACTOR
factor: OPENP exit_openp expresion CLOSEP exit_closep
    | PLUS exit_plus var_cte
    | MINUS exit_minus var_cte
    | var_cte;
    
// VAR_CTE
var_cte: ID | CTE_I | CTE_F;


// TOKENS //
SEMICOLON: ';' ;
COLON: ':';
OPENP: '(';
CLOSEP: ')';
OPENB: '[';
CLOSEB: ']';
COMMA: ',';
PLUS: '+';
EQUALS: '=';
MINUS: '-';
TIMES: '*';
DIVISION: '/';
MORETHAN: '>';
LESSTHAN: '<';
NOT: '<>';
PRINT: 'print';
PROG: 'prog';
END: 'end';
VAR: 'var';
INT: 'int';
FLOAT: 'float';
SI: 'si';
SINO: 'sino';
MIENTRAS: 'mientras';
STRING: '"' ( ~('\'' | '\\' | '\n' | '\r') ) + '"' ;
CTE_I: [0-9]+ ;
CTE_F: [+-]?([0-9]*[.])?[0-9]+;
ID: [a-zA-Z][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;

