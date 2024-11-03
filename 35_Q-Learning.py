#21110344  David López Rojas  6E2

import numpy as np  # Importar la biblioteca NumPy para realizar operaciones numéricas

class QLearning:
    def __init__(self, num_states, num_actions, alpha, gamma, epsilon, max_steps):
        # Inicializar el agente Q-Learning
        self.num_states = num_states  # Número de estados en el entorno
        self.num_actions = num_actions  # Número de acciones disponibles
        self.alpha = alpha  # Tasa de aprendizaje
        self.gamma = gamma  # Factor de descuento para valorar futuras recompensas
        self.epsilon = epsilon  # Tasa de exploración frente a explotación
        self.max_steps = max_steps  # Máximo de pasos permitidos por episodio
        self.Q = np.zeros((num_states, num_actions))  # Inicializar la matriz Q a cero

    def select_action(self, state):
        # Seleccionar una acción usando una estrategia epsilon-greedy
        if np.random.uniform(0, 1) < self.epsilon:  # Condición de exploración
            return np.random.randint(0, self.num_actions)  # Elegir una acción aleatoria
        else:
            return np.argmax(self.Q[state])  # Elegir la acción que maximiza el valor Q (explotación)

    def update_q_value(self, state, action, reward, next_state):
        # Actualizar el valor Q usando la ecuación del Q-Learning
        td_target = reward + self.gamma * np.max(self.Q[next_state])  # Objetivo de diferencia temporal (TD)
        td_error = td_target - self.Q[state, action]  # Error de TD
        self.Q[state, action] += self.alpha * td_error  # Actualización de la matriz Q

    def train(self, env):
        # Entrenamiento del agente en el ambiente
        for episode in range(self.max_steps):  # Para cada episodio
            state = env.reset()  # Reiniciar el estado del ambiente
            for step in range(self.max_steps):  # Para cada paso en el episodio
                action = self.select_action(state)  # Seleccionar una acción
                next_state, reward, done, _ = env.step(action)  # Ejecutar la acción en el ambiente
                self.update_q_value(state, action, reward, next_state)  # Actualizar la matriz Q
                state = next_state  # Moverse al siguiente estado
                if done:  # Verificar si se ha alcanzado un estado terminal
                    break  # Salir del bucle de pasos

# Ejemplo de ambiente simple
class Environment:
    def __init__(self):
        self.num_states = 2  # Definir el número de estados
        self.num_actions = 2  # Definir el número de acciones

    def reset(self):
        return 0  # Reiniciar el estado a uno predeterminado (estado 0)

    def step(self, action):
        # Definir las recompensas y los estados siguientes en función de las acciones
        if action == 0:  # Si se toma la acción 0
            return 1, 0, False, {}  # Estado siguiente, recompensa, estado terminal, información adicional
        else:  # Si se toma la acción 1
            return 0, 1, False, {}  # Estado siguiente, recompensa, estado terminal, información adicional

# Parámetros del algoritmo Q-Learning
num_states = 2  # Número de estados en el entorno
num_actions = 2  # Número de acciones disponibles
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Tasa de exploración
max_steps = 1000  # Número máximo de pasos por episodio

# Inicializar el agente Q-Learning
q_learning_agent = QLearning(num_states, num_actions, alpha, gamma, epsilon, max_steps)

# Entrenar el agente en el ambiente
env = Environment()  # Crear el entorno
q_learning_agent.train(env)  # Entrenar el agente

# Mostrar la matriz Q aprendida por el agente
print("Matriz Q aprendida:")  
print(q_learning_agent.Q)  # Imprimir la matriz Q final
