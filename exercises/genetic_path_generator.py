from exercises.problem_generation import create_problem
from exercises.graph import Graph
from exercises.problem import *
import logging

logger = logging.getLogger(__name__)


POPULATION_AMOUNT = 100
SELECTION_AMOUNT = 80

def pop_generator(g):
    logger.info('Generating initial population.')
    all_nodes = g.get_vertices()
    population = []
    for x in range(POPULATION_AMOUNT):
        individual = {'path':random.sample(all_nodes, len(all_nodes))}
        individual['cost'] = fitness(g, individual['path'])
        if individual['cost']:
            population.append(individual)
        logger.debug('Adding [{}, ...] with fitness value of {} to population' \
            .format(', '.join(individual['path'][:5]), individual['cost']))
    return list(population)

def fitness(g, solution):
    """create_problem makes nodes and edges"""
    """check if lists exists"""
    try:
        cost = 0
        i = 0
        for item in solution:
            if i < len(solution)-1:
                i += 1
            else:
                i = 0
            """get the cost of the path"""
            cost += g.get_edge_value(item, solution[i])
        return cost
    except KeyError as e:
        return None


def selection(g, population):
    # Rensa ut de sämsta individerna
    population = sorted(population, key=lambda individual: individual['cost'])
    population = population[:SELECTION_AMOUNT]

    # Fyll på med nya individer
    for i in range(POPULATION_AMOUNT - len(g)):
        # Generera en ny individ.
    

    return g

def mutation():
    pass
