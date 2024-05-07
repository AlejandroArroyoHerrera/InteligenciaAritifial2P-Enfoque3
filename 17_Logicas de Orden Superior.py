# Ejemplo de lógica temporal en Python

# Definir algunos estados del sistema
s0 = {"A": True, "B": False}
s1 = {"A": False, "B": True}
s2 = {"A": True, "B": True}

# Definir relaciones temporales entre estados
def antes(s1, s2):
    for proposicion, valor in s1.items():
        if valor and not s2[proposicion]:
            return False
    return True

def despues(s1, s2):
    return antes(s2, s1)

# Ejemplo de uso de la lógica temporal
print("Ejemplo de logica temporal:")
print("s0 antes de s1:", antes(s0, s1))
print("s1 antes de s0:", antes(s1, s0))
print("s0 después de s1:", despues(s0, s1))
print("s1 después de s0:", despues(s1, s0))
print("s1 antes de s2:", antes(s1, s2))
print("s2 después de s1:", despues(s2, s1))
