from exercises.graph import Graph
import logging

logger = logging.getLogger(__name__)


def create_problem():
    logger.debug('Creating problem graph.')

    g = Graph()

    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')
    g.add_vertex('G')
    g.add_vertex('H')

    g.add_edge('A', 'B', 3)
    g.add_edge('A', 'C', 4)
    g.add_edge('A', 'F', 2)
    g.add_edge('B', 'A', 3)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 2)
    g.add_edge('C', 'A', 4)
    g.add_edge('C', 'B', 2)
    g.add_edge('D', 'B', 2)
    g.add_edge('C', 'E', 1)
    g.add_edge('E', 'C', 1)
    g.add_edge('D', 'E', 2)
    g.add_edge('E', 'D', 2)
    g.add_edge('E', 'F', 3)
    g.add_edge('F', 'E', 3)
    g.add_edge('F', 'H', 3)
    g.add_edge('H', 'F', 3)
    g.add_edge('G', 'D', 4)
    g.add_edge('D', 'G', 4)
    g.add_edge('G', 'H', 3)
    g.add_edge('H', 'G', 3)
    g.add_edge('H', 'G', 3)
    g.add_edge('F', 'A', 2)
    g.add_edge('G', 'H', 3)
    g.add_edge('D', 'G', 4)
    g.add_edge('G', 'D', 4)
    return g
