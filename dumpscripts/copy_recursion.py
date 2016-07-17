# copy_recursion.py

import copy


class Graph:

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return 'Graph(name={}, id={})'.format(
            self.name, id(self))

    def __deepcopy__(self, memo):
        print('\nChiamata di __deepcopy__ per {!r}'.format(self))
        if self in memo:
            existing = memo.get(self)
            print('  Già copiato in {!r}'.format(existing))
            return existing
        print('  Dizionario Memo:')
        if memo:
            for k, v in memo.items():
                print('    {}: {}'.format(k, v))
        else:
            print('    (vuoto)')
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print('  In copia al nuovo oggetto {}'.format(dup))
        memo[self] = dup
        for c in self.connections:
            dup.add_connection(copy.deepcopy(c, memo))
        return dup


root = Graph('root', [])
a = Graph('a', [root])
b = Graph('b', [a, root])
root.add_connection(a)
root.add_connection(b)

dup = copy.deepcopy(root)
