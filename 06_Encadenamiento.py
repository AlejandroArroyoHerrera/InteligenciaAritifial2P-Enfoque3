# Ejemplo de encadenamiento hacia adelante (Forward Chaining) en Python
def forward_chaining(base_conocimiento, hechos_iniciales, objetivo):
    hechos = set(hechos_iniciales)

    while True:
        nuevo_hecho_agregado = False

        for regla in base_conocimiento:
            antecedente, consecuente = regla

            if all(premisa in hechos for premisa in antecedente) and consecuente not in hechos:
                hechos.add(consecuente)
                nuevo_hecho_agregado = True

                if objetivo in hechos:
                    return True, hechos

        if not nuevo_hecho_agregado:
            return False, hechos

# Base de conocimiento: [([antecedentes], consecuente)]
base_conocimiento = [
    (["p", "q"], "r"),
    (["r"], "s"),
    (["s"], "t")
]

# Hechos iniciales y objetivo
hechos_iniciales = ["p", "q"]
objetivo = "t"

# Realizar encadenamiento hacia adelante
resultado, hechos = forward_chaining(base_conocimiento, hechos_iniciales, objetivo)

# Imprimir resultado y hechos obtenidos
if resultado:
    print("El objetivo se puede alcanzar.")
    print("Hechos obtenidos:", hechos)
else:
    print("El objetivo no se puede alcanzar.")
