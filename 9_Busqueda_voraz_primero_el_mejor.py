# 21110344  David López Rojas    6E2

import heapq

# Clase que representa un grafo
class Graph:
    def __init__(self, graph_dict=None):
        # Inicializa el diccionario del grafo como un diccionario vacío si no se proporciona uno
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict  # Almacena el diccionario de adyacencia del grafo

    # Método para agregar una arista entre un nodo y su vecino con un costo asociado
    def add_edge(self, node, neighbor, cost):
        # Si el nodo no está en el diccionario, se inicializa con una lista vacía
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        # Agrega el vecino y el costo a la lista de adyacencia del nodo
        self.graph_dict[node].append((neighbor, cost))

# Función para realizar la búsqueda greedy best first
def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()  # Conjunto de nodos ya visitados
    # Cola de prioridad, inicia con el nodo de inicio y su heurística hacia el objetivo
    priority_queue = [(heuristic(start, goal), start)]
    
    # Bucle principal de búsqueda
    while priority_queue:
        # Extrae el nodo con la menor heurística
        _, current_node = heapq.heappop(priority_queue)
        # Si se alcanza el nodo objetivo, se retorna True
        if current_node == goal:
            return True
        visited.add(current_node)  # Marca el nodo actual como visitado
        # Explora cada vecino del nodo actual
        for neighbor, cost in graph.graph_dict[current_node]:
            if neighbor not in visited:  # Si el vecino no ha sido visitado
                # Agrega el vecino y su heurística a la cola de prioridad
                heapq.heappush(priority_queue, (heuristic(neighbor, goal), neighbor))
    
    # Si se termina el bucle sin encontrar el objetivo, retorna False
    return False

# Ejemplo de uso
graph = Graph({
    'A': [('B', 5), ('C', 8)],  # Nodo A conectado a B y C con sus respectivos costos
    'B': [('D', 12), ('E', 15)],  # Nodo B conectado a D y E
    'C': [('F', 10)],  # Nodo C conectado a F
    'D': [('G', 3)],   # Nodo D conectado a G
    'E': [('G', 20)],  # Nodo E también conectado a G
    'F': [('G', 6)],   # Nodo F conectado a G
    'G': []  # Nodo G es el objetivo y no tiene vecinos
})

# Función heurística que estima el costo a alcanzar el nodo objetivo
def heuristic(node, goal):
    # Heurística: distancia en línea recta hasta el nodo objetivo, calculada usando las posiciones ASCII
    return abs(ord(node) - ord(goal))

start_node = 'A'  # Nodo inicial
goal_node = 'G'   # Nodo objetivo
# Llama a la búsqueda greedy best first para encontrar un camino desde el nodo inicial al objetivo
result = greedy_best_first_search(graph, start_node, goal_node, heuristic)
print("¿Se encontró un camino al objetivo?", result)  # Imprime si se encontró un camino
