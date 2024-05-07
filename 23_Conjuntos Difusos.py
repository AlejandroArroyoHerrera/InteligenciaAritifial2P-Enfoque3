import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definir el universo del conjunto difuso
x = np.arange(0, 11, 1)

# Definir funciones de membresía para conjuntos difusos
bajo = fuzz.trimf(x, [0, 0, 5])  # Bajo: Triangular con soporte [0, 5]
medio = fuzz.trimf(x, [0, 5, 10])  # Medio: Triangular con soporte [0, 10]
alto = fuzz.trimf(x, [5, 10, 10])  # Alto: Triangular con soporte [5, 10]

# Visualizar las funciones de membresía
plt.figure()
plt.plot(x, bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(x, medio, 'g', linewidth=1.5, label='Medio')
plt.plot(x, alto, 'r', linewidth=1.5, label='Alto')
plt.title('Funciones de membresía')
plt.ylabel('Grado de pertenencia')
plt.xlabel('Valor')
plt.legend()
plt.show()

# Realizar operaciones en conjuntos difusos
conjunto_difuso1 = bajo
conjunto_difuso2 = medio

# Operación de intersección (AND)
interseccion = np.fmin(conjunto_difuso1, conjunto_difuso2)

# Operación de unión (OR)
union = np.fmax(conjunto_difuso1, conjunto_difuso2)

# Visualizar las operaciones
plt.figure()
plt.plot(x, conjunto_difuso1, 'b', label='Conjunto Difuso 1')
plt.plot(x, conjunto_difuso2, 'g', label='Conjunto Difuso 2')
plt.plot(x, interseccion, 'r--', label='Interseccion (AND)')
plt.plot(x, union, 'm-.', label='Union (OR)')
plt.title('Operaciones en conjuntos difusos')
plt.ylabel('Grado de pertenencia')
plt.xlabel('Valor')
plt.legend()
plt.show()
