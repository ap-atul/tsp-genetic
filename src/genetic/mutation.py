import random

def swap(gene, prob):
    if random.random() < prob:
        p1, p2 = random.randint(0, len(gene) - 2), random.randint(0, len(gene) - 1)
        if p1 >= p2:
            p1, p2 = p2, p1 + 1
        gene[p1], gene[p2] = gene[p2], gene[p1]
    return gene

def reverse(gene, prob):
    if random.random() < prob:
        p1, p2 = random.randint(0, len(gene) - 2), random.randint(0, len(gene) - 1)
        if p1 >= p2:
            p1, p2 = p2, p1 + 1
        gene[p1: p2] = gene[p1: p2][:: -1]
    return gene

def random_(gene, prob):
    if random.random() < prob:
        p1 = random.randint(0, len(gene) - 1)
        gene[p1] = random.choice(gene)
    return gene
