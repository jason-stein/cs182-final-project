# agents for various search algorithms

import util
import generate

def BFS(s1,s2,graph):

	frontier = util.PriorityQueueWithFunction(lambda x: len(x[1]))
	visited = set()
	frontier.push((s1.id,[s1.id]))

	while not frontier.isEmpty():
		node = frontier.pop()
		if node[0] in visited:
			continue
		visited.add(node[0])
		if node[0] == s2.id:
			return node[1]

		for i in xrange(len(graph.adjMatrix[node[0]])):
			if graph.adjMatrix[node[0]][i] == 1:
				frontier.push((i, node[1] + [i]))
	return []

def nullHeuristic(state,graph):
	return 0

def aStar(s1,s2,graph):

	frontier = util.PriorityQueueWithFunction(lambda x: len(x[1]) 
		+ graph.heuristicMatrix[x[0]][s2.id])
	
	visited = set()
	frontier.push((s1.id,[s1.id]))

	while not frontier.isEmpty():
		node = frontier.pop()
		if node[0] in visited:
			continue
		visited.add(node[0])
		if node[0] == s2.id:
			return node[1]

		for i in xrange(len(graph.adjMatrix[node[0]])):
			if graph.adjMatrix[node[0]][i] == 1:
				frontier.push((i, node[1] + [i]))
	return []
