from lib2to3.pgen2 import token
import ply.lex as lex
from ply.lex import TOKEN

class MyLex:


    @TOKEN(r'\+')
    def t_plus(self,t):
        t.type = '+'
        return t

    @TOKEN(r'-')
    def t_minus(self,t):
        t.type = '-'
        return t

    @TOKEN(r'\*')
    def t_times(self,t):
        t.type = '*'
        return t

    @TOKEN(r'/')
    def t_divide(self,t):
        t.type = '/'
        return t

    @TOKEN(r'\(')
    def t_oPrnt(self,t):
        t.type = '('
        return t

    @TOKEN(r'\)')
    def t_cPrnt(self,t):
        t.type = ')'
        return t

    @TOKEN(r'\{')
    def t_oCurly(self,t):
        t.type = '{'
        return t

    @TOKEN(r'\}')
    def t_cCurly(self,t):
        t.type = '}'
        return t

    @TOKEN(r'\.')
    def t_point(self,t):
        t.type = '.'
        return t

    @TOKEN(r':')
    def t_colon(self,t):
        t.type = ':'
        return t

    @TOKEN(r';')
    def t_semicolon(self,t):
        t.type = ';'
        return t

    @TOKEN(r',')
    def t_comma(self,t):
        t.type = ','
        return t

    @TOKEN(r'=')
    def t_equal(self,t):
        t.type = '='
        return t

    @TOKEN(r'>')
    def t_greaterThan(self,t):
        t.type = '>'
        return t

    @TOKEN(r'>')
    def t_smallerThan(self,t):
        t.type = '<'
        return t

    #se obtuvo de la documentacion oficial
    def t_error(self,t):
        print("Illegal character -->  '%s' <--" % t.value[0])
        t.lexer.skip(1)
        self.result = False

    #se obtuvo de la documentacion oficial
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    
    #@TOKEN(r'[a-zA-z]+([a-zA-Z0-9])*') version mala
    @TOKEN(r'[a-zA-Z](_?[a-zA-Z0-9]+)*')
    def t_ID(self,t):
        t.type = self.reserved.get(t.value,'ID')
        return t

    @TOKEN(r'var((t_ID(),|t_ID())+t_TIPO;)+')
    def t_VARS(self,t):
        t.type = "VARS"
        return t


    @TOKEN(r'[1-9][0-9]*\.[0-9]*')
    def t_CTEF(self,t):
        t.type = "CTEF"
        return t

    @TOKEN(r'[1-9][0-9]*')
    def t_CTEI(self,t):
        t.type = "CTEI"
        return t

    @TOKEN(r'\".*\"')
    def t_CTESTRING(self,t):
        return t

    @TOKEN(r't_ID()|t_CTEI()|t_CTEF()')
    def t_VARCTE(self,t):
        t.type = "VARCTE"
        return t

    @TOKEN(r't_EXP()|t_EXP()(<|>|<>)t_EXP()')
    def t_EXPRESION(self,t):
        return t

    @TOKEN(r't_TERMINO()|(t_TERMINO(\+|-))')
    def t_EXP(self,t):
        return t

    @TOKEN(r't_FACTOR()|(t_FACTOR(\*|/))')
    def t_TERMINO(self,t):
        return t

    @TOKEN(r'\(t_EXPRESION\)|(\+|-)?t_VARCTE()')
    def t_FACTOR(self,t):
        return t

    @TOKEN(r't_ID()=t_EXPRESION();')
    def t_ASIGNACION(self,t):
        return t

    @TOKEN(r'print\(((t_EXPRESION()|t_CTESTRING()),|(t_EXPRESION()|t_CTESTRING()))+\);')
    def ESCRITURA(self,t):
        return t

    @TOKEN(r'if\(t_EXPRESION()\)t_BLOQUE()(elset_BLOQUE())?;')
    def t_CONDICION(self,t):
        return t

    @TOKEN(r't_ASIGNACION()|t_CONDICION()|t_ESCRITUARA')
    def t_ESTATUTO(self,t):
        return t

    @TOKEN(r'\{t_ESTATUTO()*\}')
    def t_BLOQUE(self,t):
        return t

    @TOKEN(r'programt_ID();t_VARS()?t_BLOQUE()')
    def t_PROGRAMA(self,t):
        return t

    def testInput(self,test):
        self.result = True
        print('-'*6,"BEGIN LEX TEST",'-'*6)
        lex.input(test)
        while True:
            tok = lex.token()
            
            if not tok:
                print('-'*6,"END LEX TEST",'-'*6,"\n\n")
                break
            print(tok)
        return self.result
    
    def __init__(self):
        self.reserved = {
            'int': 'INT',
            'float':'FLOAT',
            'var': 'VARS',
            'if':'IF',
            'program':'PROGRAM',
            'print':'PRINT',
            'else':'ELSE'
        }

        self.literals = ['+','-','*','/','(',')','{','}','.',':',',',';','=','>','<']

        self.tokens = [ 'ID','CTEI', 'CTEF','CTESTRING'] + list(self.reserved.values())
    

        self.t_ignore  = ' \t'
        self.lexer = lex.lex(module=self) 