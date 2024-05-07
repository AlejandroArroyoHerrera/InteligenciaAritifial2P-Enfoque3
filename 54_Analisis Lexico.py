import re

# Definir patrones para tokens del lenguaje simple
patrones = [
    ('IDENTIFICADOR', r'[a-zA-Z]\w*'),
    ('NUMERO', r'\d+'),
    ('ASIGNACION', r'\='),
    ('SUMA', r'\+'),
    ('RESTA', r'\-'),
    ('MULTIPLICACION', r'\*'),
    ('DIVISION', r'\/'),
    ('PARENTESIS_IZQ', r'\('),
    ('PARENTESIS_DER', r'\)'),
    ('FIN_SENTENCIA', r'\;')
]

# Función para analizar léxicamente una sentencia
def analizar_sentencia(sentencia, patrones):
    tokens = []
    while sentencia:
        encontrado = False
        for token, patron in patrones:
            match = re.match(patron, sentencia)
            if match:
                valor = match.group(0)
                tokens.append((token, valor))
                sentencia = sentencia[len(valor):].strip()
                encontrado = True
                break
        if not encontrado:
            raise ValueError('Sentencia no valida: ' + sentencia)
    return tokens

# Ejemplo de sentencia en el lenguaje simple a analizar
sentencia = "x = 10 + y * (z - 5);"

# Analizar léxicamente la sentencia
tokens = analizar_sentencia(sentencia, patrones)
print("Tokens de la sentencia:")
for token in tokens:
    print(token)
