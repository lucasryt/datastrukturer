#!/usr/bin/env python3
import click
from exercises.problem_generation import create_problem
from exercises.genetic_path_generator import *
from exercises.problem import generate
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@click.command()
@click.option('--checkfit', is_flag=True)
def tests(checkfit):
    if checkfit:
        problem = create_problem()
        problem = generate(5, 5)

        population = pop_generator(problem)

        # list1 = ['A', 'B', 'C', 'E', 'D', 'G', 'H', 'F']
        # cost = fitness(problem, list1)
        # click.echo(cost)

if __name__ == '__main__':
    tests()
