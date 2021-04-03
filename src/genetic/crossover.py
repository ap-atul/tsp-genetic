import random

def single_point(gene_one, gene_two):
    p = random.randint(0, min(len(gene_one), len(gene_two)))
    gene_one[p: ], gene_two[p: ] = gene_two[p: ], gene_one[p: ]
    return gene_one, gene_two

def two_point(gene_one, gene_two):
    size = min(len(gene_one), len(gene_two))
    p1, p2 = random.randint(0, size), random.randint(0, size -1)
    if p1 > p2:
        p1, p2 = p2, p1
    else:
        p1, p2 = p1, p2 + 1
    gene_one[p1: p2], gene_two[p1: p2] = gene_two[p1: p2], gene_one[p1: p2]
    return gene_one, gene_two

def uniform(gene_one, gene_two, prob=0.4):
    for i in range(min(len(gene_one), len(gene_two))):
        if random.random() < prob:
            gene_one[i], gene_two[i] = gene_two[i], gene_one[i]
    return gene_one, gene_two

def partially_mapped(gene_one, gene_two):
    p1, p2 = random.randint(0, len(gene_one) - 1), random.randint(0, len(gene_one) - 1)
    if p1 >= p2:
        p1, p2 = p2, p1 + 1
    pos_one = {value: idx for idx, value in enumerate(gene_one)}
    pos_two = {value: idx for idx, value in enumerate(gene_two)}
    for i in range(p1, p2):
        value1, value2 = gene_one[i], gene_two[i]
        pos1, pos2 = pos_one[value2], pos_two[value1]
        gene_one[i], gene_one[pos1] = gene_one[pos1], gene_one[i]
        gene_two[i], gene_two[pos2] = gene_two[pos2], gene_two[i]
        pos_one[value1], pos_one[value2] = pos1, i
        pos_two[value1], pos_two[value2] = i, pos2

    return gene_one, gene_two

def cyclic(gene_one, gene_two):
    lookup = {v:i for i,v in enumerate(gene_one)}
    cycles = [-1] * len(gene_one)
    cyclestart = (i for i,v in enumerate(cycles) if v < 0)
    for cycle_no, pos in enumerate(cyclestart, 1):
        while cycles[pos] < 0:
            cycles[pos] = cycle_no
            pos = lookup[gene_two[pos]]

    for cycle in cycles:
        gene_one[cycle] = gene_two[gene_one[cycle]]
    return gene_one, gene_two

