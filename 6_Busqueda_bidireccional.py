# 21110344   David López Rojas 6E2

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

    # Método de búsqueda bidireccional
    def bidirectional_search(self, start, goal):
        # Colas para la búsqueda desde el inicio y desde el objetivo
        queue_start = [start]  # Cola para la búsqueda desde el nodo de inicio
        queue_goal = [goal]    # Cola para la búsqueda desde el nodo objetivo
        # Conjuntos para llevar el seguimiento de los nodos visitados desde cada dirección
        visited_start = set([start])  # Nodos visitados desde el inicio
        visited_goal = set([goal])    # Nodos visitados desde el objetivo

        # Mientras ambas colas tengan elementos para explorar
        while queue_start and queue_goal:
            # Expande el siguiente nodo desde el inicio
            current_start = queue_start.pop(0)
            print("Desde el inicio:", current_start)
            # Verifica si el nodo actual se ha alcanzado desde el objetivo
            if current_start in visited_goal:
                return True  # Camino encontrado al encontrarse ambas búsquedas
            # Explora los vecinos del nodo actual
            for neighbor in self.graph_dict.get(current_start, []):
                # Si el vecino no ha sido visitado, lo marca y lo añade a la cola
                if neighbor not in visited_start:
                    visited_start.add(neighbor)
                    queue_start.append(neighbor)

            # Expande el siguiente nodo desde el objetivo
            current_goal = queue_goal.pop(0)
            print("Desde el objetivo:", current_goal)
            # Verifica si el nodo actual se ha alcanzado desde el inicio
            if current_goal in visited_start:
                return True  # Camino encontrado al encontrarse ambas búsquedas
            # Explora los vecinos del nodo actual
            for neighbor in self.graph_dict.get(current_goal, []):
                # Si el vecino no ha sido visitado, lo marca y lo añade a la cola
                if neighbor not in visited_goal:
                    visited_goal.add(neighbor)
                    queue_goal.append(neighbor)

        # Si se terminan los nodos por explorar sin encontrar el objetivo, retorna False
        return False

# Ejemplo de uso de la clase Graph y del método de búsqueda bidireccional
graph = Graph({
    'A': ['B', 'C'],  # Nodo 'A' conectado a 'B' y 'C'
    'B': ['D', 'E'],  # Nodo 'B' conectado a 'D' y 'E'
    'C': ['F'],       # Nodo 'C' conectado a 'F'
    'D': [],          # Nodo 'D' no tiene conexiones
    'E': ['F'],       # Nodo 'E' conectado a 'F'
    'F': []           # Nodo 'F' no tiene conexiones
})

start_node = 'A'  # Nodo de inicio para la búsqueda bidireccional
goal_node = 'F'   # Nodo objetivo
print("Búsqueda bidireccional:")
result = graph.bidirectional_search(start_node, goal_node)  # Ejecuta la búsqueda bidireccional
print("Se encontró un camino entre el nodo inicial y el objetivo:", result)
