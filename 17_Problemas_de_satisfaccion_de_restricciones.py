# 21110344   David López Rojas   6E2

class ConstraintSatisfactionProblem:
    def __init__(self, variables, domains, constraints):
        # Inicializa un problema de satisfacción de restricciones
        # variables: lista de variables del problema
        # domains: diccionario donde cada variable tiene una lista de valores posibles
        # constraints: lista de pares de variables que tienen restricciones de valor entre sí
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        # Verifica si asignar un valor a una variable es consistente con las restricciones
        for other_variable in assignment:
            # Comprueba si existe una restricción entre la variable y otra variable asignada previamente
            if (variable, other_variable) in self.constraints or (other_variable, variable) in self.constraints:
                # Si las variables tienen la misma asignación de valor, no es consistente
                if assignment[other_variable] == value:
                    return False
        return True

    def backtracking_search(self):
        # Inicia el proceso de búsqueda de solución mediante backtracking
        return self.backtrack({})

    def backtrack(self, assignment):
        # Método recursivo para realizar la búsqueda por backtracking
        # assignment: diccionario que mantiene la asignación de valores actual para cada variable
        if len(assignment) == len(self.variables):
            # Si todas las variables están asignadas, retorna la asignación como solución
            return assignment

        # Selecciona una variable no asignada
        unassigned_variables = [variable for variable in self.variables if variable not in assignment]
        variable = unassigned_variables[0]

        # Intenta asignar cada valor posible en el dominio de la variable seleccionada
        for value in self.domains[variable]:
            # Comprueba si la asignación es consistente con las restricciones actuales
            if self.is_consistent(variable, value, assignment):
                assignment[variable] = value  # Asigna el valor a la variable
                result = self.backtrack(assignment)  # Llama recursivamente para la siguiente variable
                if result is not None:
                    # Si se encuentra una solución, retorna el resultado
                    return result
                # Si no es solución, deshace la asignación (backtracking)
                del assignment[variable]

        return None  # Si no se encuentra solución, retorna None

# Ejemplo de uso
variables = ['A', 'B', 'C']  # Define las variables del problema
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}  # Dominios posibles de valores para cada variable
constraints = [('A', 'B'), ('A', 'C')]  # Restricciones de valor entre variables
csp = ConstraintSatisfactionProblem(variables, domains, constraints)  # Crea el problema CSP
solution = csp.backtracking_search()  # Ejecuta la búsqueda de solución mediante backtracking
print("Solución encontrada:", solution)  # Imprime la solución encontrada, si existe
