import pytest
from exercises.graph import Graph

def test_add_vertex_exists():
    g = Graph()
    assert hasattr(g, 'add_vertex')


def test_add_vertex():
    g = Graph()
    g.add_vertex('A')
    assert g._nodes['A'] == [] #Forsök undvika detta!


def test_add_and_list_vertices():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    assert sorted(g.get_vertices()) == ['A', 'B']
    g.add_vertex('C')
    assert sorted(g.get_vertices()) == ['A', 'B', 'C']


def test_add_edge():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_edge('A', 'B')
    assert g._nodes['A'] == [('B', None)]
    g.add_edge('B', 'A', 7)
    assert g._nodes['B'] == [('A', 7)]


def test_is_adjacent():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_edge('A', 'B')
    assert g.is_adjacent ('A', 'B')
    assert g.is_adjacent ('B', 'A') is False
    assert g.is_adjacent ('A', 'C') is False
    assert g.is_adjacent ('C', 'A') is False


def test_set_edge_value():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_edge('A', 'B')
    assert g._nodes['A'] == [('B', None)]
    assert g._nodes['B'] == []
    g.set_edge_value('A', 'B', 7)
    assert g._nodes['A'] == [('B', 7)]
    assert g._nodes['B'] == []


def test_get_edge_value_that_doesnt_exist():
    with pytest.raises(KeyError):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_edge('A', 'B')
        g.get_edge_value('C', 'D')  # Expected to throw KeyError


def test__contains__():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    assert g.__contains__ ('A')
    assert g.__contains__ ('B')
    assert g.__contains__ ('C') is False
    assert g.__contains__ ('H') is False


def test__iter__():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    assert next(g.__iter__)
