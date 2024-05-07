class Evento:
    def __init__(self, nombre):
        self.nombre = nombre

class Accion:
    def __init__(self, nombre, participantes):
        self.nombre = nombre
        self.participantes = participantes

class Situacion:
    def __init__(self, nombre, eventos):
        self.nombre = nombre
        self.eventos = eventos

# Crear instancias de eventos
nacimiento = Evento("Nacimiento")
graduacion = Evento("Graduacion")
matrimonio = Evento("Matrimonio")

# Crear instancias de acciones
accion_nacimiento = Accion("Nacer", ["bebe", "madre", "padre"])
accion_graduacion = Accion("Graduarse", ["estudiante", "profesores"])
accion_matrimonio = Accion("Casarse", ["novio", "novia"])

# Crear instancias de situaciones
situacion1 = Situacion("Inicio de la vida", [nacimiento])
situacion2 = Situacion("Fin de la vida estudiantil", [graduacion])
situacion3 = Situacion("Union matrimonial", [matrimonio])

# Mostrar información
print("nSituacion:", situacion1.nombre)
print("Eventos en esta situacion:", [evento.nombre for evento in situacion1.eventos])

print("\nSituacion:", situacion2.nombre)
print("Eventos en esta situacion:", [evento.nombre for evento in situacion2.eventos])

print("\nSituacion:", situacion3.nombre)
print("Eventos en esta situacion:", [evento.nombre for evento in situacion3.eventos])
