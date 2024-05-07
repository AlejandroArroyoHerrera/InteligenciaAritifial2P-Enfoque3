# Ejemplo de frase ambigua
frase_ambigua = "Vi a la mujer con el telescopio."

# Posibles interpretaciones de sentido
interpretaciones = [
    "Vi a la mujer usando el telescopio.",
    "Vi a la mujer a traves del telescopio."
]

# Imprimir las interpretaciones posibles
print("Frase Ambigua:", frase_ambigua)
print("Posibles Interpretaciones:")
for i, interpretacion in enumerate(interpretaciones, 1):
    print(f"Interpretacion {i}: {interpretacion}")
