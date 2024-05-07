from pyDatalog import pyDatalog

# Definir hechos
pyDatalog.create_terms('padre, abuelo, X, Y, Z')

# Definir reglas
+padre('Juan', 'Pedro')
+padre('Pedro', 'Sofía')
+padre('Pedro', 'Luis')

abuelo(X, Y) <= padre(X, Z) & padre(Z, Y)

# Consultar la base de conocimientos
print("Abuelos:")
print(abuelo(X, Y))
