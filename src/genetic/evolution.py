import sys
import random

class GeneticSolver:
    def __init__(self, fitness_func, crossover_func, mutation_func, pop_size, mut_prob, tourn_size, reverse=True):
        self._fitness_func, self._crossover_func, self._mutation_func = fitness_func, crossover_func, mutation_func
        self._pop_size, self._mut_prob, self._tourn_size, self._rev = pop_size, mut_prob, tourn_size, reverse

    def _tournament(self, pop, min_max):
        tourn = [pop[random.randint(0, len(pop) - 1)] for _ in range(self._tourn_size)]
        fitness = [self._fitness_func(gene) for gene in tourn]
        return pop[fitness.index(min_max(fitness))]

    def evolve(self, pop, gen_size):
        min_max = max if self._rev else min
        best_sol, best_fit = [], sys.maxsize

        for g in range(gen_size + 1):
            pop = sorted(pop, key= lambda gene: self._fitness_func(gene), reverse=self._rev)
            if (x := self._fitness_func(pop[0])) < best_fit:
                best_fit, best_sol = x, pop[0]

            print(f"Generation {g} :: {pop[0]}")
            print(f"Fitness :: {self._fitness_func(pop[0])} \n")

            new_pop = pop[0: 5]
            for i in range(int(len(pop) / 2) - 1):
                parent_one, parent_two = self._tournament(pop, min_max), self._tournament(pop, min_max)
                child_one, child_two = self._crossover_func(parent_one, parent_two)
                child_one, child_two = self._mutation_func(child_one, self._mut_prob), self._mutation_func(child_two, self._mut_prob)
                new_pop += [child_one, child_two]
            pop = new_pop

        print(f"Best so far :: {best_sol} {best_fit}")
        return sorted(pop, key= lambda gene: self._fitness_func(gene), reverse=self._rev)[0]

