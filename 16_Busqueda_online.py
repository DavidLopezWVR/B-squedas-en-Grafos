#  21110344  David López Rojas   6E2

import random  # Importa la biblioteca random para generar movimientos aleatorios

class OnlineSearchAgent:
    def __init__(self):
        self.current_position = (0, 0)  # Inicializa la posición del agente en la esquina superior izquierda del laberinto

    def move(self, maze):
        # Método para mover al agente dentro del laberinto
        possible_moves = maze.get_possible_moves(self.current_position)  # Obtiene los movimientos posibles desde la posición actual
        if possible_moves:
            next_move = random.choice(possible_moves)  # Selecciona un movimiento aleatorio de los posibles
            self.current_position = next_move  # Actualiza la posición del agente
            return next_move  # Retorna el nuevo movimiento
        else:
            return None  # Si no hay movimientos posibles, retorna None

class Maze:
    def __init__(self, width, height):
        self.width = width  # Ancho del laberinto
        self.height = height  # Alto del laberinto
        self.obstacles = set()  # Conjunto para almacenar posiciones de obstáculos

    def add_obstacle(self, position):
        # Método para agregar un obstáculo en una posición específica
        self.obstacles.add(position)  # Agrega la posición al conjunto de obstáculos

    def get_possible_moves(self, position):
        # Método que devuelve una lista de movimientos posibles desde una posición dada
        possible_moves = []  # Inicializa la lista de movimientos posibles
        x, y = position  # Descompone la posición actual en coordenadas x e y
        for dx in [-1, 0, 1]:  # Itera sobre posibles desplazamientos en x
            for dy in [-1, 0, 1]:  # Itera sobre posibles desplazamientos en y
                new_x, new_y = x + dx, y + dy  # Calcula nuevas coordenadas
                # Verifica si la nueva posición es válida: no debe ser un obstáculo y debe estar dentro de los límites
                if (new_x, new_y) not in self.obstacles and 0 <= new_x < self.width and 0 <= new_y < self.height:
                    possible_moves.append((new_x, new_y))  # Agrega la nueva posición a la lista de movimientos posibles
        return possible_moves  # Retorna la lista de movimientos válidos

# Ejemplo de uso
maze = Maze(10, 10)  # Crea un laberinto de 10x10
# Agrega obstáculos en posiciones específicas
maze.add_obstacle((1, 1))
maze.add_obstacle((2, 2))
maze.add_obstacle((3, 3))
maze.add_obstacle((4, 4))

agent = OnlineSearchAgent()  # Crea un agente de búsqueda en línea
for _ in range(20):  # Permite al agente intentar moverse hasta 20 veces
    next_move = agent.move(maze)  # Intenta mover al agente
    if next_move:
        print("El agente se mueve a la posición:", next_move)  # Imprime la nueva posición si se movió
    else:
        print("El agente no puede moverse más, ha alcanzado un callejón sin salida.")  # Imprime un mensaje si no puede moverse
        break  # Termina el bucle si el agente no puede moverse más
