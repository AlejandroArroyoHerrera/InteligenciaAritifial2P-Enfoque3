class Creencia:
    def __init__(self, sujeto, objeto, verdad):
        self.sujeto = sujeto
        self.objeto = objeto
        self.verdad = verdad

# Crear instancias de creencias
creencia1 = Creencia("Juan", "El sol es una estrella", True)
creencia2 = Creencia("María", "Los gatos pueden volar", False)

# Mostrar información
print("Creencia de", creencia1.sujeto + ":", creencia1.objeto, "- Verdad?", creencia1.verdad)
print("Creencia de", creencia2.sujeto + ":", creencia2.objeto, "- Verdad?", creencia2.verdad)
