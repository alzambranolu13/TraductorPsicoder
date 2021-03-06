grammar Psicoder;

s                : (funcion | estructura)* funcion_principal (funcion | estructura)* EOF ;

funcion_principal   : 'funcion_principal' comandos 'fin_principal';

funcion             : 'funcion' tipo ID '(' parametros ')' 'hacer' comandos retornar 'fin_funcion';

retornar            : 'retornar' expr ';';

parametros          : tipo ID (',' tipo ID)*
                    | ;

estructura          : 'estructura' ID (declaracion)* 'fin_estructura';

declaracion         : tipo ID asignacion (',' ID asignacion)* ';' ;

asignacion          : '=' expr
                    | ;

comandos        	: comando comandos
                    | ;

comando             : si
                    | para
                    | mientras
                    | hacer_mientras
                    | seleccionar
                    | declaracion
                    | asignacion_id
                    | leer
                    | imprimir
                    | llamar_funcion ;

si                  : 'si' '(' expresion_logica ')' 'entonces' comandos si_no 'fin_si';
si_no               : 'si_no' comandos
                    | ;
para                : 'para' '(' (asignacion_id_para | asignacion_entero) ';' expresion_logica ';' (INT | ID) ')' 'hacer' comandos 'fin_para' ;
asignacion_entero   : 'entero' ID asignacion;
hacer_mientras      : 'hacer' comandos 'mientras' '(' expresion_logica ')' ';' ;
mientras            : 'mientras' '(' expresion_logica')' 'hacer' comandos 'fin_mientras';
seleccionar         : 'seleccionar' '(' ID ')' 'entre' casos 'fin_seleccionar';
casos               : caso casos
                    | defecto ;
caso                : 'caso' expr ':' comandos romper ;
defecto             : 'defecto' ':' comandos ;
asignacion_id_para  : ID '=' expr ;
asignacion_id       : id_pos_estruct '=' expr ';';
leer                : 'leer' '(' id_pos_estruct ')' ';';
imprimir            : 'imprimir' '(' (expr) (',' expr)* ')' ';';
romper              : 'romper' ';'
                    | ;
llamar_funcion_dentro : ID '(' pasar_parametros ')' ;
llamar_funcion      : ID '(' pasar_parametros ')' ';';
pasar_parametros    : expr (',' expr)*
                    | ;

expresion_logica    : expresion_logica ROL expresion_logica
                    | expresion_rop
                    | expresion_roi
                    |'(' expresion_logica ')'
                    | NEG expresion_logica
                    | expr ;

expresion_rop       : expr ROP expr ;
expresion_roi       : expr ROI expr ;



expr                : expr MULOP expr
                    | expr SUMOP expr
                    | PIZQ expr PDER
                    | llamar_funcion_dentro
                    | id_pos_estruct //Nueva opcion //Aun no esta implementado en el visitor
                    | DOUBLE
                    | INT
                    | CONST
                    | STRING
                    | ID
                    | BOOLEANO
                    ;

tipo                : 'entero'
                    | 'caracter'
                    | 'cadena'
                    | 'real'
                    | 'booleano'
                    | ID
                    ;

//Aun no esta implementado en el visitor
id_pos_estruct       : ID ('.' ID)* ; //id con posibilidad de ser estructura

COMMENT 		    : '/*' .*? '*/' -> skip ;
LINE_COMMENT 	    : '//' ~[\r\n]* -> skip ;
WS		            : [ \t\r\n]+ -> skip ;
PIZQ	            : '(' ;
PDER	            : ')' ;
NEG                 : '!' ;
ROI                 : ( '==' | '!=' ) ;
ROP		            : ( '<' | '<=' | '>=' | '>' ) ;
ROL                 : ( '&&' | '||');
SMCOLON             : ';' ;
COMA                : ',' ;
MULOP	            : ( '*' | '/' | '**' | '%' );
SUMOP	            : ('+' | '-') ;
DOUBLE	            : [0-9]+([.][0-9]+);
INT                 : [0-9]+;
STRING              : '"' .*? '"';
BOOLEANO            : ('verdadero' | 'falso');
CONST               : '\''[a-zA-Z]'\'';
ID 		            : [a-zA-Z][a-zA-Z0-9_]* ;