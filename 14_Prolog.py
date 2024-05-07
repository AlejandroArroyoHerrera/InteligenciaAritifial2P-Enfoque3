# Ejemplo de programación lógica con Prolog en Python utilizando la biblioteca pyswip

from pyswip import Prolog

# Crear un nuevo motor Prolog
prolog = Prolog()

# Definir hechos y reglas en Prolog
prolog.assertz("padre(juan, maria)")
prolog.assertz("padre(pedro, juan)")
prolog.assertz("padre(pedro, carlos)")

# Consultar relaciones
for solucion in prolog.query("padre(X, Y)"):
    print("X es padre de Y:", solucion["X"], solucion["Y"])
