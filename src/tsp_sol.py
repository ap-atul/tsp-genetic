# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

	# store all vertex apart from source vertex
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	# store minimum weight Hamiltonian Cycle
	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost)
		current_pathweight = 0

		# compute current path weight
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		# update minimum
		min_path = min(min_path, current_pathweight)
	return min_path


# Driver Code
if __name__ == "__main__":

        # constant values
        cities = {0: 'Delhi', 1: 'Mumbai', 2: 'Pune', 3: 'Kolkata', 
                4: 'Gujrat', 5: 'Banglore', 6: 'J&K', 7: 'Nagaland'}

        # Distance between each pair of cities
        graph = [[100, 500, 450, 480, 200, 560, 180, 400],
        [500, 100, 80, 300, 250, 500, 590, 600],
        [450, 80, 100, 400, 226, 400, 500, 500],
        [480, 300, 400, 100, 500, 400, 500, 300],
        [200, 250, 226, 500, 100, 500, 400, 600],
        [560, 500, 400, 400, 500, 100, 600, 600],
        [180, 590, 500, 500, 400, 600, 100, 600],
        [400, 600, 500, 500, 600, 600, 600, 100]]
	
        # matrix representation of graph
        s = 0
        print(travellingSalesmanProblem(graph, s))

