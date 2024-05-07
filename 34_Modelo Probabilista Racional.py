class ProbabilisticClassifier:
    def __init__(self):
        self.spam_probability = 0.5

    def train(self, emails):
        spam_count = sum(1 for email in emails if email["es_spam"])
        total_emails = len(emails)
        self.spam_probability = spam_count / total_emails

    def predict(self, email):
        probability_spam = self.spam_probability
        for word in email["contenido"].split():
            # Suponiendo independencia de palabras
            if word in self.spam_word_probabilities:
                probability_spam *= self.spam_word_probabilities[word]
        return probability_spam

# Ejemplo de uso
classifier = ProbabilisticClassifier()

# Entrenar el clasificador con ejemplos de correos
correos_entrenamiento = [
    {"contenido": "Oferta exclusiva. ¡Gana dinero rapido!", "es_spam": True},
    {"contenido": "Reunión del equipo el próximo jueves", "es_spam": False},
    {"contenido": "Prueba gratuita de nuestro producto", "es_spam": False}
]
classifier.train(correos_entrenamiento)

# Clasificar un nuevo correo
nuevo_correo = {"contenido": "¡Gana dinero facil con nuestra oferta especial!", "es_spam": None}
probabilidad_spam = classifier.predict(nuevo_correo)
print("Probabilidad de ser spam:", probabilidad_spam)
