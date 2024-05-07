from pyclips import Environment

# Crear un nuevo entorno CLIPS
env = Environment()

# Cargar la extensión Fuzzy CLIPS
env.load("fuzzy.clp")

# Resetear el entorno
env.reset()

# Definir los hechos de entrada (temperatura) y salida (velocidad del ventilador)
env.assert_string("(temperatura 75)")
env.assert_string("(velocidad-ventilador)")

# Ejecutar el sistema de inferencia
env.run()

# Obtener el valor de la velocidad del ventilador resultante
velocidad = env.find_template("velocidad-ventilador").slot_value("value").float_value

print("Velocidad del ventilador:", velocidad)
