# Ejemplo de regla de diagn�stico en l�gica de primer orden

# Supongamos que queremos diagnosticar si un paciente tiene fiebre bas�ndonos en dos s�ntomas: temperatura alta y dolor de cabeza.

def diagnosticar_fiebre(temperatura_alta, dolor_cabeza):
    # Regla de diagn�stico: Si el paciente tiene temperatura alta y dolor de cabeza, entonces se diagnostica fiebre.
    if temperatura_alta and dolor_cabeza:
        return "Fiebre"
    else:
        return "No hay fiebre"

# S�ntomas del paciente
temperatura_alta = True
dolor_cabeza = True

# Diagnosticar si el paciente tiene fiebre
diagnostico = diagnosticar_fiebre(temperatura_alta, dolor_cabeza)
print("Diagnostico:", diagnostico)
