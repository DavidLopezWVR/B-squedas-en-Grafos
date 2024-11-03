#21110344  David López Rojas  6E2

import numpy as np  # Importar la biblioteca NumPy para operaciones numéricas

class ActiveRL:
    def __init__(self, num_states, num_actions, alpha, gamma, epsilon, max_steps):
        # Inicializar el agente de aprendizaje por refuerzo activo
        self.num_states = num_states  # Número de estados en el entorno
        self.num_actions = num_actions  # Número de acciones disponibles
        self.alpha = alpha  # Tasa de aprendizaje
        self.gamma = gamma  # Factor de descuento
        self.epsilon = epsilon  # Tasa de exploración vs. explotación
        self.max_steps = max_steps  # Máximo de pasos permitidos por episodio
        self.Q = np.zeros((num_states, num_actions))  # Inicializar la matriz Q a cero

    def select_action(self, state):
        # Seleccionar una acción basada en la estrategia epsilon-greedy
        if np.random.uniform(0, 1) < self.epsilon:  # Exploración
            return np.random.randint(0, self.num_actions)  # Elegir acción aleatoria
        else:
            return np.argmax(self.Q[state])  # Elegir la acción con el valor Q más alto (explotación)

    def update_q_value(self, state, action, reward, next_state):
        # Actualizar el valor Q basado en la recompensa recibida y el estado siguiente
        best_next_action = np.argmax(self.Q[next_state])  # Mejor acción en el estado siguiente
        td_target = reward + self.gamma * self.Q[next_state, best_next_action]  # Objetivo de TD
        td_error = td_target - self.Q[state, action]  # Error de TD
        self.Q[state, action] += self.alpha * td_error  # Actualización de la matriz Q

    def train(self, env):
        # Entrenar el agente en el entorno
        for episode in range(self.max_steps):  # Para cada episodio
            state = env.reset()  # Reiniciar el entorno y obtener el estado inicial
            for step in range(self.max_steps):  # Para cada paso en el episodio
                action = self.select_action(state)  # Seleccionar acción
                next_state, reward, done, _ = env.step(action)  # Ejecutar acción y obtener resultado
                self.update_q_value(state, action, reward, next_state)  # Actualizar el valor Q
                state = next_state  # Moverse al siguiente estado
                if done:  # Si el episodio ha terminado
                    break  # Salir del bucle de pasos

# Clase de entorno simple de ejemplo
class Environment:
    def __init__(self):
        self.num_states = 2  # Definir el número de estados
        self.num_actions = 2  # Definir el número de acciones
        self.state = 0  # Estado inicial

    def reset(self):
        self.state = 0  # Reiniciar el entorno
        return self.state  # Devolver el estado inicial

    def step(self, action):
        # Ejecutar la acción y devolver el siguiente estado, la recompensa y si se ha terminado el episodio
        if self.state == 0 and action == 0:  # Si en estado 0 y se toma acción 0
            self.state = 1  # Cambiar al estado 1
            reward = 1  # Asignar recompensa de 1
        elif self.state == 1 and action == 1:  # Si en estado 1 y se toma acción 1
            self.state = 0  # Cambiar al estado 0
            reward = 1  # Asignar recompensa de 1
        else:
            reward = 0  # Si no se cumplen las condiciones, recompensa es 0
        done = False  # No hay condición de finalización en este entorno
        return self.state, reward, done, {}  # Devolver el estado siguiente, recompensa y otros valores

# Parámetros del algoritmo
num_states = 2  # Número de estados en el entorno
num_actions = 2  # Número de acciones disponibles
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.1  # Tasa de exploración
max_steps = 1000  # Máximo de pasos por episodio

# Inicializar el agente de aprendizaje por refuerzo activo
active_rl = ActiveRL(num_states, num_actions, alpha, gamma, epsilon, max_steps)

# Entrenar el agente en el ambiente
env = Environment()  # Crear el entorno
active_rl.train(env)  # Entrenar el agente

# Mostrar la matriz Q aprendida por el agente
print("Matriz Q aprendida:")  
print(active_rl.Q)  # Imprimir la matriz Q final
