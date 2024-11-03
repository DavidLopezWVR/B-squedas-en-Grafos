#  21110344   David López Rojas    6E2

import heapq  # Importa la biblioteca heapq para implementar una cola de prioridad

class Graph:
    def __init__(self, graph_dict=None):
        # Inicializa el grafo con un diccionario de adyacencia
        if graph_dict is None:
            graph_dict = {}  # Si no se proporciona un diccionario, se inicializa uno vacío
        self.graph_dict = graph_dict

    def add_edge(self, node, neighbor, cost):
        # Añade un borde al grafo con el coste asociado
        if node not in self.graph_dict:
            self.graph_dict[node] = []  # Si el nodo no existe, inicializa su lista de vecinos
        self.graph_dict[node].append((neighbor, cost))  # Agrega el vecino y el coste

def aostar_search(graph, start, goal, heuristic):
    # Implementa la búsqueda AO* (A* optimizado)
    visited = set()  # Conjunto para mantener un registro de los nodos visitados
    priority_queue = [(0, start)]  # Cola de prioridad inicial con el nodo de inicio
    g_score = {node: float('inf') for node in graph.graph_dict}  # Inicializa g_score para todos los nodos
    g_score[start] = 0  # Establece el coste del nodo de inicio a 0

    while priority_queue:
        # Mientras haya nodos en la cola de prioridad
        current_cost, current_node = heapq.heappop(priority_queue)  # Obtiene el nodo con menor coste
        if current_node == goal:
            return True  # Si se alcanza el nodo objetivo, devuelve True
        if current_node in visited:
            continue  # Si ya se visitó el nodo, continúa con el siguiente
        visited.add(current_node)  # Marca el nodo como visitado

        # Recorre los vecinos del nodo actual
        for neighbor, cost in graph.graph_dict[current_node]:
            new_cost = g_score[current_node] + cost  # Calcula el nuevo coste para el vecino
            # Si el nuevo coste es menor que el coste previamente registrado para el vecino
            if new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost  # Actualiza el g_score del vecino
                priority_queue.append((max(new_cost + heuristic(neighbor, goal), current_cost), neighbor))
                # Añade el vecino a la cola de prioridad, considerando el coste y la heurística
                heapq.heapify(priority_queue)  # Reorganiza la cola de prioridad

    return False  # Si no se encuentra un camino al objetivo, devuelve False

def astar_search(graph, start, goal, heuristic):
    # Implementa la búsqueda A* estándar
    visited = set()  # Conjunto para mantener un registro de los nodos visitados
    priority_queue = [(0, start)]  # Cola de prioridad inicial con el nodo de inicio
    g_score = {node: float('inf') for node in graph.graph_dict}  # Inicializa g_score para todos los nodos
    g_score[start] = 0  # Establece el coste del nodo de inicio a 0

    while priority_queue:
        # Mientras haya nodos en la cola de prioridad
        current_cost, current_node = heapq.heappop(priority_queue)  # Obtiene el nodo con menor coste
        if current_node == goal:
            return True  # Si se alcanza el nodo objetivo, devuelve True
        if current_node in visited:
            continue  # Si ya se visitó el nodo, continúa con el siguiente
        visited.add(current_node)  # Marca el nodo como visitado

        # Recorre los vecinos del nodo actual
        for neighbor, cost in graph.graph_dict[current_node]:
            new_cost = g_score[current_node] + cost  # Calcula el nuevo coste para el vecino
            # Si el nuevo coste es menor que el coste previamente registrado para el vecino
            if new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost  # Actualiza el g_score del vecino
                priority_queue.append((new_cost + heuristic(neighbor, goal), neighbor))
                # Añade el vecino a la cola de prioridad con el coste total
                heapq.heapify(priority_queue)  # Reorganiza la cola de prioridad

    return False  # Si no se encuentra un camino al objetivo, devuelve False

# Ejemplo de uso
graph = Graph({
    'A': [('B', 5), ('C', 8)],  # Define las aristas y sus costos
    'B': [('D', 12), ('E', 15)],
    'C': [('F', 10)],
    'D': [('G', 3)],
    'E': [('G', 20)],
    'F': [('G', 6)],
    'G': []  # Nodo objetivo sin vecinos
})

def heuristic(node, goal):
    # Heurística: distancia en línea recta hasta el nodo objetivo
    return abs(ord(node) - ord(goal))  # Calcula la diferencia entre caracteres ASCII

start_node = 'A'  # Nodo inicial
goal_node = 'G'  # Nodo objetivo
result_aostar = aostar_search(graph, start_node, goal_node, heuristic)  # Ejecuta la búsqueda AO*
result_astar = astar_search(graph, start_node, goal_node, heuristic)  # Ejecuta la búsqueda A*

# Imprime los resultados de las búsquedas
print("¿Se encontró un camino al objetivo utilizando AO*?", result_aostar)
print("¿Se encontró un camino al objetivo utilizando A*?", result_astar)
