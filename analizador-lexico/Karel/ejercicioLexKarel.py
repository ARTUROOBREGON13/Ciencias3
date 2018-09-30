import ply.lex as lex

tokens = ['START_PROGRAM', 'DEF_FUNC','FUNC','DIGIT','NUMBER', 'FOR',
          'TIMES', 'AS','NAME','GENERAL_EXPRESION', 'IDENT', 'EXECUTE',
          'END_EXECUTION', 'END_PROGRAM', 'OFF', 'LEFT','START','GET_BUZZ',
          'LEAVE_BUZZ','OUT','IF','THEN','ELSE','WHILE','DO','AND','OR',
          'NOT','STRING','LETTER']

#Expressions from Karel OMI
t_START_PROGRAM = r'iniciar-programa'
t_ignore = ' \n'
t_DEF_FUNC = r'define\-nueva\-instruccion'
t_FOR = r'repetir'
t_TIMES = r'veces'
t_AS = r'como'
t_GENERAL_EXPRESION = r'[a-zA-Z_][a-zA-Z0-9_]*;'
t_IDENT = r'\([a-zA-Z_][a-zA-Z0-9_]*\)'
t_EXECUTE = r'inicia-ejecucion'
t_END_EXECUTION = r'termina-ejecucion'
t_END_PROGRAM = r'finalizar-programa'
t_OFF = r'apagate;'
t_LEFT = r'gira-izquierda;'
t_START = r'inicio'
t_GET_BUZZ = r'coge-zumbador;'
t_LEAVE_BUZZ = r'deja-zumbador'
t_OUT = r'sal-de-instruccion'
t_IF = r'si'
t_THEN = r'entonces'
t_ELSE = r'sino'
t_WHILE = r'mientras'
t_DO = r'do'
t_AND = r'y'
t_OR = r'o'
t_NOT = r'no'
t_STRING =r'"[a-zA-Z_][a-zA-Z0-9_]"'
t_LETTER = r'[a-z_][A-Z]'


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


