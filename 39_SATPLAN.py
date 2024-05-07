from pysat.solvers import Glucose3

class SATPlan:
    def __init__(self, acciones, precondiciones, efectos):
        self.acciones = acciones
        self.precondiciones = precondiciones
        self.efectos = efectos

    def planificar(self):
        solver = Glucose3()

        variables = {}
        actions = {}
        for i, action in enumerate(self.acciones):
            variables[action] = i + 1
            actions[i + 1] = action

        for accion in self.acciones:
            for precondicion in self.precondiciones[accion]:
                solver.add_clause([-variables[accion], variables[precondicion]])
            for efecto in self.efectos[accion]:
                solver.add_clause([-variables[accion], variables[efecto]])

        result = solver.solve()
        if result:
            model = solver.get_model()
            plan = [actions[literal] for literal in model if literal > 0]
            return plan
        else:
            return None

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

sat_planner = SATPlan(acciones, precondiciones, efectos)
plan = sat_planner.planificar()
print("Plan generado por SATPLAN:", plan)
