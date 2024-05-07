# Ejemplo de lógica modal deóntica en Python

# Definir algunos agentes
agentes = ["Agente1", "Agente2"]

# Definir algunas acciones
acciones = ["P", "Q", "R"]

# Inicializar el modelo de Kripke
modelo_kripke = {
    "Agente1": {
        "P": True,
        "Q": False,
        "R": True
    },
    "Agente2": {
        "P": False,
        "Q": True,
        "R": False
    }
}

# Verificar si una acción es permitida para un agente en un modelo de Kripke
def accion_permitida(agente, accion, modelo):
    return modelo[agente][accion]

# Ejemplo de uso de la lógica modal deóntica
print("Ejemplo de logica modal deontica:")
for agente in agentes:
    for accion in acciones:
        print(f"{accion} es permitida para {agente}?: {accion_permitida(agente, accion, modelo_kripke)}")
