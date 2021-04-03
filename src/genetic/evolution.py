import random

class GeneticSolver:
    def __init__(self, fitness_func, crossover_func, mutation_func, pop_size, mut_prob, tourn_size, reverse=True):
        self._fitness_func, self._crossover_func, self._mutation_func = fitness_func, crossover_func, mutation_func
        self._pop_size, self._mut_prob, self._tourn_size, self._rev = pop_size, mut_prob, tourn_size, reverse

    def _tournament(self, pop):
        tourn = [pop[random.randint(0, len(pop) - 1)] for _ in range(self._tourn_size)]
        fitness = [self._fitness_func(gene) for gene in tourn]
        return pop[fitness.index(max(fitness))]

    def evolve(self, pop, gen_size):
        for _ in range(gen_size + 1):
            pop = sorted(pop, key= lambda gene: self._fitness_func(gene), reverse=self._rev)
            new_pop = pop[0: 2]
            for i in range(int(len(pop) / 2) - 1):
                parent_one, parent_two = self._tournament(pop), self._tournament(pop)
                child_one, child_two = self._crossover_func(parent_one, parent_two)
                child_one, child_two = self._mutation_func(child_one, self._mut_prob), self._mutation_func(child_two, self._mut_prob)
                new_pop += [child_one, child_two]
            pop = new_pop

            for p in pop:
                print(p)

        return pop
