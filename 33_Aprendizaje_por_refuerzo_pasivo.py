#21110344  David López Rojas  6E2

import numpy as np  # Importar la biblioteca NumPy para operaciones numéricas

class PassiveRL:
    def __init__(self, num_states, num_actions, transitions, rewards, gamma, epsilon=0.01):
        # Inicializar el entorno de aprendizaje por refuerzo pasivo
        self.num_states = num_states  # Número de estados en el entorno
        self.num_actions = num_actions  # Número de acciones disponibles
        self.transitions = transitions  # Función de transición del estado (probabilidades de transición)
        self.rewards = rewards  # Función de recompensas
        self.gamma = gamma  # Factor de descuento
        self.epsilon = epsilon  # Umbral de convergencia para la iteración de valores

    def value_iteration(self):
        # Método para realizar la iteración de valores
        V = np.zeros(self.num_states)  # Inicializar la función de valor de cada estado a cero
        while True:  # Bucle para iterar hasta la convergencia
            delta = 0  # Inicializar la diferencia máxima
            for s in range(self.num_states):  # Iterar sobre cada estado
                v = V[s]  # Almacenar el valor actual del estado
                # Calcular el valor esperado para cada acción en el estado actual
                V[s] = max(sum(self.transitions[s][a][s_next] * (self.rewards[s][a][s_next] + self.gamma * V[s_next])
                              for s_next in range(self.num_states)) for a in range(self.num_actions))
                # Actualizar la diferencia máxima entre los valores de los estados
                delta = max(delta, abs(v - V[s]))
            # Verificar si la convergencia se ha alcanzado
            if delta < self.epsilon:
                break  # Salir del bucle si la diferencia es menor que epsilon
        return V  # Devolver la función de valor óptima

# Definir los parámetros del entorno
num_states = 3  # Número de estados
num_actions = 2  # Número de acciones
transitions = {  # Función de transición: probabilidad de moverse de un estado a otro
    0: {0: {0: 0.9, 1: 0.1}, 1: {0: 0.8, 1: 0.2}},
    1: {0: {0: 0.6, 1: 0.4}, 1: {0: 0.3, 1: 0.7}},
    2: {0: {0: 0.5, 1: 0.5}, 1: {0: 0.1, 1: 0.9}}
}
rewards = {  # Función de recompensa: recompensa recibida por cada acción en cada estado
    0: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    1: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    2: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}}
}
gamma = 0.9  # Factor de descuento

# Inicializar el aprendizaje por refuerzo pasivo
passive_rl = PassiveRL(num_states, num_actions, transitions, rewards, gamma)

# Realizar la iteración de valor para encontrar la función de valor óptima
optimal_values = passive_rl.value_iteration()
print("Función de valor óptima:", optimal_values)  # Imprimir la función de valor óptima

