# agents for various search algorithms

import util
import generate

# Uniform Cost Search, effectively basic BFS for social graphs with uniform edge costs
def BFS(s1,s2,graph):
	nnodes = 0
	frontier = util.PriorityQueueWithFunction(lambda x: len(x[1]))
	visited = set()
	frontier.push((s1.id,[s1.id]))

	while not frontier.isEmpty():
		node = frontier.pop()
		if node[0] in visited:
			continue
		nnodes += 1
		visited.add(node[0])
		if node[0] == s2.id:
			return (node[1],nnodes)

		for i in xrange(generate.NSTUDENTS):
			if graph.adjMatrix[node[0]][i] == 1:
				frontier.push((i, node[1] + [i]))
	return ([],0)

# A* heuristic search
def aStar(s1,s2,graph):
	nnodes = 0
	frontier = util.PriorityQueueWithFunction(lambda x: len(x[1]) 
		+ graph.heuristicMatrix[x[0]][s2.id])
	
	visited = set()
	frontier.push((s1.id,[s1.id]))

	while not frontier.isEmpty():
		node = frontier.pop()
		if node[0] in visited:
			continue
		nnodes += 1
		visited.add(node[0])
		if node[0] == s2.id:
			return (node[1],nnodes)

		for i in xrange(generate.NSTUDENTS):
			if graph.adjMatrix[node[0]][i] == 1:
				frontier.push((i, node[1] + [i]))
	return ([],0)

# 2-sided BFS (expands out from both nnodes)
def BFS2(s1,s2,graph):
	nnodes = 0
	frontier1 = util.PriorityQueueWithFunction(lambda x: len(x[1]))
	frontier2 = util.PriorityQueueWithFunction(lambda x: len(x[1]))
	visited1 = set()
	visited2 = set()
	frontier1.push((s1.id,[s1.id]))
	frontier2.push((s2.id,[s2.id]))
	curLen = 1

	while not frontier1.isEmpty() and not frontier2.isEmpty():
		while True:
			node1 = frontier1.pop()
			if len(node1[1]) != curLen:
				frontier1.push(node1)
				break
			if node1[0] in visited1:
				continue
			nnodes += 1
			for i in frontier2.heap:
				if node1[0] == i[2][0]:
					i[2][1].reverse()
					return (node1[1] + i[2][1][1:],nnodes)
			for i in xrange(generate.NSTUDENTS):
				if graph.adjMatrix[node1[0]][i] == 1:
					frontier1.push((i, node1[1] + [i]))
		while True:
			node2 = frontier2.pop()
			if len(node2[1]) != curLen:
				frontier2.push(node2)
				curLen += 1
				break
			if node2[0] in visited2:
				continue
			nnodes += 1
			for i in frontier1.heap:
				if i[2][0] == node2[0]:
					node2[1].reverse()
					return (i[2][1] + node2[1][1:],nnodes)
			for i in xrange(generate.NSTUDENTS):
				if graph.adjMatrix[node2[0]][i] == 1:
					frontier2.push((i, node2[1] + [i]))
	return ([],0)

# Depth limited search
def DLS(s1, s2, graph, depth):
	frontier = util.Stack()
	frontier.push((s1.id,[s1.id]))

	while not frontier.isEmpty():
		node = frontier.pop()
		if node[0] in node[1][:-1] or len(node[1]) > depth:
			continue
		if node[0] == s2.id:
			return node[1]
		for i in xrange(generate.NSTUDENTS):
			if graph.adjMatrix[node[0]][i] == 1:
				frontier.push((i, node[1] + [i]))
	return []

# Iterative deepening depth first search, use 3 as initial depth because it is the average depth for 
# the type of problems we are searching
def IDDFS(s1, s2, graph):
	depth = 3
	result = DLS(s1, s2, graph, depth)
	if result:
		while depth > 0:
			depth -= 1
			tmp = DLS(s1, s2, graph, depth)
			if tmp:
				result = tmp
			else:
				break
		return result
	else:
		while not result:
			depth += 1
			result = DLS(s1, s2, graph, depth)
		return result

	return []
