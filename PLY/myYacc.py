import ply.yacc as yacc
from myLex import MyLex
class MyYacc:

    tokens = MyLex().tokens

    def p_program0(self,p):
        '''
        program0 : PROGRAM ID ';'  program1
        '''
        p[0] = p[1:]

    def p_program1(self,p):
        '''
        program1 : vars0  bloque 
                            | bloque 
        '''
        p[0] = p[1:]

    def p_tipo(self,p):
        '''
        tipo : INT 
                    | FLOAT
        '''
        p[0] = ''.join(p[1])

    def p_empty(self,p):
        'empty :'
        pass

    def p_vars0(self,p):
        '''
        vars0 : VARS vars1
        '''
        p[0] = p[1:]

    def p_vars1(self,p):
        '''
        vars1 : ID ',' vars1
                    | ID ':' vars2
        '''
        p[0] = p[1:]

    def p_vars2(self,p):
        '''
        vars2 : vars3 vars1 
                    | vars3
        '''
        p[0] = p[1:]
            
    def p_vars3(self,p):
        '''
         vars3 : tipo ';' 
        '''
        p[0] = p[1:]

    def p_bloque(self,p):
        '''
        bloque : '{' bloque2
        '''
        p[0] = p[1:]

    def p_bloque2(self,p):
        '''
        bloque2 : '}'
                        |  estatuto bloque2
        '''
        p[0] = p[1:]



    def p_estatuto(self,p):
        '''
        estatuto : asignacion
                            | condicion
                            | escritura0
        '''
        p[0] = p[1:]

    def p_asignacion(self,p):
        '''
        asignacion : ID '=' expresion0 ';'
        '''
        p[0] = p[1:]

    def p_escritura0(self,p):
        '''
        escritura0 : PRINT '('  escritura1
        '''
        p[0] = p[1:]

    def p_escritura1(self,p):
        '''
        escritura1 : expresion0 escritura2
                                | CTESTRING escritura2
        '''
        p[0] = p[1:]

    def p_escritura2(self,p):
        '''
        escritura2 :  ',' escritura1
                                 |  ')' ';'
        '''
        p[0] = p[1:]

    def p_expresion0(self,p):
        '''
        expresion0 : exp0
                                  | exp0 '>' exp0
                                 | exp0 '<' exp0
                                 | exp0 '<' '>' exp0
        '''
        p[0] = p[1:]
    
    def p_exp0(self,p):
        '''
        exp0 : termino0 '+' exp0 
                    | termino0 '-' exp0 
                    | termino0
        '''
        p[0] = p[1:]

    def p_termino0(self,p):
        '''
        termino0 : factor0 '*' termino0 
                            | factor0 '/' termino0 
                            | factor0
        '''
        p[0] = p[1:]

    def p_factor0(self,p):
        '''
        factor0 : '(' expresion0 ')' 
                          | factor1
        '''
        p[0] = p[1:]

    def p_factor1(self,p):
        '''
        factor1 : '+' varcte0 
                          | '-' varcte0 
                          | varcte0
        '''
        p[0] = p[1:]

    def p_condicion(self,p):
        '''
        condicion : IF '(' expresion0 ')' bloque condicion1
        '''
        p[0] = p[1:]

    def p_condicion1(self, p):
        '''
        condicion1 : ELSE bloque ';' 
                                | ';'
        '''
        p[0] = p[1:]

    def p_varcte0(self,p):
        '''
        varcte0 : ID 
                            | ctei0
                            | ctef0
        '''
        p[0] = p[1]

    def p_ctei0(self,p):
        '''
        ctei0 : CTEI
        '''
        p[0] = int(p[1])
    
    def p_ctef0(self,p):
        '''
        ctef0 : CTEF
        '''
        p[0] = float(p[1])

    def testInput(self,input):
        print('-'*6,"BEGIN YACC TEST",'-'*6)
        while True:
            result = self.parser.parse(input)
            if result == None:
                return False
                break
            print('-'*6,"STRING VERSION: ",'-'*6,"\n",self.resultToString(result))
            print('-'*6,"ARRAY VERSION: ",'-'*6,"\n",result)
            break      
        print('-'*6,"END YACC TEST",'-'*6,"\n\n")
        return True
            
    def resultToString(self,result):
        answer = ""
        for r in result:
            if type(r) == list:
                answer += self.resultToString(r)
            else:
                answer += str(r)
        return answer



    def __init__(self, tokens):
        self.parser = yacc.yacc(module=self)

    
        
