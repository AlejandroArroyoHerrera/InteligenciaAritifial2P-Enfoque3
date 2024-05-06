# Ejemplo de base de conocimiento para inferencia lógica en Python
class BaseConocimiento:
    def __init__(self):
        self.hechos = set()
        self.reglas = []

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_regla(self, antecedente, consecuente):
        self.reglas.append((antecedente, consecuente))

    def inferir(self, objetivo):
        inferido = False
        for regla in self.reglas:
            antecedente, consecuente = regla
            if all(h in self.hechos for h in antecedente):
                self.hechos.add(consecuente)
                inferido = True
                if consecuente == objetivo:
                    return True
        return inferido

# Crear una base de conocimiento
base = BaseConocimiento()

# Agregar hechos a la base de conocimiento
base.agregar_hecho("p")
base.agregar_hecho("q")

# Agregar reglas a la base de conocimiento
base.agregar_regla({"p"}, "r")
base.agregar_regla({"q"}, "s")

# Realizar inferencias en la base de conocimiento
objetivo = "s"
resultado = base.inferir(objetivo)

# Imprimir resultado de la inferencia
if resultado:
    print(f"Se puede inferir {objetivo} a partir de la base de conocimiento.")
else:
    print(f"No se puede inferir {objetivo} a partir de la base de conocimiento.")
