# Ejemplo de un sistema de recomendación de películas utilizando lógica de primer orden

# Base de conocimiento: Relación entre géneros de películas y preferencias del usuario
base_conocimiento = {
    "Juan": ["Accion", "Aventura", "Ciencia ficcion"],
    "María": ["Romance", "Comedia", "Drama"],
    "Pedro": ["Terror", "Suspenso", "Accion"]
}

# Función para recomendar películas basadas en las preferencias del usuario
def recomendar_peliculas(usuario):
    recomendaciones = []
    for pelicula in base_conocimiento[usuario]:
        recomendaciones.append(f"Te recomendamos ver {pelicula}.")

    return recomendaciones

# Usuario para el que queremos recomendar películas
usuario = "Juan"

# Obtener recomendaciones para el usuario
recomendaciones = recomendar_peliculas(usuario)

# Imprimir las recomendaciones
for recomendacion in recomendaciones:
    print(recomendacion)
