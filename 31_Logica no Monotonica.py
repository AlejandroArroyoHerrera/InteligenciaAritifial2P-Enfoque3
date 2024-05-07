class MotorInferencia:
    def __init__(self):
        self.hechos = []

    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)

    def inferir(self, pregunta):
        for hecho in self.hechos:
            if pregunta in hecho:
                return True
        return False

# Crear un motor de inferencia
motor = MotorInferencia()

# Establecer hechos
motor.agregar_hecho(["Pajaros", "Pueden volar"])
motor.agregar_hecho(["Pajaros", "Tienen alas"])
motor.agregar_hecho(["Pingüinos", "Son Pajaros"])

# Consultar si los pingüinos pueden volar
resultado = motor.inferir(["Pingüinos", "Pueden volar"])

# Mostrar resultado
if resultado:
    print("Los pingüinos pueden volar (por defecto)")
else:
    print("Los pingüinos no pueden volar (por defecto)")
