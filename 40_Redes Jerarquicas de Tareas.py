class Tarea:
    def __init__(self, nombre, duracion, subtasks=None):
        self.nombre = nombre
        self.duracion = duracion
        self.subtasks = subtasks if subtasks is not None else []

    def agregar_subtarea(self, subtarea):
        self.subtasks.append(subtarea)

    def obtener_duracion_total(self):
        duracion_total = self.duracion
        for subtarea in self.subtasks:
            duracion_total += subtarea.obtener_duracion_total()
        return duracion_total

# Crear las tareas del proyecto
tarea_principal = Tarea("Desarrollo de Software", 10)
disenio = Tarea("Diseño", 5)
implementacion = Tarea("Implementación", 8)
pruebas = Tarea("Pruebas", 3)
revision = Tarea("Revision de Codigo", 2)

# Construir la jerarquía de tareas
tarea_principal.agregar_subtarea(disenio)
tarea_principal.agregar_subtarea(implementacion)
tarea_principal.agregar_subtarea(pruebas)
implementacion.agregar_subtarea(revision)

# Obtener la duración total del proyecto
duracion_total_proyecto = tarea_principal.obtener_duracion_total()
print("Duracion total del proyecto:", duracion_total_proyecto, "dias")
