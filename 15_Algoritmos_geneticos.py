# 21110344  David López Rojas   6E2

import random  # Importa la biblioteca random para generar números aleatorios

class GeneticAlgorithm:
    def __init__(self, population_size, gene_length, crossover_rate, mutation_rate, fitness_func, selection_func):
        # Inicializa los parámetros del algoritmo genético
        self.population_size = population_size  # Tamaño de la población
        self.gene_length = gene_length  # Longitud de los genes (número de bits)
        self.crossover_rate = crossover_rate  # Tasa de cruce (probabilidad de realizar crossover)
        self.mutation_rate = mutation_rate  # Tasa de mutación (probabilidad de mutar un gen)
        self.fitness_func = fitness_func  # Función para evaluar la aptitud de un individuo
        self.selection_func = selection_func  # Función para seleccionar padres

    def generate_population(self):
        # Genera una población inicial aleatoria de individuos
        return [[random.randint(0, 1) for _ in range(self.gene_length)] for _ in range(self.population_size)]

    def crossover(self, parent1, parent2):
        # Realiza la operación de crossover entre dos padres para crear dos hijos
        crossover_point = random.randint(1, self.gene_length - 1)  # Elige un punto de cruce aleatorio
        # Crea dos nuevos individuos (hijos) combinando genes de los padres
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2  # Retorna los hijos generados

    def mutate(self, individual):
        # Aplica mutaciones a un individuo según la tasa de mutación
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:  # Si se decide mutar un gen
                individual[i] = 1 - individual[i]  # Cambia el valor del gen (de 0 a 1 o de 1 a 0)
        return individual  # Retorna el individuo mutado

    def evolve(self, population):
        # Evoluciona la población a la siguiente generación
        new_population = []  # Lista para almacenar la nueva población
        while len(new_population) < self.population_size:
            # Selecciona dos padres usando la función de selección
            parent1 = self.selection_func(population, self.fitness_func)
            parent2 = self.selection_func(population, self.fitness_func)
            if random.random() < self.crossover_rate:  # Decide si realizar crossover
                child1, child2 = self.crossover(parent1, parent2)  # Realiza crossover
                new_population.append(self.mutate(child1))  # Agrega el hijo mutado a la nueva población
                new_population.append(self.mutate(child2))  # Agrega el otro hijo mutado
            else:
                # Si no se realiza crossover, muta y agrega los padres a la nueva población
                new_population.append(self.mutate(parent1))
                new_population.append(self.mutate(parent2))
        return new_population  # Retorna la nueva población generada

# Ejemplo de uso
def fitness(solution):
    # Función de aptitud que suma los valores de los genes (el número de 1's en el individuo)
    return sum(solution)

def roulette_wheel_selection(population, fitness_func):
    # Selección de individuos basada en la rueda de ruleta
    total_fitness = sum(fitness_func(individual) for individual in population)  # Calcula la aptitud total
    selection_point = random.uniform(0, total_fitness)  # Elige un punto de selección aleatorio
    cumulative_fitness = 0  # Inicializa la aptitud acumulativa
    for individual in population:  # Recorre la población
        cumulative_fitness += fitness_func(individual)  # Suma la aptitud de cada individuo
        if cumulative_fitness > selection_point:  # Si la aptitud acumulativa supera el punto de selección
            return individual  # Retorna el individuo seleccionado

# Parámetros del algoritmo genético
population_size = 100  # Tamaño de la población
gene_length = 10  # Longitud de cada individuo (número de genes)
crossover_rate = 0.8  # Tasa de cruce
mutation_rate = 0.01  # Tasa de mutación
generations = 100  # Número de generaciones a evolucionar

# Crea una instancia del algoritmo genético con los parámetros definidos
genetic_algorithm = GeneticAlgorithm(population_size, gene_length, crossover_rate, mutation_rate, fitness, roulette_wheel_selection)
# Genera la población inicial
population = genetic_algorithm.generate_population()

# Itera a través de las generaciones, evolucionando la población
for generation in range(generations):
    population = genetic_algorithm.evolve(population)  # Evoluciona la población
    best_individual = max(population, key=fitness)  # Encuentra el mejor individuo en la población actual
    print("Generación {}: Mejor individuo: {}, Fitness: {}".format(generation + 1, best_individual, fitness(best_individual)))
