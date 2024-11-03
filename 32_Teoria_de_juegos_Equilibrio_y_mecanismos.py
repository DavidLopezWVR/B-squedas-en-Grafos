#21110344  David López Rojas  6E2

import numpy as np  # Importar la biblioteca NumPy para operaciones numéricas
import nashpy as nash  # Importar la biblioteca Nashpy para el análisis de juegos no cooperativos

# Definir las matrices de pago del juego
payoff_player1 = np.array([[3, 2], [0, 1]])  # Matriz de pagos para el jugador 1
payoff_player2 = np.array([[3, 0], [2, 1]])  # Matriz de pagos para el jugador 2

# Crear el juego
game = nash.Game(payoff_player1, payoff_player2)  # Instanciar el objeto de juego con las matrices de pago

# Encontrar el equilibrio de Nash
equilibria = game.support_enumeration()  # Utilizar el método de enumeración de soportes para encontrar los equilibrios de Nash
for eq in equilibria:  # Iterar sobre los equilibrios encontrados
    print("Equilibrio de Nash:", eq)  # Imprimir cada equilibrio de Nash encontrado
