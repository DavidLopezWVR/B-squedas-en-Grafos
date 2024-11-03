# 21110344  David López Rojas   6E2

import random  # Importa la biblioteca random para generar números aleatorios
import math  # Importa la biblioteca math para realizar cálculos matemáticos

class SimulatedAnnealing:
    def __init__(self, initial_solution, neighbors_func, objective_func, temperature=100, cooling_rate=0.95, min_temperature=1, max_iterations=100):
        # Inicializa el algoritmo de recocido simulado con una solución inicial, funciones para obtener vecinos y calcular objetivos
        self.current_solution = initial_solution  # Solución actual inicial
        self.best_solution = initial_solution  # Mejor solución encontrada
        self.temperature = temperature  # Temperatura inicial del sistema
        self.cooling_rate = cooling_rate  # Tasa de enfriamiento
        self.min_temperature = min_temperature  # Temperatura mínima para continuar el enfriamiento
        self.max_iterations = max_iterations  # Número máximo de iteraciones para la búsqueda
        self.neighbors_func = neighbors_func  # Función que genera vecinos de la solución actual
        self.objective_func = objective_func  # Función que evalúa la calidad de una solución

    def search(self):
        # Método que ejecuta el algoritmo de recocido simulado
        for iteration in range(self.max_iterations):
            if self.temperature < self.min_temperature:  # Si la temperatura cae por debajo del mínimo, se detiene la búsqueda
                break
            # Selecciona una nueva solución aleatoria de los vecinos de la solución actual
            new_solution = random.choice(self.neighbors_func(self.current_solution))
            # Calcula la diferencia de costos entre la nueva solución y la actual
            cost_diff = self.objective_func(new_solution) - self.objective_func(self.current_solution)
            # Acepta la nueva solución si mejora el costo o con cierta probabilidad basada en la temperatura
            if cost_diff < 0 or random.random() < math.exp(-cost_diff / self.temperature):
                self.current_solution = new_solution  # Actualiza la solución actual
            # Actualiza la mejor solución encontrada si la nueva solución es mejor
            if self.objective_func(self.current_solution) < self.objective_func(self.best_solution):
                self.best_solution = self.current_solution
            # Enfría el sistema multiplicando la temperatura por la tasa de enfriamiento
            self.temperature *= self.cooling_rate
        return self.best_solution  # Devuelve la mejor solución encontrada

# Ejemplo de uso
def initial_solution():
    # Genera una solución inicial aleatoria entre 0 y 100
    return random.randint(0, 100)

def neighbors(solution):
    # Genera 10 vecinos aleatorios para la solución actual, modificando la solución por -1, 0 o 1
    return [solution + random.randint(-1, 1) for _ in range(10)]

def objective(solution):
    # Define la función objetivo: minimizar la diferencia entre la solución y 50
    return abs(solution - 50)

# Se genera una solución inicial
initial_solution = initial_solution()
# Se crea una instancia del algoritmo de recocido simulado
simulated_annealing = SimulatedAnnealing(initial_solution, neighbors, objective)
# Se ejecuta el algoritmo de recocido simulado
best_solution = simulated_annealing.search()
# Se imprime la mejor solución encontrada y su valor objetivo
print("Mejor solución encontrada:", best_solution)
print("Valor objetivo en la mejor solución:", objective(best_solution))
