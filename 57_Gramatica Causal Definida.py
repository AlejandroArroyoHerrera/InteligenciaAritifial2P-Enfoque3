import nltk

# Definir la gramática causal definida para cadenas alimenticias
gramatica_causal = nltk.CFG.fromstring("""
    S -> Organismo 'come' Organismo
    Organismo -> 'hierba' | 'conejo' | 'zorro' | 'leon'
""")

# Ejemplo de cadena alimenticia
cadena_alimenticia = "El leon come al zorro."

# Crear un analizador sintáctico basado en la gramática causal
analizador_sintactico = nltk.ChartParser(gramatica_causal)

# Analizar sintácticamente la cadena alimenticia para identificar la relación causal
tokens = nltk.word_tokenize(cadena_alimenticia)
for arbol in analizador_sintactico.parse(tokens):
    print("Relacion causal identificada:")
    print(arbol)
