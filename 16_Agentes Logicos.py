# Ejemplo de un agente lógico para resolución de problemas utilizando lógica de primer orden

# Definir la base de conocimiento como una lista de cláusulas
base_conocimiento = [
    ("padre(juan, pedro)", True),
    ("padre(pedro, maria)", True),
    ("madre(maria, luisa)", True),
    ("hermano(X, Y) :- padre(Z, X), padre(Z, Y), X != Y", True)  # Regla para determinar hermanos
]

# Definir un agente lógico para resolución de problemas
class AgenteLogico:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def consultar(self, consulta):
        # Verificar si la consulta se cumple en la base de conocimiento
        for clausula, valor in self.base_conocimiento:
            if consulta == clausula:
                return valor
        return False

# Crear una instancia del agente lógico
agente = AgenteLogico(base_conocimiento)

# Consultar si dos personas son hermanos
hermano_de_luisa = agente.consultar("hermano(X, luisa)")
print("Luisa tiene un hermano?", hermano_de_luisa)
