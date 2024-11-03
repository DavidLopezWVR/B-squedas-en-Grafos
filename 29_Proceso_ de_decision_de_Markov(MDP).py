#21110344  David López Rojas  6E2

import numpy as np

class MDP:
    def __init__(self, states, actions, transitions, rewards, gamma):
        # Inicializa el Proceso de Decisión de Markov (MDP) con sus estados, acciones, transiciones, recompensas y factor de descuento
        self.states = states  # Lista de estados del MDP
        self.actions = actions  # Lista de acciones posibles
        self.transitions = transitions  # Diccionario de transiciones que mapea estados y acciones a sus probabilidades de transición
        self.rewards = rewards  # Diccionario de recompensas que mapea estados y acciones a sus recompensas
        self.gamma = gamma  # Factor de descuento que determina la importancia de las recompensas futuras

    def value_iteration(self, epsilon=0.01):
        # Realiza la iteración de valores para encontrar la función de valor óptima
        num_states = len(self.states)  # Número de estados
        num_actions = len(self.actions)  # Número de acciones
        V = np.zeros(num_states)  # Inicializa la función de valor de los estados a cero
        while True:
            delta = 0  # Variable para rastrear el cambio máximo en la función de valor
            for s in range(num_states):
                v = V[s]  # Almacena el valor actual del estado
                # Calcula el valor esperado para el estado s bajo la mejor acción
                V[s] = max(sum(self.transitions[self.states[s]][self.actions[a]].get(self.states[s_next], 0) * 
                                (self.rewards[self.states[s]][self.actions[a]].get(self.states[s_next], 0) + 
                                 self.gamma * V[s_next]) 
                                for s_next in range(num_states)) 
                               for a in range(num_actions))
                delta = max(delta, abs(v - V[s]))  # Actualiza el cambio máximo
            if delta < epsilon:  # Verifica si la convergencia se ha alcanzado
                break
        return V  # Retorna la función de valor óptima

# Ejemplo de uso
states = ['S1', 'S2', 'S3']  # Define los estados del MDP
actions = ['A1', 'A2']  # Define las acciones posibles
# Define las transiciones de estado como un diccionario anidado
transitions = {
    'S1': {'A1': {'S1': 0.1, 'S2': 0.9}, 'A2': {'S2': 1}},  # Transiciones desde S1
    'S2': {'A1': {'S1': 0.8, 'S2': 0.2}, 'A2': {'S3': 1}},  # Transiciones desde S2
    'S3': {'A1': {'S1': 0, 'S2': 0}, 'A2': {'S1': 1}}   # Transiciones desde S3
}
# Define las recompensas como un diccionario anidado
rewards = {
    'S1': {'A1': {'S1': 0, 'S2': 0}, 'A2': {'S2': 1}},  # Recompensas en S1
    'S2': {'A1': {'S1': 0, 'S2': 0}, 'A2': {'S3': 10}},  # Recompensas en S2
    'S3': {'A1': {'S1': 0, 'S2': 0}, 'A2': {'S1': -1}}   # Recompensas en S3
}
gamma = 0.9  # Establece el factor de descuento

# Crea una instancia del MDP con los estados, acciones, transiciones, recompensas y gamma
mdp = MDP(states, actions, transitions, rewards, gamma)
V = mdp.value_iteration()  # Realiza la iteración de valores para obtener la función de valor
print("Función de valor:")  # Imprime la función de valor óptima
print(V)  # Muestra la función de valor en forma de array
