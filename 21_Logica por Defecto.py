# Ejemplo de lógica por defecto probabilística en Python

# Definir reglas y hechos
reglas = [
    ("feliz(X)", ["rico(X)"], 0.9),  # Regla por defecto con probabilidad 0.9: Si alguien es rico, es probable que sea feliz
    ("feliz(X)", ["casado(X)", "sano(X)"], 0.8),  # Regla por defecto con probabilidad 0.8: Si alguien está casado y sano, es probable que sea feliz
    ("casado(juan)", [], 1.0),  # Hecho: Juan está casado con probabilidad 1.0
    ("sano(juan)", [], 0.9),  # Hecho: Juan está sano con probabilidad 0.9
    ("rico(pedro)", [], 0.7)  # Hecho: Pedro es rico con probabilidad 0.7
]

# Función para verificar si una afirmación es válida según las reglas y hechos dados
def verificar_afirmacion_probabilistica(afirmacion, reglas, hechos):
    for regla, condiciones, probabilidad in reglas:
        if afirmacion == regla:
            probabilidad_cumplimiento = min([probabilidad] + [p for h, p in hechos if h in condiciones])
            return probabilidad_cumplimiento
    return None  # Si no se encuentra una regla que coincida con la afirmación, retornar None

# Ejemplo de uso de la lógica por defecto probabilística
print("Ejemplo de lógica por defecto probabilistica:")
print("Juan es feliz?:", verificar_afirmacion_probabilistica("feliz(juan)", reglas, [("casado(juan)", 1.0), ("sano(juan)", 0.9)]))
print("Pedro es feliz?:", verificar_afirmacion_probabilistica("feliz(pedro)", reglas, [("rico(pedro)", 0.7)]))
