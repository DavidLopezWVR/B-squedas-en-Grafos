# 21110344   David López Rojas   6E2

import random  # Importa la biblioteca random para generar números aleatorios

class BeamSearch:
    def __init__(self, initial_solutions, neighbors_func, objective_func, beam_width=5, max_iterations=100):
        # Inicializa el algoritmo de búsqueda en haz con una lista de soluciones iniciales, funciones para obtener vecinos y evaluar objetivos
        self.current_solutions = initial_solutions  # Soluciones actuales en la búsqueda
        self.beam_width = beam_width  # Ancho del haz, número de soluciones a mantener en cada iteración
        self.max_iterations = max_iterations  # Número máximo de iteraciones para la búsqueda
        self.neighbors_func = neighbors_func  # Función que genera vecinos de cada solución
        self.objective_func = objective_func  # Función que evalúa la calidad de una solución

    def search(self):
        # Método que ejecuta el algoritmo de búsqueda en haz
        for _ in range(self.max_iterations):
            next_solutions = []  # Lista para almacenar las soluciones generadas en la próxima iteración
            for solution in self.current_solutions:  # Itera sobre cada solución actual
                neighbors = self.neighbors_func(solution)  # Obtiene los vecinos de la solución actual
                next_solutions.extend(neighbors)  # Agrega los vecinos a la lista de soluciones de la próxima iteración
            next_solutions.sort(key=self.objective_func)  # Ordena las soluciones generadas por su valor objetivo
            self.current_solutions = next_solutions[:self.beam_width]  # Mantiene solo las mejores soluciones según el ancho del haz
            if self.objective_func(self.current_solutions[0]) == 0:  # Si la mejor solución es la óptima (costo 0)
                break  # Detiene la búsqueda
        return self.current_solutions[0]  # Devuelve la mejor solución encontrada

# Ejemplo de uso
def initial_solutions():
    # Genera una lista de soluciones iniciales aleatorias
    return [random.randint(0, 100)]

def neighbors(solution):
    # Genera 10 vecinos aleatorios para la solución actual, modificando la solución por -1, 0 o 1
    return [solution + random.randint(-1, 1) for _ in range(10)]

def objective(solution):
    # Define la función objetivo: minimizar la diferencia entre la solución y 50
    return abs(solution - 50)

# Se generan soluciones iniciales aleatorias
initial_solutions = initial_solutions()
# Se crea una instancia del algoritmo de búsqueda en haz
beam_search = BeamSearch(initial_solutions, neighbors, objective)
# Se ejecuta la búsqueda en haz
best_solution = beam_search.search()
# Se imprime la mejor solución encontrada y su valor objetivo
print("Mejor solución encontrada:", best_solution)
print("Valor objetivo en la mejor solución:", objective(best_solution))
