# Supongamos que hemos cargado los datos de las casas en las variables X y y

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir precios de casas en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Calcular error cuadrático medio del modelo
mse = mean_squared_error(y_prueba, predicciones)
print("Error Cuadratico Medio del modelo:", mse)
