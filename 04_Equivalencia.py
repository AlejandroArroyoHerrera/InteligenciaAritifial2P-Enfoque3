# Ejemplo de equivalencia de expresiones l�gicas en Python
def equivalencia(expresion1, expresion2):
    # Verificar si ambas expresiones son equivalentes
    return expresion1 == expresion2

# Expresiones l�gicas
expresion1 = "(p and q) or r"
expresion2 = "p or (q and r)"

# Verificar equivalencia
if equivalencia(expresion1, expresion2):
    print("Las expresiones son equivalentes.")
else:
    print("Las expresiones no son equivalentes.")
