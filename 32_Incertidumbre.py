import random

# Definir probabilidades
probabilidad_lluvia = 0.6

# Simular si llueve o no
if random.random() < probabilidad_lluvia:
    print("¡Es probable que llueva!")
else:
    print("Es poco probable que llueva.")
