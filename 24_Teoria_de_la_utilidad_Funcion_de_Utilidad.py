#21110344  David López Rojas  6E2

class UtilityFunction:
    def __init__(self, weights):
        # Inicializa los pesos que se aplicarán a cada elemento de un resultado
        self.weights = weights

    def calculate_utility(self, outcome):
        # Calcula la utilidad como la suma ponderada de los elementos en outcome
        # multiplicando cada elemento por su peso correspondiente
        utility = sum(w * x for w, x in zip(self.weights, outcome))
        return utility

# Ejemplo de uso
weights = [0.5, 0.3, 0.2]  # Define los pesos para la utilidad
utility_function = UtilityFunction(weights)  # Crea una instancia de la función de utilidad

# Define dos outcomes con diferentes valores
outcome1 = [10, 20, 30]
outcome2 = [5, 25, 35]

# Calcula la utilidad de cada outcome
utility1 = utility_function.calculate_utility(outcome1)
utility2 = utility_function.calculate_utility(outcome2)

# Imprime las utilidades calculadas
print("Utilidad de Outcome 1:", utility1)
print("Utilidad de Outcome 2:", utility2)

# Compara las utilidades para determinar cuál outcome es preferido
if utility1 > utility2:
    print("Outcome 1 es preferido sobre Outcome 2")
elif utility1 < utility2:
    print("Outcome 2 es preferido sobre Outcome 1")
else:
    print("Los outcomes son igualmente preferidos")
