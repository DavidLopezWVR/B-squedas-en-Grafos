# 21110344  David López Rojas    6E2

import math

# Clase que representa un grafo
class Graph:
    def __init__(self, graph_dict=None):
        # Inicializa el diccionario del grafo como un diccionario de diccionarios
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict  # Almacena el diccionario de adyacencia del grafo

    # Método para agregar una arista entre un nodo y su vecino con una distancia
    def add_edge(self, node, neighbor, distance):
        # Si el nodo no está en el diccionario, se inicializa con un diccionario vacío
        if node not in self.graph_dict:
            self.graph_dict[node] = {}
        # Agrega el vecino y la distancia a la lista de adyacencia del nodo
        self.graph_dict[node][neighbor] = distance

# Función heurística para la búsqueda A*
def heuristic(node, goal):
    # Calcula la distancia euclidiana entre el nodo actual y el objetivo
    x1, y1 = node
    x2, y2 = goal
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Implementación del algoritmo A* para la búsqueda de caminos
def a_star(graph, start, goal):
    open_set = {start}  # Conjunto de nodos a explorar
    closed_set = set()  # Conjunto de nodos ya explorados
    # Diccionario para almacenar la distancia mínima desde el inicio a cada nodo
    g_score = {node: float('inf') for node in graph.graph_dict}
    g_score[start] = 0  # La distancia al nodo inicial es 0

    # Diccionario para almacenar la función f(n) = g(n) + h(n)
    f_score = {node: float('inf') for node in graph.graph_dict}
    f_score[start] = heuristic(start, goal)  # Estimación inicial de f(n) usando la heurística

    # Bucle principal del algoritmo
    while open_set:
        # Selecciona el nodo en open_set con el menor valor de f(n)
        current = min(open_set, key=lambda node: f_score[node])

        # Si se alcanza el nodo objetivo, se encontró un camino
        if current == goal:
            return True

        # Mueve el nodo actual de open_set a closed_set
        open_set.remove(current)
        closed_set.add(current)

        # Explora cada vecino del nodo actual
        for neighbor, distance in graph.graph_dict[current].items():
            # Calcula el g(n) tentativo desde el nodo actual hasta el vecino
            tentative_g_score = g_score[current] + distance

            # Si el g(n) tentativo es mejor, actualiza g_score y f_score para el vecino
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                # Si el vecino no ha sido completamente explorado, lo añade a open_set
                if neighbor not in closed_set:
                    open_set.add(neighbor)

    # Si se sale del bucle sin encontrar el objetivo, no hay camino
    return False

# Ejemplo de uso de la clase Graph y el algoritmo A*
graph = Graph({
    (0, 0): {(0, 1): 1, (1, 0): 1},  # Nodo (0, 0) conectado a (0, 1) y (1, 0)
    (0, 1): {(0, 0): 1, (1, 1): 1},  # Nodo (0, 1) conectado a (0, 0) y (1, 1)
    (1, 0): {(0, 0): 1, (1, 1): 1},  # Nodo (1, 0) conectado a (0, 0) y (1, 1)
    (1, 1): {(0, 1): 1, (1, 0): 1}   # Nodo (1, 1) conectado a (0, 1) y (1, 0)
})

start_node = (0, 0)  # Nodo inicial
goal_node = (1, 1)   # Nodo objetivo
result = a_star(graph, start_node, goal_node)  # Ejecuta el algoritmo A* para encontrar el camino
print("¿Se encontró un camino al objetivo?", result)
