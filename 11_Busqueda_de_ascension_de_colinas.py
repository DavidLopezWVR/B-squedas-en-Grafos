#21110344  David López Rojas    6E2

import random  # Importa la biblioteca random para generar números aleatorios

def hill_climbing(problem, max_iterations):
    # Implementa el algoritmo de escalada de colinas
    current_state = problem.initial_state()  # Inicializa el estado actual llamando a la función de estado inicial
    for _ in range(max_iterations):
        # Itera un número máximo de veces especificado
        neighbors = problem.neighbors(current_state)  # Obtiene los vecinos del estado actual
        # Selecciona el vecino con el mejor valor heurístico (máximo)
        next_state = max(neighbors, key=lambda state: problem.heuristic(state))
        # Compara el valor heurístico del siguiente estado con el estado actual
        if problem.heuristic(next_state) <= problem.heuristic(current_state):
            # Si no se mejora, se detiene el algoritmo
            break
        current_state = next_state  # Actualiza el estado actual al siguiente estado
    return current_state  # Devuelve el estado actual (máximo local encontrado)

class Problem:
    def __init__(self, initial_state, heuristic, neighbors):
        # Inicializa el problema con estado inicial, función heurística y función de vecinos
        self.initial_state = initial_state  # Función que retorna el estado inicial
        self.heuristic = heuristic  # Función heurística que evalúa el estado
        self.neighbors = neighbors  # Función que genera vecinos de un estado

# Ejemplo de uso
def initial_state():
    # Genera un estado inicial aleatorio entre 0 y 100
    return random.randint(0, 100)

def heuristic(state):
    # Define la función heurística que busca maximizar -x^2 (máximo local de una función cuadrática negativa)
    return -state ** 2  # Objetivo: encontrar el máximo de la función cuadrática negativa

def neighbors(state):
    # Genera los vecinos del estado actual, moviéndose hacia arriba y hacia abajo
    return [state + 1, state - 1]  # Retorna una lista con el estado +1 y el estado -1

# Crea una instancia del problema
problem = Problem(initial_state, heuristic, neighbors)
max_iterations = 1000  # Define el número máximo de iteraciones para el algoritmo
solution = hill_climbing(problem, max_iterations)  # Ejecuta el algoritmo de escalada de colinas
# Imprime el máximo local encontrado y su valor en la función objetivo
print("Máximo local encontrado:", solution)
print("Valor de la función objetivo en el máximo local:", heuristic(solution))
