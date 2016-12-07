from exercises.graph import Graph

def add_nodes():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')
    g.add_vertex('G')
    g.add_vertex('H')
    g.add_edge('A', 'B')
    g.add_edge('B', 'A')
    g.add_edge('B', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'B')
    g.add_edge('C', 'E')
    g.add_edge('D', 'B')
    g.add_edge('D', 'E')
    g.add_edge('D', 'G')
    g.add_edge('E', 'C')
    g.add_edge('E', 'D')
    g.add_edge('E', 'F')
    g.add_edge('F', 'E')
    g.add_edge('F', 'H')
    g.add_edge('G', 'D')
    g.add_edge('G', 'H')
    g.add_edge('H', 'F')
    g.add_edge('H', 'G')
    g.add_nodes['A'] = [('B', 3)]
    g.add_nodes['B'] = [('A', 3)]
    g.add_nodes['B'] = [('C', 2)]
    g.add_nodes['B'] = [('D', 2)]
    g.add_nodes['C'] = [('B', 2)]
    g.add_nodes['C'] = [('E', 1)]
    g.add_nodes['D'] = [('B', 2)]
    g.add_nodes['D'] = [('E', 2)]
    g.add_nodes['D'] = [('G', 4)]
    g.add_nodes['E'] = [('C', 1)]
    g.add_nodes['E'] = [('D', 2)]
    g.add_nodes['E'] = [('F', 3)]
    g.add_nodes['F'] = [('E', 3)]
    g.add_nodes['F'] = [('H', 3)]
    g.add_nodes['G'] = [('D', 4)]
    g.add_nodes['G'] = [('H', 3)]
    g.add_nodes['H'] = [('F', 3)]
    g.add_nodes['H'] = [('G', 3)]
