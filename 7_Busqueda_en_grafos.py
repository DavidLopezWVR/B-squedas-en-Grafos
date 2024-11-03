# 21110344 David López Rojas    6E2

from collections import deque

# Clase que representa un grafo
class Graph:
    def __init__(self, graph_dict=None):
        # Inicializa el diccionario del grafo, donde cada nodo tiene una lista de vecinos
        if graph_dict is None:  # Si no se pasa un diccionario, crea uno vacío
            graph_dict = {}
        self.graph_dict = graph_dict  # Almacena el diccionario de adyacencia del grafo

    # Método para agregar una arista entre un nodo y su vecino
    def add_edge(self, node, neighbor):
        # Si el nodo no existe en el diccionario, crea una lista vacía para él
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        # Agrega el vecino a la lista de adyacencia del nodo
        self.graph_dict[node].append(neighbor)

    # Método de búsqueda en anchura (Breadth-First Search, BFS) para encontrar un camino entre dos nodos
    def bfs(self, start, goal):
        visited = set()  # Conjunto para almacenar los nodos ya visitados
        # Cola para la búsqueda, que almacena tuplas de (nodo actual, camino hasta ese nodo)
        queue = deque([(start, [start])])

        # Mientras haya nodos en la cola por explorar
        while queue:
            # Extrae el primer nodo de la cola junto con el camino hasta él
            current_node, path = queue.popleft()
            # Marca el nodo actual como visitado
            visited.add(current_node)

            # Si el nodo actual es el objetivo, retorna el camino encontrado
            if current_node == goal:
                return path

            # Explora los vecinos del nodo actual
            for neighbor in self.graph_dict.get(current_node, []):
                # Si el vecino no ha sido visitado, lo añade a la cola con el camino actualizado
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)  # Marca el vecino como visitado para evitar ciclos

# Ejemplo de uso de la clase Graph y del método bfs
graph = Graph({
    'A': ['B', 'C'],  # Nodo 'A' conectado a 'B' y 'C'
    'B': ['D', 'E'],  # Nodo 'B' conectado a 'D' y 'E'
    'C': ['F'],       # Nodo 'C' conectado a 'F'
    'D': [],          # Nodo 'D' no tiene conexiones
    'E': ['F'],       # Nodo 'E' conectado a 'F'
    'F': []           # Nodo 'F' no tiene conexiones
})

start_node = 'A'  # Nodo de inicio para la búsqueda
goal_node = 'F'   # Nodo objetivo
path = graph.bfs(start_node, goal_node)  # Llama al método bfs para encontrar un camino
print("Camino encontrado:", path)
