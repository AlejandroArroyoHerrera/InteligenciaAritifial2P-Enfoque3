class MotorInferencia:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, antecedente, consecuente):
        self.reglas.append((antecedente, consecuente))

    def inferir(self, hechos):
        for antecedente, consecuente in self.reglas:
            if all(item in hechos for item in antecedente):
                return consecuente
        return None

# Crear un motor de inferencia basado en reglas
motor_experto = MotorInferencia()

# Definir reglas
motor_experto.agregar_regla(["Tiene fiebre"], "Podría tener gripe")
motor_experto.agregar_regla(["Tiene tos"], "Podría tener resfriado")

# Consultar al sistema experto
sintomas = ["Tiene fiebre", "Tiene tos"]
diagnostico = motor_experto.inferir(sintomas)

# Mostrar resultado
if diagnostico:
    print("El diagnostico es:", diagnostico)
else:
    print("No se puede determinar el diagnostico.")
