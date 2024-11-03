#  21110344  David López Rojas   6E2

class ConflictDirectedBackjumping:
    def __init__(self, variables, domains, constraints):
        # Inicializamos las variables, dominios y restricciones para el problema CSP
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def backtracking_search(self):
        # Inicia la búsqueda en profundidad con backtracking desde un asignación vacía
        return self.backtrack({})

    def backtrack(self, assignment):
        # Si todas las variables están asignadas, se ha encontrado una solución completa
        if len(assignment) == len(self.variables):
            return assignment

        # Selecciona una variable no asignada para intentar asignarle un valor
        unassigned_variables = [variable for variable in self.variables if variable not in assignment]
        variable = unassigned_variables[0]

        # Intenta asignar cada valor del dominio de la variable seleccionada
        for value in self.domains[variable]:
            # Verifica si la asignación de este valor es consistente con las restricciones
            if self.is_consistent(variable, value, assignment):
                # Realiza la asignación temporal
                assignment[variable] = value
                # Llama recursivamente para continuar la asignación
                result = self.backtrack(assignment)
                # Si se encuentra una solución válida, se devuelve el resultado
                if result is not None:
                    return result
                # Si no se encontró solución, deshace la asignación
                del assignment[variable]

        # Si no se puede asignar un valor válido a la variable, devuelve None
        return None

    def is_consistent(self, variable, value, assignment):
        # Verifica si asignar el valor a la variable es consistente con el resto de la asignación
        for other_variable, other_value in assignment.items():
            # Comprueba si existe una restricción entre la variable y otra variable ya asignada
            if (variable, other_variable) in self.constraints or (other_variable, variable) in self.constraints:
                # Si existe conflicto (mismo valor en variables relacionadas), no es consistente
                if other_value == value:
                    return False
        # Si no hay conflictos, la asignación es consistente
        return True

# Ejemplo de uso
variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
constraints = [('A', 'B'), ('A', 'C')]

# Creamos una instancia de la clase y ejecutamos la búsqueda con backtracking
cb = ConflictDirectedBackjumping(variables, domains, constraints)
solution = cb.backtracking_search()
print("Solución encontrada:", solution)
