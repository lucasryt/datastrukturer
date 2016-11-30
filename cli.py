#!/usr/bin/env python3
import click
from exercises.problem_generation import create_problem
from exercises.genetic_path_generator import *


@click.command()
@click.option('--checkfit', is_flag=True)
def tests(checkfit):
    if checkfit:
        list1 = []
        create_problem()
        cost = fitness(list1)
        click.echo(cost)

if __name__ == '__main__':
    tests()
