#21110344  David López Rojas  6E2

class ValueOfInformation:
    def __init__(self, utility_function):
        # Inicializa la clase con una función de utilidad proporcionada
        self.utility_function = utility_function

    def value_of_information(self, prior_prob, posterior_probs):
        # Calcula el valor de la información utilizando probabilidades a priori y posteriores
        # Calcula la utilidad de la probabilidad a priori
        prior_utility = self.utility_function.calculate_utility(prior_prob)
        # Calcula la utilidad esperada de las probabilidades posteriores
        expected_utility = sum(prob * self.utility_function.calculate_utility(post_prob) for prob, post_prob in zip(prior_prob, posterior_probs))
        # Retorna la diferencia entre la utilidad esperada y la utilidad a priori
        return expected_utility - prior_utility

class UtilityFunction:
    def __init__(self, weights):
        # Inicializa la función de utilidad con pesos asignados a cada resultado
        self.weights = weights

    def calculate_utility(self, outcome):
        # Calcula la utilidad como la suma ponderada de los elementos en el resultado
        utility = sum(w * x for w, x in zip(self.weights, outcome))
        return utility

# Ejemplo de uso
prior_prob = [0.4, 0.6]  # Probabilidades a priori de los resultados (por ejemplo, eventos posibles)
posterior_probs = [[0.7, 0.3], [0.2, 0.8]]  # Probabilidades posteriores asociadas a cada resultado
weights = [1, 2]  # Pesos asignados para calcular la utilidad

# Crea una instancia de la función de utilidad con los pesos especificados
utility_function = UtilityFunction(weights)
# Crea una instancia de la clase ValueOfInformation con la función de utilidad
voi_calculator = ValueOfInformation(utility_function)

# Calcula el valor de la información utilizando las probabilidades a priori y posteriores
voi = voi_calculator.value_of_information(prior_prob, posterior_probs)
# Imprime el valor de la información calculado
print("Valor de la información:", voi)
