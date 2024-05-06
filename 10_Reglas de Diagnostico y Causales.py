# Ejemplo de regla de diagnóstico en lógica de primer orden

# Supongamos que queremos diagnosticar si un paciente tiene fiebre basándonos en dos síntomas: temperatura alta y dolor de cabeza.

def diagnosticar_fiebre(temperatura_alta, dolor_cabeza):
    # Regla de diagnóstico: Si el paciente tiene temperatura alta y dolor de cabeza, entonces se diagnostica fiebre.
    if temperatura_alta and dolor_cabeza:
        return "Fiebre"
    else:
        return "No hay fiebre"

# Síntomas del paciente
temperatura_alta = True
dolor_cabeza = True

# Diagnosticar si el paciente tiene fiebre
diagnostico = diagnosticar_fiebre(temperatura_alta, dolor_cabeza)
print("Diagnostico:", diagnostico)
