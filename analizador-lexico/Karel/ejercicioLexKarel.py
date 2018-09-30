import ply.lex as lex

tokens = ['START', 'DEF_FUNC','FUNC','DIGIT','NUMBER', 'IDENT', 'FOR',
          'TIMES', 'AS','NAME','EXPRESION']

t_NAME = r'\[[a-zA-Z_][a-zA-Z]*\]'
t_START = r'iniciar-programa'
t_ignore = ' \n'
t_DEF_FUNC = r'define\-nueva\-instruccion '+'[a-zA-Z_][a-zA-Z]*'+' como'
t_FOR = r'repetir'
t_TIMES = r'veces'
t_AS = r'como'
t_EXPRESION = r'[a-zA-Z_][a-zA-Z]*;'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer
archivo = open("textKarel.txt", "r") 

for linea in archivo.readlines():
    lex.input(linea)
    print("\nlinea : "+linea)
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " -> " + str(tok.type))

#######################################################


