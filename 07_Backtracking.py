# Ejemplo de backtracking para resolver problemas de satisfacibilidad (SAT) en Python
def backtracking_sat(expresion, asignacion):
    if len(asignacion) == len(variables):
        return eval(expresion, asignacion)

    variable = variables[len(asignacion)]
    asignacion[variable] = True
    if backtracking_sat(expresion, asignacion):
        return True

    asignacion[variable] = False
    if backtracking_sat(expresion, asignacion):
        return True

    del asignacion[variable]
    return False

# Expresión lógica en forma de cadena
expresion = "p or (q and r)"

# Lista de variables en la expresión
variables = ["p", "q", "r"]

# Realizar backtracking para satisfacibilidad (SAT)
asignacion = {}
if backtracking_sat(expresion, asignacion):
    print("La expresion es satisfacible.")
    print("Asignacion de variables:", asignacion)
else:
    print("La expresion no es satisfacible.")
