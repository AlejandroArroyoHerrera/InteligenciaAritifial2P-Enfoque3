import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Cargar datos de ejemplo sobre emisiones de CO2 de automóviles
datos = pd.read_csv('emisiones_co2_automoviles.csv')

# Separar características (X) y etiquetas (y)
X = datos[['cilindros', 'desplazamiento', 'consumo']]
y = datos['emisiones_co2']

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar modelo de árbol de regresión M5
modelo = DecisionTreeRegressor()
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir emisiones de CO2 en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Calcular error cuadrático medio del modelo
mse = mean_squared_error(y_prueba, predicciones)
print("Error Cuadratico Medio del modelo:", mse)
