#21110344  David López Rojas  6E2

import numpy as np

class GridWorld:
    def __init__(self, rows, cols, start, goal):
        # Inicializa el entorno de GridWorld con el número de filas y columnas, el estado inicial y el estado objetivo
        self.rows = rows  # Número de filas en el GridWorld
        self.cols = cols  # Número de columnas en el GridWorld
        self.start = start  # Estado inicial (tupla de coordenadas)
        self.goal = goal  # Estado objetivo (tupla de coordenadas)
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimientos: derecha, izquierda, abajo, arriba
        self.num_actions = len(self.actions)  # Número de acciones posibles

    def step(self, state, action):
        # Realiza un paso en el entorno dado un estado y una acción
        next_state = (state[0] + action[0], state[1] + action[1])  # Calcula el siguiente estado
        # Comprueba si el siguiente estado está fuera de los límites del GridWorld
        if next_state[0] < 0 or next_state[0] >= self.rows or next_state[1] < 0 or next_state[1] >= self.cols:
            next_state = state  # Si la acción lleva fuera del GridWorld, el estado se mantiene igual
        # Determina la recompensa basada en si se ha alcanzado el estado objetivo
        if next_state == self.goal:
            reward = 1  # Recompensa si se alcanza la meta
        else:
            reward = 0  # Sin recompensa si no se alcanza la meta
        return next_state, reward  # Retorna el siguiente estado y la recompensa

def policy_iteration(gridworld, gamma=0.9, num_iterations=100):
    # Realiza la iteración de política para encontrar la política óptima
    policy = np.random.randint(0, gridworld.num_actions, size=(gridworld.rows, gridworld.cols))  # Política inicial aleatoria
    for _ in range(num_iterations):  # Repite por un número fijo de iteraciones
        value_function = evaluate_policy(gridworld, policy, gamma)  # Evalúa la política actual
        policy = improve_policy(gridworld, value_function, gamma)  # Mejora la política basada en la función de valor
    return policy  # Retorna la política óptima

def evaluate_policy(gridworld, policy, gamma):
    # Evalúa la función de valor para una política dada
    value_function = np.zeros((gridworld.rows, gridworld.cols))  # Inicializa la función de valor a cero
    for i in range(gridworld.rows):
        for j in range(gridworld.cols):
            action = gridworld.actions[policy[i, j]]  # Obtiene la acción de la política
            next_state, reward = gridworld.step((i, j), action)  # Calcula el siguiente estado y la recompensa
            # Actualiza la función de valor para el estado actual
            value_function[i, j] = reward + gamma * value_function[next_state[0], next_state[1]]
    return value_function  # Retorna la función de valor evaluada

def improve_policy(gridworld, value_function, gamma):
    # Mejora la política dada una función de valor
    policy = np.zeros((gridworld.rows, gridworld.cols), dtype=int)  # Inicializa la política a cero
    for i in range(gridworld.rows):
        for j in range(gridworld.cols):
            max_action = None  # Almacena la mejor acción
            max_value = float('-inf')  # Inicializa el valor máximo como negativo infinito
            for k, action in enumerate(gridworld.actions):  # Itera sobre todas las acciones posibles
                next_state, _ = gridworld.step((i, j), action)  # Calcula el siguiente estado
                value = value_function[next_state[0], next_state[1]]  # Obtiene el valor de la función para el siguiente estado
                if value > max_value:  # Si el valor es mayor que el máximo encontrado
                    max_value = value  # Actualiza el valor máximo
                    max_action = k  # Actualiza la acción que produce el valor máximo
            policy[i, j] = max_action  # Asigna la mejor acción a la política
    return policy  # Retorna la política mejorada

# Ejemplo de uso
gridworld = GridWorld(rows=3, cols=3, start=(0, 0), goal=(2, 2))  # Crea un GridWorld de 3x3
optimal_policy = policy_iteration(gridworld)  # Encuentra la política óptima
print("Política óptima:")  # Imprime la política óptima
print(optimal_policy)  # Muestra la política en forma de matriz
