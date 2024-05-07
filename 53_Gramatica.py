import nltk

# Definir gramática libre de contexto para oraciones simples en inglés
gramatica_oraciones = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'a' | 'an' | 'the'
    N -> 'cat' | 'dog' | 'house'
    V -> 'chased' | 'ate' | 'slept'
    P -> 'in' | 'on' | 'by'
""")

# Crear un analizador sintáctico basado en la gramática
analizador_sintactico = nltk.ChartParser(gramatica_oraciones)

# Oraciones para análisis
oraciones = [
    "the cat chased the dog",
    "a dog slept in the house",
    "the house by the river",
    "an cat ate on the table"
]

# Analizar cada oración utilizando el analizador sintáctico
for oracion in oraciones:
    tokens = nltk.word_tokenize(oracion)
    arbol = list(analizador_sintactico.parse(tokens))
    if arbol:
        print("Oracion:", oracion)
        print("Analisis Sintactico:")
        print(arbol[0])
    else:
        print("La oracion", oracion, "no se puede analizar sintacticamente.")
