import ply.yacc as yacc

# Definir las reglas de la gramática
def p_sentencia(p):
    '''
    sentencia : asignacion FIN_SENTENCIA
              | expresion FIN_SENTENCIA
    '''
    print("Análisis Sintáctico: Sentencia")

def p_asignacion(p):
    '''
    asignacion : IDENTIFICADOR ASIGNACION expresion
    '''
    print("Análisis Sintáctico: Asignación")

def p_expresion(p):
    '''
    expresion : termino
             | expresion SUMA termino
             | expresion RESTA termino
    '''
    print("Análisis Sintáctico: Expresión")

def p_termino(p):
    '''
    termino : factor
            | termino MULTIPLICACION factor
            | termino DIVISION factor
    '''
    print("Análisis Sintáctico: Término")

def p_factor(p):
    '''
    factor : IDENTIFICADOR
           | NUMERO
           | PARENTESIS_IZQ expresion PARENTESIS_DER
    '''
    print("Análisis Sintáctico: Factor")

# Build the parser
parser = yacc.yacc()

# Ejemplo de sentencia en el lenguaje simple
sentencia = "x = 10 + y * (z - 5);"

# Analizar sintácticamente la sentencia
parser.parse(sentencia)
