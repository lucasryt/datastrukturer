from exercises.problem_generation import create_problem
from exercises.graph import Graph
from exercises.problem import *
import logging


logger = logging.getLogger(__name__)

POPULATION_AMOUNT = 1000
SELECTION_AMOUNT = 500
MUTATION_AMOUNT = 100


def pop_generator(g):
    logger.info('Generating initial population.')
    all_nodes = g.get_vertices()
    population = []
    for x in range(POPULATION_AMOUNT):
        individual = {'path':random.sample(all_nodes, len(all_nodes))}
        individual['cost'] = fitness(g, individual['path'])
        individual['gen'] = 1
        if individual['cost']:
            population.append(individual)
        logger.debug('Adding [{}, ...] with fitness value of {} to population' \
            .format(', '.join(individual['path'][:5]), individual['cost']))
    population = sorted(list(population), key=lambda individual: individual['cost'])
    return population

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


def selection(g, population, generation):
    logger.info('Performing selection...')
    # Rensa ut de sämsta individerna
    population = population[:SELECTION_AMOUNT]
    # Fyll på med nya individer
    for i in range(POPULATION_AMOUNT - len(population)):
        # Generera en ny individ.
        parent = random.choice(population)  # Funkar inte som förväntat!
        pizza_slice = random.randint(1, len(parent['path'])-1)
        child_path = parent['path'][pizza_slice:] + parent['path'][:pizza_slice]
        if random.randint(1, MUTATION_AMOUNT) == 1:
            logger.debug('Mutating')
            child_path = mutation(child_path)
        child = {'path': child_path, 'cost': fitness(g, child_path), 'gen': generation}
        population.append(child)
        #logger.debug('Added individual [{}, ...] with cost {} to population.'.format(', '.join(child['path'][:5]), child['cost']))
    population = sorted(population, key=lambda individual: individual['cost'])
    return population

def mutation(path):
    x = random.randint(1, len(path)-1)
    y = random.randint(1, len(path)-1)
    path[x], path[y] = path[y], path[x]
    logger.debug('{0} mutated ({1} and {2} swapped).'.format(path, x, y))
    return path
