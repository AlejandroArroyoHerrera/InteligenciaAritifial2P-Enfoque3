from skmultilearn.adapt import MLTSVM
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Cargar el conjunto de datos de diabetes
diabetes = load_diabetes()

# Separar características (X) y etiquetas (y)
X = diabetes.data
y = diabetes.target

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar modelo de Listas de Decisión K-DT
modelo = MLTSVM()

# Entrenar el modelo
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir valores en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Calcular error cuadrático medio del modelo
mse = mean_squared_error(y_prueba, predicciones)
print("Error Cuadratico Medio del modelo:", mse)
