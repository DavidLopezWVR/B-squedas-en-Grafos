#21110344  David López Rojas  6E2

import numpy as np  # Importar la biblioteca NumPy para operaciones numéricas

class PolicySearch:
    def __init__(self, num_states, num_actions, transitions, rewards, gamma):
        # Inicializar el objeto con los parámetros del entorno
        self.num_states = num_states  # Número de estados en el entorno
        self.num_actions = num_actions  # Número de acciones disponibles
        self.transitions = transitions  # Matriz de transiciones del estado
        self.rewards = rewards  # Matriz de recompensas
        self.gamma = gamma  # Factor de descuento
        # Inicializar una política aleatoria uniforme
        self.policy = np.ones((num_states, num_actions)) / num_actions

    def evaluate_policy(self):
        # Evaluación de la política actual
        V = np.zeros(self.num_states)  # Inicializar el vector de valores de estado
        for _ in range(1000):  # Iteraciones para evaluar la política
            for s in range(self.num_states):  # Para cada estado
                v = 0  # Valor acumulado para el estado s
                for a in range(self.num_actions):  # Para cada acción
                    # Calcular el valor esperado de la acción a en el estado s
                    v += self.policy[s][a] * sum(self.transitions[s][a][s_next] * (self.rewards[s][a][s_next] + self.gamma * V[s_next])
                                                 for s_next in range(self.num_states))
                V[s] = v  # Actualizar el valor del estado s
        return V  # Devolver los valores de estado evaluados

    def improve_policy(self, V):
        # Mejora de la política basada en los valores de estado-acción
        for s in range(self.num_states):  # Para cada estado
            q_values = np.zeros(self.num_actions)  # Inicializar los valores Q para el estado s
            for a in range(self.num_actions):  # Para cada acción
                # Calcular el valor Q para la acción a en el estado s
                q_values[a] = sum(self.transitions[s][a][s_next] * (self.rewards[s][a][s_next] + self.gamma * V[s_next])
                                  for s_next in range(self.num_states))
            best_action = np.argmax(q_values)  # Encontrar la acción con el mejor valor Q
            self.policy[s] = np.eye(self.num_actions)[best_action]  # Actualizar la política para el estado s

    def train(self):
        # Búsqueda de la política iterativa
        for _ in range(100):  # Número de iteraciones de mejora de política
            V = self.evaluate_policy()  # Evaluar la política actual
            self.improve_policy(V)  # Mejorar la política con los valores evaluados

# Definir los parámetros del entorno
num_states = 3  # Definir el número de estados
num_actions = 2  # Definir el número de acciones
transitions = {  # Definir la matriz de transiciones de estado
    0: {0: {0: 0.9, 1: 0.1}, 1: {0: 0.8, 1: 0.2}},
    1: {0: {0: 0.1, 1: 0.9}, 1: {0: 0.2, 1: 0.8}},
    2: {0: {0: 0.5, 1: 0.5}, 1: {0: 0.3, 1: 0.7}}
}
rewards = {  # Definir la matriz de recompensas
    0: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    1: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}},
    2: {0: {0: 0, 1: 1}, 1: {0: 0, 1: 1}}
}
gamma = 0.9  # Factor de descuento

# Inicializar la búsqueda de la política
policy_search = PolicySearch(num_states, num_actions, transitions, rewards, gamma)

# Entrenar la búsqueda de la política
policy_search.train()  # Ejecutar el entrenamiento del agente

# Mostrar la política aprendida
print("Política aprendida:")  # Imprimir la política final
print(policy_search.policy)  # Mostrar la política aprendida
