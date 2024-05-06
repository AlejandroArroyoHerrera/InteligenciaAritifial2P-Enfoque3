import random
import math

# Función objetivo: número de cláusulas satisfechas
def funcion_objetivo(asignacion, clausulas):
    satisfaccion = 0
    for clausula in clausulas:
        if any(asignacion[literal] for literal in clausula):
            satisfaccion += 1
    return satisfaccion

# Algoritmo de recocido simulado
def simulated_annealing(clausulas, temperatura_inicial, enfriamiento, asignacion_inicial):
    asignacion_actual = asignacion_inicial
    temperatura_actual = temperatura_inicial

    while temperatura_actual > 0:
        vecino = dict(asignacion_actual)
        # Generar vecino cambiando el valor de una variable aleatoria
        variable_aleatoria = random.choice(list(asignacion_actual.keys()))
        vecino[variable_aleatoria] = not vecino[variable_aleatoria]
        
        diferencia = funcion_objetivo(vecino, clausulas) - funcion_objetivo(asignacion_actual, clausulas)
        if diferencia > 0 or random.random() < math.exp(diferencia / temperatura_actual):
            asignacion_actual = vecino

        temperatura_actual -= enfriamiento

    return asignacion_actual

# Clausulas del problema
clausulas = [
    {"p", "q"},
    {"not p", "r"},
    {"not r", "q"}
]

# Parámetros del algoritmo
temperatura_inicial = 100
enfriamiento = 0.1
asignacion_inicial = {"p": False, "q": False, "r": False}

# Ejecutar algoritmo de recocido simulado
solucion = simulated_annealing(clausulas, temperatura_inicial, enfriamiento, asignacion_inicial)
print("Asignacion optima encontrada:", solucion)
