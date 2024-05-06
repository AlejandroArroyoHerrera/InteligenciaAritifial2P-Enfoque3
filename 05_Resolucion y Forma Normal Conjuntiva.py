# Ejemplo de resoluci�n de cl�usulas en Python
def resolucion(clausula1, clausula2):
    # Combinar cl�usulas sin duplicados
    nueva_clausula = set(clausula1) | set(clausula2)

    # Eliminar literales y sus negaciones opuestas
    for literal in nueva_clausula:
        if ("not " + literal) in nueva_clausula:
            return nueva_clausula - {literal, "not " + literal}

    return nueva_clausula

# Clausulas
clausula1 = {"p", "q"}
clausula2 = {"not p", "r"}

# Aplicar resoluci�n
resultado = resolucion(clausula1, clausula2)

# Imprimir resultado
print("Resultado de la resolucion:", resultado)
