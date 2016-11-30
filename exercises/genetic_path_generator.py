from exercises.problem_generation import create_problem
from exercises.graph import Graph


def fitness(list1):
    """create_problem makes nodes and edges"""
    g = create_problem()
    cost = 0
    """check if lists exists"""
    if list1 == None:
        return False
    """check which path is cheaper"""
    for item in list1:
        i+=1
        """get the cost of path 1"""
        cost += g.get_edge_value(item, list1[i])
    return cost

def selection():
    pass

def mutation():
    pass
