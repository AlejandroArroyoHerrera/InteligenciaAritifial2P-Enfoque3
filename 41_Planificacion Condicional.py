class ConditionalPlanning:
    def __init__(self, conditions, actions):
        self.conditions = conditions
        self.actions = actions

    def planificar(self, estado_actual):
        plan = []
        for condition, action in zip(self.conditions, self.actions):
            if condition(estado_actual):
                plan.append(action)
        return plan

# Ejemplo de uso
def condition1(estado):
    return estado["humedad_suelo"] < 50

def action1():
    return "Encender sistema de riego"

def condition2(estado):
    return estado["temperatura"] > 30

def action2():
    return "Aumentar frecuencia de riego"

conditions = [condition1, condition2]
actions = [action1, action2]

planner = ConditionalPlanning(conditions, actions)
estado_actual = {"humedad_suelo": 40, "temperatura": 32}
plan = planner.planificar(estado_actual)
print("Plan de accion:", plan)
