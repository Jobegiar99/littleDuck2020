// Define a grammar called Hello
grammar littleDuck;


INT: 'int';
FLOAT: 'float';
VARS: 'var';
IF : 'if' WS* '('  WS*;
ELSE : 'else';
PROGRAM: 'program';
PRINT: 'print' WS* '(' WS*;

ID : [a-z]['_'(a-zA-Z0-9)+]* ;
CTEI: [1-9][0-9]*;
CTEF: [1-9d][0-9]*('.'[0-9]+)?;
CTESTRING: '"'.*?'"' ;



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

program0 : WS* PROGRAM ID ';' program1 ;
program1: 
                      vars0  bloque0 end0
                      | bloque0 end0;

end0 : EOF;

tipo0: INT | FLOAT;

vars0: VARS vars1;
vars1: ID ',' vars1
            | ID ':' vars2;
vars2: vars3 vars1
             | vars3;
vars3: tipo0 ';'; 

bloque0: '{' bloque1;
bloque1:  
                   estatuto0 bloque1
                 | '}';

estatuto0: 
                          condicion0 
                        | escritura0 
                        | asignacion0;

condicion0:  IF expresion0 ')' bloque0 condicion1 ;
condicion1: ELSE bloque0 ';' | ';';

escritura0:  PRINT escritura1;
escritura1:  CTESTRING escritura2
                        | expresion0 escritura2;
escritura2: ',' escritura1 
                        | ')' ';';


asignacion0: ID  '=' expresion0 ';';


expresion0: 
                            exp0 
                            | exp0 '<' exp0
                            | exp0 '>' exp0
                            | exp0 '<' '>' exp0;
                            
exp0: 
            termino0 '+' exp0
            | termino0 '-' exp0
            | termino0;

termino0: 
                      factor0 
                    | factor0 '*' termino0
                    | factor0 '/' termino0;

factor0: '(' expresion0 ')' 
                 | factor1;

factor1: '+' varcte0
                 | '-' varcte0
                 |varcte0;

varcte0: ID | CTEI | CTEF;









