# Ejemplo de resolución Skolem con una cláusula existencial en lógica de primer orden

# Supongamos la cláusula existencial: ∃x P(x) → Q(x)
# Queremos demostrar Q(a), donde 'a' es una constante introducida por Skolemización

# Definir la cláusula existencial
clausula_existencial = {'P(x)': True, 'Q(x)': True}

# Skolemización: Introducir una constante 'a'
constante_skolem = 'a'
clausula_skolemizada = {'Q(a)': True}

# Verificar si la cláusula skolemizada implica la conclusión
def resolucion_skolem(clausula_existencial, clausula_skolemizada):
    for literal in clausula_existencial:
        if literal in clausula_skolemizada and clausula_existencial[literal] != clausula_skolemizada[literal]:
            return True  # La resolución es exitosa
    return False  # No se puede inferir la conclusión

# Realizar la resolución Skolem
resultado = resolucion_skolem(clausula_existencial, clausula_skolemizada)

# Imprimir el resultado
if resultado:
    print("La conclusion Q(a) se puede inferir utilizando resolucion Skolem.")
else:
    print("La conclusion Q(a) no se puede inferir utilizando resolucion Skolem.")
