#  21110344  David López Rojas   6E2

def constraint_propagation(variables, domains, constraints):
    # Inicializamos la cola con todos los pares (variable, vecino)
    # para revisar todas las posibles restricciones entre ellos
    queue = [(variable, neighbor) for variable in variables for neighbor in variables if variable != neighbor]
    
    # Bucle principal que se ejecuta mientras haya pares en la cola
    while queue:
        # Tomamos el primer par (variable, vecino) de la cola
        variable, neighbor = queue.pop(0)
        
        # Revisamos el dominio de 'variable' con respecto a 'neighbor'
        if revise(variable, neighbor, domains, constraints):
            # Si el dominio de 'variable' queda vacío, no hay solución posible
            if not domains[variable]:
                return None
            
            # Añadimos otros pares (other_neighbor, variable) a la cola para
            # propagar cualquier cambio en el dominio de 'variable' a sus vecinos
            for other_neighbor in variables:
                if other_neighbor != neighbor and (variable, other_neighbor) in constraints:
                    queue.append((other_neighbor, variable))
    
    # Retornamos los dominios reducidos después de la propagación de restricciones
    return domains

def revise(variable1, variable2, domains, constraints):
    # Bandera que indica si el dominio de variable1 se ha modificado
    revised = False
    
    # Iteramos sobre una copia del dominio de variable1 para evitar problemas de modificación
    for value1 in list(domains[variable1]):
        # Verificamos si hay algún valor en el dominio de variable2 que satisfaga la restricción
        if not any(value2 for value2 in domains[variable2] if (value1, value2) in constraints):
            # Si no se encuentra ningún valor compatible, eliminamos 'value1' del dominio de 'variable1'
            domains[variable1].remove(value1)
            # Marcamos que el dominio de 'variable1' ha sido revisado
            revised = True
    
    # Retornamos True si el dominio de 'variable1' ha cambiado, False en caso contrario
    return revised

# Ejemplo de uso
variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2], 'C': [2, 3]}
constraints = [((1, 2), (2, 1)), ((2, 2), (1, 1)), ((2, 3), (1, 3))]

# Ejecutamos la propagación de restricciones y mostramos los dominios resultantes
reduced_domains = constraint_propagation(variables, domains, constraints)
print("Dominios reducidos después de la propagación de restricciones:", reduced_domains)
