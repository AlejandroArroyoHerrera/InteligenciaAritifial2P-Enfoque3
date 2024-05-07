# Importar librerías necesarias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Cargar conjunto de datos de flores Iris
iris = load_iris()

# Separar características (X) y etiquetas (y)
X = iris.data
y = iris.target

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar modelo de vecinos más cercanos
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir clases de flores en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Evaluar precisión del modelo
precision = modelo.score(X_prueba, y_prueba)
print("Precision del modelo:", precision)
