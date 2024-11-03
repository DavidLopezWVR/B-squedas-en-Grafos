#21110344  David López Rojas  6E2

def backtracking_search(assignment, variables, domains, constraints):
    # Si todas las variables están asignadas, retorna la asignación como solución completa
    if len(assignment) == len(variables):
        return assignment

    # Encuentra las variables que aún no están asignadas
    unassigned_variables = [variable for variable in variables if variable not in assignment]
    # Selecciona la primera variable no asignada
    variable = unassigned_variables[0]

    # Intenta asignar cada valor en el dominio de la variable seleccionada
    for value in domains[variable]:
        # Verifica si la asignación es consistente con las restricciones actuales
        if is_consistent(variable, value, assignment, constraints):
            assignment[variable] = value  # Asigna el valor a la variable
            # Llama recursivamente para asignar el resto de las variables
            result = backtracking_search(assignment, variables, domains, constraints)
            if result is not None:
                # Si se encuentra una solución completa, retorna el resultado
                return result
            # Si no se encuentra solución, elimina la asignación (backtracking)
            del assignment[variable]

    # Si no se encuentra ninguna asignación válida, retorna None
    return None

def is_consistent(variable, value, assignment, constraints):
    # Verifica si la asignación de un valor a una variable es consistente con las restricciones
    for other_variable, other_value in assignment.items():
        # Comprueba si existe una restricción entre la variable actual y otra variable ya asignada
        if (variable, other_variable) in constraints or (other_variable, variable) in constraints:
            # Si las variables tienen el mismo valor, la asignación no es consistente
            if other_value == value:
                return False
    return True

# Ejemplo de uso
variables = ['A', 'B', 'C']  # Variables del problema
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}  # Dominios de valores para cada variable
constraints = [('A', 'B'), ('A', 'C')]  # Restricciones entre pares de variables
assignment = {}  # Diccionario vacío para almacenar la asignación de variables
solution = backtracking_search(assignment, variables, domains, constraints)  # Ejecuta la búsqueda
print("Solución encontrada:", solution)  # Imprime la solución si se encuentra
