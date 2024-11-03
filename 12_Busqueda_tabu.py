#21110344    David López Rojas   6E2

import random  # Importa la biblioteca random para generar números aleatorios

class TabuSearch:
    def __init__(self, initial_solution, neighbors_func, objective_func, tabu_list_size=10, max_iterations=100):
        # Inicializa la búsqueda Tabu con una solución inicial, funciones para obtener vecinos y calcular objetivos
        self.current_solution = initial_solution  # Solución actual inicial
        self.best_solution = initial_solution  # Mejor solución encontrada
        self.tabu_list = []  # Lista Tabu para evitar ciclos
        self.tabu_list_size = tabu_list_size  # Tamaño máximo de la lista Tabu
        self.max_iterations = max_iterations  # Número máximo de iteraciones de búsqueda
        self.neighbors_func = neighbors_func  # Función que genera vecinos de la solución actual
        self.objective_func = objective_func  # Función que evalúa la calidad de una solución

    def search(self):
        # Método que ejecuta el algoritmo de búsqueda Tabu
        for _ in range(self.max_iterations):
            # Genera vecinos de la solución actual
            neighbors = self.neighbors_func(self.current_solution)
            # Selecciona el mejor vecino basado en la función objetivo
            best_neighbor = min(neighbors, key=self.objective_func)
            # Verifica si el mejor vecino no está en la lista Tabu o si mejora la mejor solución encontrada
            if best_neighbor not in self.tabu_list or self.objective_func(best_neighbor) < self.objective_func(self.best_solution):
                self.current_solution = best_neighbor  # Actualiza la solución actual
                self.best_solution = best_neighbor  # Actualiza la mejor solución
            self.tabu_list.append(best_neighbor)  # Agrega el mejor vecino a la lista Tabu
            # Mantiene el tamaño de la lista Tabu
            if len(self.tabu_list) > self.tabu_list_size:
                self.tabu_list.pop(0)  # Elimina el elemento más antiguo si se supera el tamaño permitido
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
# Se crea una instancia del algoritmo de búsqueda Tabu
tabu_search = TabuSearch(initial_solution, neighbors, objective)
# Se ejecuta la búsqueda Tabu
best_solution = tabu_search.search()
# Se imprime la mejor solución encontrada y su valor objetivo
print("Mejor solución encontrada:", best_solution)
print("Valor objetivo en la mejor solución:", objective(best_solution))
