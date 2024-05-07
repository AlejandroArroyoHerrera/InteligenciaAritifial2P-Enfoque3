# Ejemplo de lógica temporal modal en Python

# Definir algunos momentos
momentos = ["t0", "t1", "t2"]

# Definir proposiciones en cada momento
proposiciones = {
    "t0": {"A": True, "B": False},
    "t1": {"A": True, "B": True},
    "t2": {"A": False, "B": True}
}

# Verificar el valor de una proposición en un momento dado
def valor_proposicion_momento(prop, momento, proposiciones):
    return proposiciones[momento][prop]

# Ejemplo de uso de la lógica temporal modal
print("Ejemplo de logica temporal modal:")
print("La proposición A es verdadera en t0?:", valor_proposicion_momento("A", "t0", proposiciones))
print("La proposición B es verdadera en t1?:", valor_proposicion_momento("B", "t1", proposiciones))
print("La proposición A es verdadera en t2?:", valor_proposicion_momento("A", "t2", proposiciones))
