"""Implementation av ADTn graph."""


class Graph():
    """Implementation av ADTn Graph med metoden `Adjacency list`.

    En dictionary, `self._nodes`, används för att lagra alla noder och kanter.
    En node är en nyckel i `self._nodes` och dess kanter representeras av en
    lista med parvisa tupler.

    En graf med noderna `a`, `b` och `c` och kanter mellan alla tre skulle
    representeras som nedan.

    self._nodes = {'a': [('b', 4), ('c', 2)],
                   'b': [('a', 4), ('c', 5)],
                   'c': [('a', 2), ('b', 5)]}
    """

    def __init__(self):
        """Initiera `self._nodes`."""
        self._nodes = {}

    def neighbours(self, key):
        """Returnera alla grannar till `key`."""
        return [key for key, value in self._nodes[key]]

    def add_vertex(self, key):
        """Lägg till en ny nod."""
        self._nodes[key] = []

    def get_vertices(self):
        """Returnera grafens alla noder."""
        return self._nodes.keys()

    def add_edge(self, x, y, value = None):
        """Lägg till en kant från `x` till `y`."""
        self._nodes[x].append((y, value))

    def is_adjacent(self, x, y):
        """Kontrollera om `x` och `y` är grannar."""
        if x not in self._nodes:
            return False
        return y in [t[0] for t in self._nodes[x]]

    def set_edge_value(self, x, y, value):
        """Sätt värde för kanten mellan `x` och `y`."""
        self._nodes[x] = [(y, value)]

    def get_edge_value(self, x, y):
        """Returnera värde för kanten mellan `x` och `y`."""
        if x not in self._nodes:
            raise KeyError
        for key, value in self._nodes[x]:
            if key == y:
                return value
        raise KeyError

    def __contains__(self, key):
        """Kontrollera om noden med matchande `key` finns."""
        return key in self._nodes

    def __iter__(self):
        """Gör det enkelt att iterera över grafens alla noders namn."""
        return iter([t[0] for t in self._nodes[x]])
