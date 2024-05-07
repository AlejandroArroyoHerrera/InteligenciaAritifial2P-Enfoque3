class ProductionSystem:
    def __init__(self, acciones, precondiciones, efectos):
        self.acciones = acciones
        self.precondiciones = precondiciones
        self.efectos = efectos

    def ejecutar_accion(self, accion, estado_actual):
        print(f"Ejecutando accion: {accion}")
        for efecto in self.efectos[accion]:
            estado_actual[efecto] = True

    def verificar_estado(self, estado_actual):
        for accion in self.acciones:
            if all(precondicion in estado_actual for precondicion in self.precondiciones[accion]):
                return accion
        return None

# Ejemplo de uso
acciones = ["Producir", "Detener_produccion"]
precondiciones = {
    "Producir": ["Recursos_suficientes"],
    "Detener_produccion": ["Recursos_insuficientes"]
}
efectos = {
    "Producir": ["Producto_producido"],
    "Detener_produccion": ["Produccion_detenida"]
}

production_system = ProductionSystem(acciones, precondiciones, efectos)
estado_actual = {"Recursos_suficientes": True}

# Ejecutar acciones hasta que se cumpla una condición deseada
while True:
    accion_a_ejecutar = production_system.verificar_estado(estado_actual)
    if accion_a_ejecutar is None:
        print("No hay acciones disponibles para el estado actual. Replanificando...")
        # Aquí se puede implementar la replanificación
        break
    else:
        production_system.ejecutar_accion(accion_a_ejecutar, estado_actual)
        print("Estado actual:", estado_actual)
