# Ejemplo de cuantificador universal en lógica de primer orden

# Supongamos que queremos verificar si todos los elementos en una lista son mayores que cero

def todos_mayores_que_cero(lista):
    # Cuantificador universal: para todo elemento x en la lista
    for elemento in lista:
        # Verificar si el elemento es mayor que cero
        if elemento <= 0:
            return False
    return True

# Lista de ejemplo
numeros = [1, 2, 3, 4, 5]

# Verificar si todos los elementos son mayores que cero
resultado = todos_mayores_que_cero(numeros)

if resultado:
    print("Todos los numeros en la lista son mayores que cero.")
else:
    print("Al menos un numero en la lista no es mayor que cero.")
