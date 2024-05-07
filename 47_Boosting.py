from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generar datos de ejemplo para regresión
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar modelo Gradient Boosting para regresión
modelo = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)

# Entrenar el modelo
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir valores en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Calcular error cuadrático medio del modelo
mse = mean_squared_error(y_prueba, predicciones)
print("Error Cuadratico Medio del modelo:", mse)
