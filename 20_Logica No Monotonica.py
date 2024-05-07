# Ejemplo de lógica circunstancial en Python

# Definir un conjunto de reglas y hechos
reglas = [
    ("feliz(X)", ["rico(X)"]),
    ("feliz(X)", ["casado(X)", "sano(X)"]),
    ("casado(juan)", []),
    ("sano(juan)", []),
    ("rico(pedro)", [])
]

# Verificar si una conclusión es válida según las reglas y los hechos
def verificar_conclusion(conclusion, reglas, hechos):
    for regla, condiciones in reglas:
        if conclusion == regla:
            for condicion in condiciones:
                if condicion not in hechos:
                    return False
            return True
    return False

# Ejemplo de uso de la lógica circunstancial
print("Ejemplo de lógica circunstancial:")
print("Juan es feliz?:", verificar_conclusion("feliz(juan)", reglas, ["casado(juan)", "sano(juan)"]))
print("Pedro es feliz?:", verificar_conclusion("feliz(pedro)", reglas, ["rico(pedro)"]))
