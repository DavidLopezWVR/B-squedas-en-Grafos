#21110344  David López Rojas  6E2

class DecisionNode:
    def __init__(self, name, probabilities, children=None):
        # Inicializa un nodo de decisión con un nombre, una lista de probabilidades y una lista de nodos hijos
        self.name = name
        self.probabilities = probabilities  # Probabilidades asociadas a las decisiones del nodo
        self.children = children if children else []  # Inicializa los hijos; si no hay, es una lista vacía

class DecisionTree:
    def __init__(self):
        # Inicializa el árbol de decisión sin un nodo raíz
        self.root = None

    def add_node(self, parent_name, node):
        # Agrega un nodo al árbol, conectándolo a su nodo padre
        if not self.root:
            # Si el árbol está vacío, el nodo se convierte en la raíz
            self.root = node
        else:
            # Busca el nodo padre en el árbol
            parent_node = self._find_node(self.root, parent_name)
            if parent_node:
                # Si se encuentra el nodo padre, agrega el nuevo nodo como hijo
                parent_node.children.append(node)
            else:
                # Si no se encuentra el nodo padre, imprime un mensaje de error
                print("Parent node not found.")

    def _find_node(self, current_node, name):
        # Busca un nodo por su nombre de forma recursiva
        if current_node.name == name:
            return current_node  # Retorna el nodo si se encuentra
        for child in current_node.children:
            result = self._find_node(child, name)  # Busca en los hijos
            if result:
                return result  # Retorna el nodo encontrado
        return None  # Retorna None si no se encuentra el nodo

    def expected_value(self, node):
        # Calcula el valor esperado a partir de un nodo dado
        if not node.children:
            return 0  # Retorna 0 si el nodo no tiene hijos (nodo final)
        else:
            expected_value = 0  # Inicializa el valor esperado
            # Calcula el valor esperado sumando las probabilidades multiplicadas por el valor esperado de los hijos
            for i, child in enumerate(node.children):
                expected_value += node.probabilities[i] * self.expected_value(child)
            return expected_value  # Retorna el valor esperado calculado

# Ejemplo de uso
root_node = DecisionNode("Inicio", [0, 0])  # Nodo raíz con probabilidades iniciales no relevantes
decision_tree = DecisionTree()  # Crea una instancia del árbol de decisión

# Define los nodos de la red de decisión con sus probabilidades
distribuidor_node = DecisionNode("Distribuidor", [0.7, 0.3])
compra_mayorista_node = DecisionNode("Compra a Mayorista", [0.9, 0.1])
compra_minorista_node = DecisionNode("Compra a Minorista", [0.2, 0.8])
venta_mayorista_node = DecisionNode("Venta (Mayorista)", [0.6, 0.4])
venta_minorista_node = DecisionNode("Venta (Minorista)", [0.8, 0.2])

# Agregar nodos a la red de decisión
decision_tree.add_node("Inicio", distribuidor_node)
decision_tree.add_node("Distribuidor", compra_mayorista_node)
decision_tree.add_node("Distribuidor", compra_minorista_node)
decision_tree.add_node("Compra a Mayorista", venta_mayorista_node)
decision_tree.add_node("Compra a Minorista", venta_minorista_node)

# Calcular el valor esperado a partir del nodo raíz
expected_value = decision_tree.expected_value(root_node)
print("Valor esperado:", expected_value)  # Imprime el valor esperado calculado
