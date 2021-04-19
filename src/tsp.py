import random
import json

from .genetic.crossover import *
from .genetic.mutation import *
from .genetic.evolution import *

# Running TSP with genetic algorithm
FILE = "./examples/gr17.json"
data = json.load(open(FILE))
optimal = data["OptTour"]
matrix = data["DistanceMatrix"]
size = data["TourSize"]
fittest = data["OptDistance"]

# fitness function imp
def fitness(individual):
    distance = matrix[individual[-1]][individual[0]]

    for i in individual:
        count = individual.count(i)
        if count > 1:
            distance += 1000

    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        distance += matrix[gene1][gene2]
    return distance

def run():
    solver = GeneticSolver(
            fitness_func=fitness,
            crossover_func=single_point,
            mutation_func=swap,
            pop_size=50,
            mut_prob=0.1,
            tourn_size=4,
            reverse=True
            )

    pop = []
    p = [i for i in range(size - 1)]
    for _ in range(50):
        random.shuffle(p)
        pop.append(p)

    res = solver.evolve(pop, gen_size=100)

    print("\nSolution:: " , res)
    print("Fitness:: ", fitness(res))
    print("\nOptimal:: ", optimal)
    print("Fitness:: ", fittest)

# run the example
run()
