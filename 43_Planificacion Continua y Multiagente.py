class NegotiationAgent:
    def __init__(self, id, utility_function):
        self.id = id
        self.utility_function = utility_function

    def negotiate(self, other_agent, initial_offer):
        offer = initial_offer
        other_offer = initial_offer
        for _ in range(3):  # Número arbitrario de rondas de negociación
            my_utility = self.utility_function(offer)
            other_utility = other_agent.utility_function(other_offer)
            if my_utility >= other_utility:
                return offer
            else:
                offer = other_offer
                other_offer = self.generate_counter_offer()

    def generate_counter_offer(self):
        # Aquí se puede implementar la lógica para generar una contraoferta
        return "Contraoferta"

# Ejemplo de uso
def utility_function(offer):
    # Función de utilidad arbitraria
    return len(offer)

agent1 = NegotiationAgent(id=1, utility_function=utility_function)
agent2 = NegotiationAgent(id=2, utility_function=utility_function)

initial_offer = "Oferta inicial"

final_offer_agent1 = agent1.negotiate(agent2, initial_offer)
final_offer_agent2 = agent2.negotiate(agent1, initial_offer)

print("Oferta final del agente 1:", final_offer_agent1)
print("Oferta final del agente 2:", final_offer_agent2)
