import random
import math
from evolution import *
from mutation import *
from crossover import *

def fit(x):
    return xi

def x(s):
	return s[0]

def rosenbrock(x): # https://www.sfu.ca/~ssurjano/rosen.html
    return sum([ ( 100 * math.pow((x[i + 1] - math.pow(x[i], 2)), 2) + math.pow((x[i] - 1), 2)  )  for i in range(len(x) - 1)])

solver = GeneticSolver(
            fitness_func=x,
            crossover_func=two_point,
            mutation_func=random_,
            pop_size=10,
            mut_prob=0.1,
            tourn_size=4,
            reverse=False
        )
pop = [[random.randint(0, 10) for _ in range(10)] for _ in range(10)]
res = solver.evolve(pop, gen_size=100)
print(res)
