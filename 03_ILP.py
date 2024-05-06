# Ejemplo de inferencia Modus Ponens en Python
def modus_ponens(premisa, implicacion):
    if premisa:
        if implicacion:
            return True
    return False

# Definir premisa y implicación
premisa = True
implicacion = False

# Realizar inferencia Modus Ponens
resultado = modus_ponens(premisa, implicacion)

# Imprimir resultado
if resultado:
    print("La implicacion es verdadera segun Modus Ponens.")
else:
    print("La implicacion no se puede validar segin Modus Ponens.")
