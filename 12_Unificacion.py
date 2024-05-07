# Ejemplo de unificaci�n de t�rminos en l�gica de primer orden

def unificar(termino1, termino2):
    # Verificar si los t�rminos son iguales
    if termino1 == termino2:
        return True, {}

    # Verificar si uno de los t�rminos es una variable
    if es_variable(termino1):
        return True, {termino1: termino2}
    elif es_variable(termino2):
        return True, {termino2: termino1}

    # Verificar si los t�rminos tienen la misma funci�n y misma cantidad de argumentos
    if es_funcion(termino1) and es_funcion(termino2) and len(termino1) == len(termino2):
        # Unificar los argumentos recursivamente
        unificacion = {}
        for arg1, arg2 in zip(termino1, termino2):
            unificacion_exitosa, sustitucion = unificar(arg1, arg2)
            if not unificacion_exitosa:
                return False, {}
            unificacion.update(sustitucion)
        return True, unificacion

    # Si no se cumple ninguna condici�n, los t�rminos no se pueden unificar
    return False, {}

def es_variable(termino):
    # Verificar si el t�rmino es una variable
    return isinstance(termino, str) and termino.islower()

def es_funcion(termino):
    # Verificar si el t�rmino es una funci�n (lista)
    return isinstance(termino, list)

# Ejemplo de unificaci�n de t�rminos
termino1 = ['f', 'x', 'y']
termino2 = ['f', 'a', 'b']

resultado, sustitucion = unificar(termino1, termino2)
print("Unificacion exitosa:", resultado)
if resultado:
    print("Sustitucion:", sustitucion)
