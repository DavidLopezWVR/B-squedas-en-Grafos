#21110344  David López Rojas  6E2

from pgmpy.models import DynamicBayesianNetwork as DBN  # Importar la clase para crear redes bayesianas dinámicas
from pgmpy.factors.discrete import TabularCPD  # Importar la clase para definir distribuciones de probabilidad condicionales
from pgmpy.inference import DBNInference  # Importar la clase para realizar inferencia en redes bayesianas dinámicas

# Definir la estructura de la DBN
dbn = DBN()  # Crear una instancia de la Red Bayesiana Dinámica

# Definir los nodos y las conexiones temporales
# Aquí se añaden las aristas que indican las relaciones temporales entre los nodos
dbn.add_edges_from([(('X', 0), ('X', 1)), (('X', 1), ('X', 2))])  # Conectar el estado X en el tiempo 0 con X en el tiempo 1, y X en el tiempo 1 con X en el tiempo 2

# Definir las distribuciones condicionales temporales (CPDs) para los nodos
cpd_x0 = TabularCPD(('X', 0), 2, [[0.6], [0.4]])  # Distribución de probabilidad para X en el tiempo 0
cpd_x1 = TabularCPD(('X', 1), 2, [[0.3, 0.7], [0.7, 0.3]], evidence=[('X', 0)], evidence_card=[2])  # CPD para X en el tiempo 1, dado X en el tiempo 0
cpd_x2 = TabularCPD(('X', 2), 2, [[0.2, 0.8], [0.8, 0.2]], evidence=[('X', 1)], evidence_card=[2])  # CPD para X en el tiempo 2, dado X en el tiempo 1

# Agregar las distribuciones condicionales temporales a la DBN
dbn.add_cpds(cpd_x0, cpd_x1, cpd_x2)  # Añadir los CPDs a la red

# Verificar si la DBN es válida
print("¿Es válida la DBN?", dbn.check_model())  # Comprobar la validez del modelo y mostrar el resultado

# Realizar inferencia en la DBN
inference = DBNInference(dbn)  # Crear un objeto de inferencia para la DBN
result = inference.query(variables=[('X', 2)], evidence={('X', 0): 1})  # Realizar una consulta para obtener la probabilidad de X en el tiempo 2 dado que X en el tiempo 0 es 1
print("Probabilidad de X en el tiempo 2 dado X en el tiempo 0 igual a 1:", result)  # Mostrar el resultado de la inferencia
