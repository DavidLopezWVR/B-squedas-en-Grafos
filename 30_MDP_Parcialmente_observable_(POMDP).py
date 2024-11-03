#21110344  David López Rojas  6E2

from pomdp_py import POMDP, BeliefState, DiscreteSpace, DiscreteDistribution

# Definir los estados, acciones, observaciones y recompensas
states = ['S0', 'S1', 'S2']  # Lista de estados posibles en el POMDP
actions = ['A0', 'A1']  # Lista de acciones posibles que el agente puede tomar
observations = ['O0', 'O1']  # Lista de observaciones que el agente puede recibir

# Definición de recompensas asociadas a cada estado-acción
rewards = {
    ('S0', 'A0'): {'S0': 0, 'S1': 0, 'S2': 0},  # Recompensas cuando se toma A0 en S0
    ('S0', 'A1'): {'S0': 0, 'S1': 0, 'S2': 0},  # Recompensas cuando se toma A1 en S0
    ('S1', 'A0'): {'S0': 0, 'S1': 1, 'S2': 0},  # Recompensas cuando se toma A0 en S1
    ('S1', 'A1'): {'S0': 0, 'S1': 0, 'S2': 1},  # Recompensas cuando se toma A1 en S1
    ('S2', 'A0'): {'S0': 0, 'S1': 0, 'S2': 0},  # Recompensas cuando se toma A0 en S2
    ('S2', 'A1'): {'S0': 0, 'S1': 0, 'S2': 0}   # Recompensas cuando se toma A1 en S2
}

# Definición de las probabilidades de transición entre estados para cada acción
transitions = {
    ('S0', 'A0'): {'S0': 0.8, 'S1': 0.1, 'S2': 0.1},  # Probabilidades de transición al tomar A0 en S0
    ('S0', 'A1'): {'S0': 0.1, 'S1': 0.8, 'S2': 0.1},  # Probabilidades de transición al tomar A1 en S0
    ('S1', 'A0'): {'S0': 0.1, 'S1': 0.8, 'S2': 0.1},  # Probabilidades de transición al tomar A0 en S1
    ('S1', 'A1'): {'S0': 0.1, 'S1': 0.1, 'S2': 0.8},  # Probabilidades de transición al tomar A1 en S1
    ('S2', 'A0'): {'S0': 0.1, 'S1': 0.1, 'S2': 0.8},  # Probabilidades de transición al tomar A0 en S2
    ('S2', 'A1'): {'S0': 0.8, 'S1': 0.1, 'S2': 0.1}   # Probabilidades de transición al tomar A1 en S2
}

# Definición de las probabilidades de observación para cada acción y estado
observations_prob = {
    ('S0', 'A0'): {'O0': 0.8, 'O1': 0.2},  # Probabilidades de observar O0 y O1 al tomar A0 en S0
    ('S0', 'A1'): {'O0': 0.2, 'O1': 0.8},  # Probabilidades de observar O0 y O1 al tomar A1 en S0
    ('S1', 'A0'): {'O0': 0.2, 'O1': 0.8},  # Probabilidades de observar O0 y O1 al tomar A0 en S1
    ('S1', 'A1'): {'O0': 0.8, 'O1': 0.2},  # Probabilidades de observar O0 y O1 al tomar A1 en S1
    ('S2', 'A0'): {'O0': 0.8, 'O1': 0.2},  # Probabilidades de observar O0 y O1 al tomar A0 en S2
    ('S2', 'A1'): {'O0': 0.2, 'O1': 0.8}   # Probabilidades de observar O0 y O1 al tomar A1 en S2
}

# Definir el POMDP utilizando los estados, acciones, observaciones, recompensas, transiciones y probabilidades de observación
pomdp = POMDP(states, actions, observations, rewards, transitions, observations_prob)

# Crear un estado de creencia inicial uniforme
belief_space = DiscreteSpace(states)  # Espacio de creencia discreto basado en los estados definidos
# Inicializa el estado de creencia con probabilidades uniformes para cada estado
initial_belief = BeliefState({s: 1/len(states) for s in states}, belief_space)

# Ejecutar la planificación POMDP para encontrar la política óptima
policy = pomdp.solve(100, initial_belief)  # Resuelve el POMDP con un límite de iteraciones (100) y el estado de creencia inicial

# Imprimir la política óptima resultante
print("Política óptima:")
print(policy)  # Muestra la política óptima que el agente debe seguir
