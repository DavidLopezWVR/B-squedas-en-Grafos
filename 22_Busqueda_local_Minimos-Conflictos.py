# 21110344  David López Rojas  6E2

import random

class MinimumConflicts:
    def __init__(self, variables, domains, constraints, max_steps=1000):
        # Inicializa las variables, dominios y restricciones para el problema CSP
        # max_steps define el número máximo de iteraciones permitidas en la búsqueda
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.max_steps = max_steps

    def minimum_conflicts_search(self):
        # Genera una asignación inicial aleatoria
        assignment = self.initial_assignment()
        
        # Itera hasta el máximo de pasos permitidos o hasta encontrar una solución
        for _ in range(self.max_steps):
            # Si la asignación actual es una solución válida, la retorna
            if self.is_solution(assignment):
                return assignment
            
            # Selecciona una variable que esté en conflicto en la asignación actual
            conflicted_variable = self.get_conflicted_variable(assignment)
            
            # Encuentra el valor para la variable en conflicto que minimiza el número de conflictos
            value = self.minimum_conflicts_value(conflicted_variable, assignment)
            
            # Actualiza la asignación con el valor que minimiza los conflictos
            assignment[conflicted_variable] = value
        
        # Si no se encuentra solución en el número máximo de pasos, retorna None
        return None

    def initial_assignment(self):
        # Genera una asignación inicial aleatoria seleccionando un valor al azar de cada dominio
        return {variable: random.choice(self.domains[variable]) for variable in self.variables}

    def is_solution(self, assignment):
        # Verifica si la asignación actual es una solución válida para todas las restricciones
        return all(self.is_consistent(variable, assignment) for variable in self.variables)

    def is_consistent(self, variable, assignment):
        # Verifica si la asignación de una variable es consistente con las restricciones
        for other_variable, other_value in assignment.items():
            # Comprueba si existe una restricción entre la variable y otra asignada
            if (variable, other_variable) in self.constraints or (other_variable, variable) in self.constraints:
                # Si hay conflicto (mismo valor en variables relacionadas), retorna False
                if other_value == assignment[variable]:
                    return False
        # Si no hay conflictos, la asignación es consistente
        return True

    def get_conflicted_variable(self, assignment):
        # Genera una lista de variables que están en conflicto en la asignación actual
        conflicted_variables = [variable for variable in self.variables if not self.is_consistent(variable, assignment)]
        # Selecciona y retorna una variable en conflicto de forma aleatoria
        return random.choice(conflicted_variables)

    def minimum_conflicts_value(self, variable, assignment):
        # Encuentra el valor en el dominio de 'variable' que minimiza el número de conflictos
        min_conflicts = float('inf')
        min_value = None
        # Itera sobre cada valor en el dominio de la variable
        for value in self.domains[variable]:
            # Calcula el número de conflictos que surgirían al asignar este valor
            conflicts = sum(
                not self.is_consistent(other_variable, {**assignment, variable: value})
                for other_variable in self.variables
            )
            # Si el número de conflictos es menor que el mínimo encontrado, actualiza el valor
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                min_value = value
        # Retorna el valor que minimiza los conflictos
        return min_value

# Ejemplo de uso
variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
constraints = [('A', 'B'), ('A', 'C')]

# Crea una instancia de la clase y ejecuta la búsqueda de mínimo de conflictos
mc = MinimumConflicts(variables, domains, constraints)
solution = mc.minimum_conflicts_search()
print("Solución encontrada:", solution)
