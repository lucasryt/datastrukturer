#!/usr/bin/env python3
import click
from exercises.problem_generation import create_problem
from exercises.genetic_path_generator import *
from exercises.problem import generate
import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


@click.command()
@click.option('--checkfit', is_flag=True)
def tests(checkfit):
    if checkfit:
        problem = create_problem()
        problem = generate(5, 5)

        population = pop_generator(problem)
        best_kid = population[0]  # Best of initial population
        generation = 1
        while True:
            generation += 1
            click.echo('At generation {} with best cost of best soulution at {}.'.format(generation, best_kid['cost']))
            population = selection(problem, population, generation)
            if population[0]['cost'] < best_kid['cost']:
                best_kid = population[0]
                logger.info('Replacing best solution with\n{}'.format(best_kid))
            if best_kid['gen'] < generation - 10:
                break

            click.echo('10 best solutions:')
            for i in range(10):
                click.echo(population[i])


        click.echo('Best solution is \n{path}\n with cost {cost}.'.format(**best_kid))
        click.echo('Ended at generation {}.'.format(generation))

        # list1 = ['A', 'B', 'C', 'E', 'D', 'G', 'H', 'F']
        # cost = fitness(problem, list1)
        # click.echo(cost)

if __name__ == '__main__':
    tests()
