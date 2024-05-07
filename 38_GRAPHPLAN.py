from collections import defaultdict

class GraphPlan:
    def __init__(self, acciones, precondiciones, efectos):
        self.acciones = acciones
        self.precondiciones = precondiciones
        self.efectos = efectos

    def planificar(self, nivel):
        if nivel == 0:
            return [[]]

        plan_nivel_anterior = self.planificar(nivel - 1)
        nuevo_nivel = []

        for accion in self.acciones:
            for plan in plan_nivel_anterior:
                if all(precondicion in plan for precondicion in self.precondiciones[accion]):
                    nuevo_plan = plan + [accion]
                    if all(efecto in nuevo_plan for efecto in self.efectos[accion]):
                        nuevo_nivel.append(nuevo_plan)

        return nuevo_nivel

# Ejemplo de uso
acciones = ["A", "B", "C"]
precondiciones = {
    "A": [],
    "B": ["A"],
    "C": ["B"]
}
efectos = {
    "A": ["B"],
    "B": ["C"],
    "C": []
}

graph_planner = GraphPlan(acciones, precondiciones, efectos)
plan = graph_planner.planificar(3)
print("Plan generado por GRAPHPLAN:", plan)
