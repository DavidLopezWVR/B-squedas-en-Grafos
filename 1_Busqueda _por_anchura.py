# David Lopez Rojas  reg 21110344

from collections import deque  # Importa deque, una estructura de datos de doble extremo que se usa como cola

# Definición de un grafo como un diccionario de listas de adyacencia
graph = {
    'A': ['B', 'C'],  # Nodo 'A' está conectado a 'B' y 'C'
    'B': ['D', 'E'],  # Nodo 'B' está conectado a 'D' y 'E'
    'C': ['F'],       # Nodo 'C' está conectado a 'F'
    'D': [],          # Nodo 'D' no tiene conexiones
    'E': ['F'],       # Nodo 'E' está conectado a 'F'
    'F': []           # Nodo 'F' no tiene conexiones
}

def bfs(graph, start):
    # Inicializa un conjunto para llevar un registro de los nodos visitados
    visited = set()
    # Inicializa la cola con el nodo de inicio
    queue = deque([start])
    # Marca el nodo de inicio como visitado
    visited.add(start)
    
    # Mientras la cola no esté vacía
    while queue:
        # Saca el primer nodo de la cola y lo guarda en la variable 'vertex'
        vertex = queue.popleft()
        # Imprime el nodo actual
        print(vertex, end=' ')
        
        # Recorre los vecinos del nodo actual
        for neighbor in graph[vertex]:
            # Si el vecino no ha sido visitado
            if neighbor not in visited:
                # Agrega el vecino a la cola para visitarlo más tarde
                queue.append(neighbor)
                # Marca el vecino como visitado
                visited.add(neighbor)

# Ejemplo de uso del algoritmo BFS
print("Recorrido en anchura empezando desde el vértice 'A':")
bfs(graph, 'A')  # Llama a la función BFS comenzando desde el nodo 'A'

