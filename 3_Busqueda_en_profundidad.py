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

    # Método de búsqueda en profundidad (DFS) recursiva
    def dfs(self, start, visited=None):
        # Inicializa el conjunto de nodos visitados si es la primera llamada
        if visited is None:
            visited = set()
        # Marca el nodo inicial como visitado
        visited.add(start)
        # Imprime el nodo actual
        print(start)
        # Recorre los vecinos del nodo actual
        for neighbor in self.graph_dict.get(start, []):
            # Si el vecino no ha sido visitado, llama recursivamente a dfs en el vecino
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Ejemplo de uso de la clase Graph y del método DFS
graph = Graph({
    'A': ['B', 'C'],  # Nodo 'A' conectado a 'B' y 'C'
    'B': ['D', 'E'],  # Nodo 'B' conectado a 'D' y 'E'
    'C': ['F'],       # Nodo 'C' conectado a 'F'
    'D': [],          # Nodo 'D' no tiene conexiones
    'E': ['F'],       # Nodo 'E' conectado a 'F'
    'F': []           # Nodo 'F' no tiene conexiones
})

start_node = 'A'  # Nodo de inicio para el recorrido DFS
print("Recorrido DFS:")
graph.dfs(start_node)  # Llama al método DFS comenzando desde el nodo 'A'
