# 21110344 David López Rojas   6E2

def forward_checking(assignment, variables, domains, constraints):
    # Recorre cada variable en la lista de variables
    for variable in variables:
        # Solo procesa variables que aún no tienen asignación
        if variable not in assignment:
            # Itera sobre una copia del dominio de la variable actual
            for value in list(domains[variable]):
                # Asigna temporalmente el valor a la variable
                assignment[variable] = value
                # Verifica si la asignación es consistente con las restricciones
                if not is_consistent(variable, value, assignment, constraints):
                    # Si no es consistente, elimina el valor del dominio de la variable
                    domains[variable].remove(value)
            # Si el dominio de la variable queda vacío, se retorna None, indicando que no hay solución
            if not domains[variable]:
                return None
    # Retorna la asignación actual si no hay problemas
    return assignment

def is_consistent(variable, value, assignment, constraints):
    # Verifica la consistencia de la asignación actual para la variable y su valor
    for other_variable, other_value in assignment.items():
        # Revisa si existe una restricción entre la variable actual y otra variable ya asignada
        if (variable, other_variable) in constraints or (other_variable, variable) in constraints:
            # Si ambas variables tienen el mismo valor, la asignación no es consistente
            if other_value == value:
                return False
    return True

# Ejemplo de uso
variables = ['A', 'B', 'C']  # Lista de variables en el problema
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}  # Dominios de posibles valores para cada variable
constraints = [('A', 'B'), ('A', 'C')]  # Restricciones entre pares de variables
assignment = {}  # Diccionario vacío para la asignación de variables
solution = forward_checking(assignment, variables, domains, constraints)  # Ejecuta forward checking
print("Asignación después de la comprobación hacia adelante:", solution)  # Imprime la asignación resultante
