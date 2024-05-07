# Ejemplo de encadenamiento hacia adelante en lógica de primer orden

# Base de conocimiento: Reglas de inferencia
base_conocimiento = {
    "Regla1": (("P",), ("Q",)),
    "Regla2": (("Q",), ("R",))
}

# Hechos iniciales
hechos = {"P": True}

# Función para realizar encadenamiento hacia adelante
def encadenamiento_hacia_adelante(hechos, base_conocimiento):
    nuevos_hechos = hechos.copy()
    while True:
        algo_cambio = False
        for regla, (premisas, conclusion) in base_conocimiento.items():
            if all(premisa in hechos for premisa in premisas) and conclusion[0] not in hechos:
                nuevos_hechos[conclusion[0]] = True
                algo_cambio = True
        if not algo_cambio:
            break
    return nuevos_hechos

# Realizar encadenamiento hacia adelante
nuevos_hechos = encadenamiento_hacia_adelante(hechos, base_conocimiento)

# Imprimir los nuevos hechos derivados
print("Nuevos hechos derivados:")
for hecho, valor in nuevos_hechos.items():
    print(hecho, "=", valor)
