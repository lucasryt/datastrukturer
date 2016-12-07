from exercises.problem_generation import create_problem
from exercises.graph import Graph
from exercises.problem import *
import logging


def selection():
    pass


logger = logging.getLogger(__name__)

POPULATION_AMOUNT = 100
SELECTION_AMOUNT = 80
MUTATION_AMOUNT = 1000

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
    logger.info('Performing selection...')
    # Rensa ut de sämsta individerna
    logger.info('Generating initial population.')
    population = sorted(population, key=lambda individual: individual['cost'])
    population = population[:SELECTION_AMOUNT]

    # Fyll på med nya individer
    for i in range(POPULATION_AMOUNT - len(population)):
        # Generera en ny individ.
        parent = random.choice(population)
        pizza_slice = random.randint(1, len(parent['path'])-1)
        child_path = parent['path'][pizza_slice:] + parent['path'][:pizza_slice]
        if random.randint(1, MUTATION_AMOUNT) == 1:
            logger.debug('Mutating')
            child_path = mutation(child_path)
        child = {'path': child_path, 'cost': fitness(g, child_path)}
        population.append(child)
        logger.debug('Added individual [{}, ...] with cost {} to population.'.format(', '.join(child['path'][:5]), child['cost']))
    return population

def mutation(path):
    x = random.randint(1, len(path)-1)
    y = random.randint(1, len(path)-1)
    path[x], path[y] = path[y], path[x]
    logger.debug('{0} mutated ({1} and {2} swapped).'.format(path, x, y))
    return path
