class STRIPSPlanner:
    def __init__(self, estado_inicial, estado_final, acciones):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.acciones = acciones

    def planificar(self):
        plan = []
        estado_actual = self.estado_inicial.copy()

        while estado_actual != self.estado_final:
            accion_seleccionada = None
            maximo_ajuste = -1

            for accion in self.acciones:
                precondiciones_satisfechas = all(estado_actual[p] for p in accion["precondiciones"])
                if precondiciones_satisfechas:
                    ajuste = sum(1 for p in accion["efectos"] if not estado_actual[p])
                    if ajuste > maximo_ajuste:
                        maximo_ajuste = ajuste
                        accion_seleccionada = accion

            if accion_seleccionada:
                plan.append(accion_seleccionada["nombre"])
                for efecto in accion_seleccionada["efectos"]:
                    estado_actual[efecto] = True
            else:
                return None  # No se puede alcanzar el estado final

        return plan

# Ejemplo de uso
estado_inicial = {"casa_limpia": False, "ropa_lavada": False}
estado_final = {"casa_limpia": True, "ropa_lavada": True}

acciones = [
    {"nombre": "Lavar ropa", "precondiciones": [], "efectos": ["ropa_lavada"]},
    {"nombre": "Limpiar casa", "precondiciones": [], "efectos": ["casa_limpia"]}
]

planner_strips = STRIPSPlanner(estado_inicial, estado_final, acciones)
plan = planner_strips.planificar()
print("Plan de accion:", plan)
