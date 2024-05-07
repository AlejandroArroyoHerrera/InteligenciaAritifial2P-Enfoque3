class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Mamifero(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

class Ave(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

class Perro(Mamifero):
    def __init__(self, nombre):
        super().__init__(nombre)

class Gato(Mamifero):
    def __init__(self, nombre):
        super().__init__(nombre)

class Pajaro(Ave):
    def __init__(self, nombre):
        super().__init__(nombre)

# Crear instancias
mi_perro = Perro("Fido")
mi_gato = Gato("Garfield")
mi_pajaro = Pajaro("Piolin")

# Mostrar información
print("Mi perro se llama", mi_perro.nombre)
print("Mi gato se llama", mi_gato.nombre)
print("Mi pájaro se llama", mi_pajaro.nombre)
