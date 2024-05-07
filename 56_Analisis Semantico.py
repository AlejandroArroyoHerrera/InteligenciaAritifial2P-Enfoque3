# Función para realizar el análisis semántico de una sentencia de asignación
def analizar_asignacion(sentencia):
    tokens = sentencia.split()
    if len(tokens) == 3:
        variable, operador, valor = tokens
        if operador == '=':
            try:
                # Verificar si el valor asignado es un número
                int(valor)
                return True
            except ValueError:
                return False
    return False

# Ejemplo de sentencia en el lenguaje simple a analizar semánticamente
sentencia = "x = 10"

# Realizar el análisis semántico de la sentencia de asignación
if analizar_asignacion(sentencia):
    print("La sentencia de asignacion es semanticamente valida.")
else:
    print("La sentencia de asignacion no es semanticamente valida.")
