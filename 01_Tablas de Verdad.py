# Ejemplo de evaluaci�n de una expresi�n l�gica con tabla de verdad en Python
def evaluar_expresion(expresion, variables):
    # Construir todas las combinaciones posibles de valores para las variables
    combinaciones = []
    for i in range(2 ** len(variables)):
        combinacion = []
        for j in range(len(variables)):
            combinacion.append((i // (2 ** j)) % 2)
        combinaciones.append(combinacion)

    # Evaluar la expresi�n para cada combinaci�n de valores
    resultados = []
    for combinacion in combinaciones:
        valores = dict(zip(variables, combinacion))
        resultado = eval(expresion, valores)
        resultados.append(resultado)

    return resultados

# Expresi�n l�gica y variables
expresion = "(p and q) or (not p)"
variables = ["p", "q"]

# Evaluar la expresi�n con tabla de verdad
resultados = evaluar_expresion(expresion, variables)

# Imprimir tabla de verdad
print("Tabla de Verdad:")
for i, combinacion in enumerate(combinaciones):
    print(f"{combinacion} -> {resultados[i]}")
