# David Lopez Rojas  reg 21110344

import heapq  # Importa el módulo heapq para trabajar con colas de prioridad

# Clase que representa un nodo en el grafo con su estado, costo y el camino seguido hasta él
class Node:
    def __init__(self, state, cost, path):
        self.state = state  # Estado del nodo (nombre o identificador)
        self.cost = cost    # Costo acumulado hasta este nodo
        self.path = path    # Camino seguido para llegar a este nodo

    def __lt__(self, other):
        # Define el operador < para comparar nodos según su costo
        return self.cost < other.cost

# Implementación del algoritmo de búsqueda de costo uniforme (Uniform Cost Search)
def uniform_cost_search(graph, start, goal):
    visited = set()  # Conjunto para registrar los nodos ya visitados
    priority_queue = []  # Cola de prioridad para procesar los nodos en orden de costo mínimo
    # Insertamos el nodo inicial en la cola de prioridad con costo 0
    heapq.heappush(priority_queue, Node(start, 0, [start]))

    # Mientras haya nodos en la cola de prioridad
    while priority_queue:
        # Extraemos el nodo con el menor costo acumulado
        current_node = heapq.heappop(priority_queue)
        # Obtenemos el estado, costo y camino del nodo actual
        current_state, current_cost, current_path = current_node.state, current_node.cost, current_node.path

        # Si hemos llegado al nodo objetivo, devolvemos el camino seguido
        if current_state == goal:
            return current_path

        # Si el nodo actual no ha sido visitado
        if current_state not in visited:
            visited.add(current_state)  # Lo marcamos como visitado

            # Recorremos los vecinos del nodo actual
            for neighbor, neighbor_cost in graph[current_state].items():
                # Calculamos el costo para alcanzar el vecino
                new_cost = current_cost + neighbor_cost
                # Añadimos el vecino a la cola de prioridad con su costo actualizado y el camino acumulado
                heapq.heappush(priority_queue, Node(neighbor, new_cost, current_path + [neighbor]))

# Ejemplo de uso del algoritmo Uniform Cost Search
graph = {
    'A': {'B': 1, 'C': 4},      # Nodo 'A' conectado a 'B' (costo 1) y a 'C' (costo 4)
    'B': {'A': 1, 'C': 2, 'D': 5},  # Nodo 'B' conectado a 'A', 'C' y 'D' con sus respectivos costos
    'C': {'A': 4, 'B': 2, 'D': 1},  # Nodo 'C' conectado a 'A', 'B' y 'D'
    'D': {'B': 5, 'C': 1}        # Nodo 'D' conectado a 'B' y 'C'
}

start_node = 'A'  # Nodo de inicio
goal_node = 'D'   # Nodo objetivo

# Llama a la función de búsqueda de costo uniforme
path = uniform_cost_search(graph, start_node, goal_node)
print("Camino encontrado:", path)  # Imprime el camino encontrado
