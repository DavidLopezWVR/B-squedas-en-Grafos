#21110344  David López Rojas  6E2

import numpy as np  # Importar la biblioteca NumPy para operaciones numéricas

class ExplorationExploitation:
    def __init__(self, epsilon):
        # Inicializar el objeto con un valor de epsilon
        self.epsilon = epsilon  # Tasa de exploración; controla la probabilidad de explorar

    def select_action(self, q_values):
        # Seleccionar una acción basada en la estrategia epsilon-greedy
        if np.random.uniform(0, 1) < self.epsilon:  # Generar un número aleatorio y compararlo con epsilon
            return np.random.randint(0, len(q_values))  # Exploración: seleccionar una acción aleatoria
        else:
            return np.argmax(q_values)  # Explotación: seleccionar la acción con el mayor valor Q estimado

# Ejemplo de uso
exploration_exploitation = ExplorationExploitation(epsilon=0.1)  # Crear una instancia con epsilon=0.1

# Q-values estimados para tres acciones
q_values = [0.2, 0.5, 0.8]  # Valores Q estimados que indican la calidad de cada acción

# Selección de acción basada en exploración vs. explotación
action = exploration_exploitation.select_action(q_values)  # Elegir una acción usando la estrategia definida

# Imprimir la acción seleccionada
print("Acción seleccionada:", action)  # Mostrar el resultado de la selección de acción
