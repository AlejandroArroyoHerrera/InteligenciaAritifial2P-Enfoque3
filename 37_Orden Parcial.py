class PartialOrderPlanner:
    def __init__(self, acciones, dependencias):
        self.acciones = acciones
        self.dependencias = dependencias

    def planificar(self):
        orden = []
        while self.acciones:
            action_with_no_dependencies = [action for action in self.acciones if action not in self.dependencias.values()]
            if not action_with_no_dependencies:
                return None  # No se puede planificar debido a dependencias cíclicas
            for action in action_with_no_dependencies:
                orden.append(action)
                self.acciones.remove(action)
                self.dependencias = {k: v for k, v in self.dependencias.items() if v != action}
        return orden

# Ejemplo de uso
acciones = ["A", "B", "C", "D", "E"]
dependencias = {
    "B": "A",
    "C": "A",
    "D": "B",
    "E": "C"
}

planner = PartialOrderPlanner(acciones, dependencias)
plan = planner.planificar()
print("Plan de Orden Parcial:", plan)
