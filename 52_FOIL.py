# Definir datos de ejemplo: ejemplos de aprendizaje
datos_aprendizaje = [
    {"edad": "joven", "ingresos": "bajos", "trabajo": "no", "compra": "no"},
    {"edad": "joven", "ingresos": "bajos", "trabajo": "si", "compra": "no"},
    {"edad": "joven", "ingresos": "altos", "trabajo": "no", "compra": "si"},
    {"edad": "joven", "ingresos": "altos", "trabajo": "si", "compra": "si"},
]

# Generar reglas de FOIL para clasificar ejemplos de aprendizaje
regla_foil_aprendizaje = foil(datos_aprendizaje)
print("Regla de FOIL para Aprendizaje:", regla_foil_aprendizaje)
