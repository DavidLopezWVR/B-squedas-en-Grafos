#  21110344  David López Rojas  6E2

import networkx as nx

def cut_conditioning(graph):
    # Inicializa el conjunto del mejor corte encontrado y el tamaño máximo del corte
    best_cut = set()
    max_cut_size = 0

    # Bucle principal que continúa mientras se encuentren cortes más grandes
    while True:
        cut_found = False  # Indicador para verificar si se encontró un mejor corte en esta iteración
        
        # Recorre cada arista del grafo para evaluar posibles cortes
        for edge in graph.edges():
            # Crea un conjunto de nodos del corte basado en la arista actual
            cut = set(edge)
            # Calcula el tamaño del corte actual usando la función cut_size de NetworkX
            cut_size = nx.cut_size(graph, cut)
            
            # Si el tamaño del corte actual es mayor que el máximo registrado, actualiza el mejor corte
            if cut_size > max_cut_size:
                max_cut_size = cut_size  # Actualiza el tamaño máximo del corte
                best_cut = cut  # Almacena el conjunto de nodos del mejor corte encontrado
                cut_found = True  # Marca que se encontró un nuevo corte
        
        # Si no se encontró un mejor corte en esta iteración, termina el bucle
        if not cut_found:
            break

        # Elimina los nodos del mejor corte encontrado del grafo para reducir su tamaño
        for node in best_cut:
            graph.remove_node(node)

    # Retorna el tamaño máximo del corte encontrado
    return max_cut_size

# Ejemplo de uso
# Crea un grafo y añade aristas
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)])

# Calcula el tamaño inicial de un corte especificado
initial_cut_size = nx.cut_size(G, {(0, 1), (2, 3)})
print("Tamaño inicial del corte:", initial_cut_size)

# Ejecuta la función de corte condicionado y muestra el resultado
cut_size = cut_conditioning(G)
print("Tamaño del corte después del acondicionamiento:", cut_size)
