import random

from .genetic.crossover import *
from .genetic.mutation import *
from .genetic.evolution import *

# Running TSP with genetic algorithm

# constant values
cities = {0: 'Delhi', 1: 'Mumbai', 2: 'Pune', 3: 'Kolkata', 
        4: 'Gujrat', 5: 'Banglore', 6: 'J&K', 7: 'Nagaland'}

# Distance between each pair of cities
w0 = [100, 500, 450, 480, 200, 560, 180, 400]
w1 = [500, 100, 80, 300, 250, 500, 590, 600]
w2 = [450, 80, 100, 400, 226, 400, 500, 500]
w3 = [480, 300, 400, 100, 500, 400, 500, 300]
w4 = [200, 250, 226, 500, 100, 500, 400, 600]
w5 = [560, 500, 400, 400, 500, 100, 600, 600]
w6 = [180, 590, 500, 500, 400, 600, 100, 600]
w7 = [400, 600, 500, 500, 600, 600, 600, 100]

distances = {0: w0, 1: w1, 2: w2, 3: w3, 4: w4, 5: w5, 6: w6, 7: w7}


# fitness function imp
def fitness(chromosome):
    def distance(index, city):
        w = distances.get(index)
        return w[city]

    def penalty(chromosome):
        val = 0
        for i in chromosome:
            times = chromosome.count(i)
            if times > 1:
                val += 1000 * times
        return val

    chromosome = list(chromosome)
    fitness_val = count = 0
    penalty_val = penalty(chromosome)

    for i in chromosome:
        if count >= 7:
            city = chromosome[0]
        else:
            temp = count + 1
            city = chromosome[temp]

        fitness_val += distance(i, city) + penalty_val
        count += 1

    return fitness_val

def run():
    solver = GeneticSolver(
            fitness_func=fitness,
            crossover_func=single_point,
            mutation_func=swap,
            pop_size=10,
            mut_prob=0.1,
            tourn_size=4,
            reverse=False
            )
    
    pop = []
    for _ in range(10):
        p = [0, 1, 2, 3, 4, 5, 6, 7]
        random.shuffle(p)
        pop.append(p)

    res = solver.evolve(pop, gen_size=100)

    print("\nSolution:: " , res)
    print("Fitness:: ", fitness(res))

    print("\nRoute ::")
    sol = []
    for i in res:
        sol.append(cities[i])
    print(' --> '.join(sol))

# run the example
run()
