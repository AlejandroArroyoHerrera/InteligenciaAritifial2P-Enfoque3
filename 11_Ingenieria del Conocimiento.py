# Ejemplo de un sistema de recomendaci�n de pel�culas utilizando l�gica de primer orden

# Base de conocimiento: Relaci�n entre g�neros de pel�culas y preferencias del usuario
base_conocimiento = {
    "Juan": ["Accion", "Aventura", "Ciencia ficcion"],
    "Mar�a": ["Romance", "Comedia", "Drama"],
    "Pedro": ["Terror", "Suspenso", "Accion"]
}

# Funci�n para recomendar pel�culas basadas en las preferencias del usuario
def recomendar_peliculas(usuario):
    recomendaciones = []
    for pelicula in base_conocimiento[usuario]:
        recomendaciones.append(f"Te recomendamos ver {pelicula}.")

    return recomendaciones

# Usuario para el que queremos recomendar pel�culas
usuario = "Juan"

# Obtener recomendaciones para el usuario
recomendaciones = recomendar_peliculas(usuario)

# Imprimir las recomendaciones
for recomendacion in recomendaciones:
    print(recomendacion)
