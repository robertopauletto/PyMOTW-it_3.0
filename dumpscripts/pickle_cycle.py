# pickle_cycle.py

import pickle


class Node:
    """Un semplice digrafo
    """
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_edge(self, node):
        "Crea un collegamento tra questo nodo e gli altri."
        self.connections.append(node)

    def __iter__(self):
        return iter(self.connections)


def preorder_traversal(root, seen=None, parent=None):
    """Generatore che fornisce i collegamenti in un grafo.
    """
    if seen is None:
        seen = set()
    yield (parent, root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        recurse = preorder_traversal(node, seen, root)
        for parent, subnode in recurse:
            yield (parent, subnode)


def show_edges(root):
    "Stampa tutti i collegamenti nel grafo."
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print('{:>5} -> {:>2} ({})'.format(
            parent.name, child.name, id(child)))


# Imposta i nodi.
root = Node('root')
a = Node('a')
b = Node('b')
c = Node('c')

# Aggiunge i collegamenti tra i nodi.
root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
a.add_edge(a)

print('GRAFO ORIGINALE :')
show_edges(root)

# Serializza e deserializza il grafo per creare
# un nuovo insieme di nodi.
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print('\nGRAFO RICARICATO:')
show_edges(reloaded)
