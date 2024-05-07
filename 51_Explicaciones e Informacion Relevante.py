import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar datos de ejemplo sobre precios de casas
datos = pd.read_csv('precios_casas.csv')

# Separar características (X) y etiquetas (y)
X = datos[['tamaño', 'num_habitaciones']]
y = datos['precio']

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir precios de casas en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Calcular error cuadrático medio del modelo
mse = mean_squared_error(y_prueba, predicciones)
print("Error Cuadratico Medio del modelo:", mse)

# Explicar la predicción del precio de una casa específica
casa_nueva = [[2500, 4]]  # Características de la casa nueva
precio_predicho = modelo.predict(casa_nueva)
print("Precio Predicho:", precio_predicho)
print("Coeficientes del Modelo:")
print("Tamaño:", modelo.coef_[0])
print("Numero de Habitaciones:", modelo.coef_[1])
