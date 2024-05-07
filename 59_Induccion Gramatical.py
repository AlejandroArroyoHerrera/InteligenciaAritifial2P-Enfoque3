import random

# Definir una gramática simple para generar texto aleatorio
gramatica_texto = {
    'S': ['NP VP'],
    'NP': ['Articulo Sustantivo', 'Pronombre'],
    'VP': ['Verbo', 'Verbo NP'],
    'Articulo': ['el', 'la', 'los', 'las'],
    'Sustantivo': ['perro', 'gato', 'mesa', 'silla'],
    'Pronombre': ['él', 'ella', 'ellos', 'ellas'],
    'Verbo': ['corre', 'salta', 'come', 'duerme']
}

# Función para generar texto aleatorio utilizando inducción gramatical
def generar_texto(gramatica, simbolo_inicial, iteraciones):
    texto = simbolo_inicial
    for _ in range(iteraciones):
        nuevo_texto = ''
        for simbolo in texto.split():
            if simbolo in gramatica:
                nuevo_texto += random.choice(gramatica[simbolo]) + ' '
            else:
                nuevo_texto += simbolo + ' '
        texto = nuevo_texto.strip()
    return texto

# Generar texto aleatorio utilizando la gramática
texto_generado = generar_texto(gramatica_texto, 'S', 5)
print("Texto generado:", texto_generado)
