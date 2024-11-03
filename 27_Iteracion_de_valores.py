#21110344  David López Rojas  6E2

import numpy as np

class ValueIteration:
    def __init__(self, num_states, num_actions, transitions, rewards, gamma, epsilon=0.01):
        # Inicializa los parámetros del algoritmo de iteración de valores
        self.num_states = num_states  # Número de estados en el entorno
        self.num_actions = num_actions  # Número de acciones posibles
        self.transitions = transitions  # Matriz de transiciones que define las probabilidades de transición entre estados
        self.rewards = rewards  # Matriz de recompensas asociadas a cada acción en cada estado
        self.gamma = gamma  # Factor de descuento para futuras recompensas
        self.epsilon = epsilon  # Tolerancia para determinar la convergencia

    def value_iteration(self):
        V = np.zeros(self.num_states)  # Inicializa los valores de los estados a cero
        while True:
            delta = 0  # Inicializa la diferencia máxima entre valores
            for s in range(self.num_states):
                v = V[s]  # Guarda el valor anterior del estado actual
                # Calcular el valor esperado para cada acción en el estado actual
                q_values = [
                    sum(self.transitions[s][a][s_next] * (self.rewards[s][a][s_next] + self.gamma * V[s_next])
                        for s_next in range(self.num_states)) 
                    for a in range(self.num_actions)
                ]
                # Actualiza el valor del estado como el máximo valor esperado entre todas las acciones
                V[s] = max(q_values)
                # Actualiza la diferencia máxima entre los valores de los estados
                delta = max(delta, abs(v - V[s]))
            # Verifica si la convergencia se ha alcanzado
            if delta < self.epsilon:
                break  # Salir del bucle si la diferencia es menor que la tolerancia
        return V  # Retorna la función de valor óptima

# Definir los parámetros del entorno
num_states = 3  # Número de estados en el entorno
num_actions = 2  # Número de acciones posibles
transitions = {  # Definición de la matriz de transiciones
    0: {0: {0: 0.9, 1: 0.1}, 1: {0: 0.8, 1: 0.2}},
    1: {0: {0: 0.1, 1: 0.9}, 1: {0: 0.2, 1: 0.8}},
    2: {0: {0: 0.5, 1: 0.5}, 1: {0: 0.3, 1: 0.7}}
}
rewards = {  # Definición de la matriz de recompensas
    0: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    1: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    2: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}}
}
gamma = 0.9  # Factor de descuento para futuras recompensas
epsilon = 0.01  # Tolerancia para determinar la convergencia

# Inicializar la Iteración de Valores
value_iteration = ValueIteration(num_states, num_actions, transitions, rewards, gamma, epsilon)

# Realizar la Iteración de Valores para encontrar la función de valor óptima
optimal_values = value_iteration.value_iteration()

# Mostrar la función de valor óptima
print("Función de valor óptima:")
print(optimal_values)  # Imprime la función de valor óptima calculada
