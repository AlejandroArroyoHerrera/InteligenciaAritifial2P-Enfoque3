import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar datos de ejemplo sobre compra de computadoras
datos = pd.read_csv('compra_computadoras.csv')

# Convertir variables categóricas en variables dummy
datos = pd.get_dummies(datos)

# Separar características (X) y etiquetas (y)
X = datos.drop('compra', axis=1)
y = datos['compra']

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar modelo de árbol de decisión ID3
modelo = DecisionTreeClassifier(criterion='entropy')
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir compra de computadoras en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Calcular precisión del modelo
precision = accuracy_score(y_prueba, predicciones)
print("Precision del modelo:", precision)
