# David Lopez Rojas  reg 21110344

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

    # Método de búsqueda limitada en profundidad (Depth-Limited Search, DLS)
    def dls(self, start, goal, depth_limit, visited=None):
        # Inicializa el conjunto de nodos visitados si es la primera llamada
        if visited is None:
            visited = set()
        # Comprueba si el límite de profundidad es mayor o igual a 0
        if depth_limit >= 0:
            # Marca el nodo inicial como visitado
            visited.add(start)
            # Imprime el nodo actual
            print(start)
            # Si el nodo actual es el objetivo, devuelve True indicando que se encontró el objetivo
            if start == goal:
                return True
            # Si se alcanza el límite de profundidad, retorna False
            if depth_limit == 0:
                return False
            # Recorre los vecinos del nodo actual
            for neighbor in self.graph_dict.get(start, []):
                # Si el vecino no ha sido visitado, llama recursivamente a DLS en el vecino,
                # reduciendo el límite de profundidad en 1
                if neighbor not in visited:
                    if self.dls(neighbor, goal, depth_limit - 1, visited):
                        return True
        # Retorna False si no se encuentra el objetivo en el límite de profundidad dado
        return False

# Ejemplo de uso de la clase Graph y del método DLS
graph = Graph({
    'A': ['B', 'C'],  # Nodo 'A' conectado a 'B' y 'C'
    'B': ['D', 'E'],  # Nodo 'B' conectado a 'D' y 'E'
    'C': ['F'],       # Nodo 'C' conectado a 'F'
    'D': [],          # Nodo 'D' no tiene conexiones
    'E': ['F'],       # Nodo 'E' conectado a 'F'
    'F': []           # Nodo 'F' no tiene conexiones
})

start_node = 'A'      # Nodo de inicio para el recorrido DLS
goal_node = 'F'       # Nodo objetivo
depth_limit = 2       # Límite de profundidad para la búsqueda
print("Recorrido DLS:")
graph.dls(start_node, goal_node, depth_limit)  # Llama al método DLS comenzando desde el nodo 'A'
