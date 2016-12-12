import util, generate, random
import searchAgents as search
import time
import sys
import matplotlib.pyplot as plt
# import networkx as nx

n = 50	# number of iterations of each algorithm

# generate a social graph
graph = generate.SocialGraph()
# graph.loadAdjMatrix()

# plot the randomized locations
plt.figure(1)
plt.title("Untrained (Random) Locations")
graph.plotStudents(lines=False)

# summary statistics of social graph
print "The average person has", graph.averageFriends(), "friends."
print "The average person has", graph.averageInterests(), "interests."

# time n iterations of BFS search for deterministically selected pairs
start = time.time()
avg1 = 0.0
nnodes1 = 0
n1 = n
for i in xrange(n):
	# try to find the path
	ret = search.BFS(graph.students[i],graph.students[i+1],graph)
	separation = len(ret[0])
	# if the path exists, factor it in to average path len
	if separation != 0:
		avg1 += separation - 1
		nnodes1 += ret[1]
	# otherwise ignore this pair
	else:
		n1 -= 1

	# progress bar visualiation
	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("BFS iter " + str(i+1) + '   ' + progress + "\r")
	sys.stdout.flush()
# calculate average degrees of separation
avg1 = avg1 / n1
# calculate averange number of nodes expanded
nnodes1 = nnodes1 / n1
# calculate execution time
end = time.time()
diff1 = end - start
print ""

# continue as above for other algorithms
start = time.time()
avg2 = 0.0
nnodes2 = 0
n2 = n
for i in xrange(n):
	ret = search.aStar(graph.students[i],graph.students[i+1],graph)
	separation = len(ret[0])
	if separation != 0:
		avg2 += separation - 1
		nnodes2 += ret[1]
	else:
		n2 -= 1
	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("A* untrained iter " + str(i+1) + ' ' + progress + "\r")
	sys.stdout.flush()
avg2 = avg2 / n2
nnodes2 = nnodes2 / n2
end = time.time()
diff2 = end - start
print ""

# train the locations, plot the new locations in a new figure
graph.train(1000000)
plt.figure(2)
plt.title("Trained Locations")
graph.plotStudents('gs', lines=False)

start = time.time()
avg3 = 0.0
nnodes3 = 0
n3 = n
for i in xrange(n):
	ret = search.aStar(graph.students[i],graph.students[i+1],graph)
	separation = len(ret[0])
	if separation != 0:
		avg3 += separation - 1
		nnodes3 += ret[1]
	else:
		n3 -= 1
	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("A* trained iter " + str(i+1) + ' ' + progress + "\r")
	sys.stdout.flush()
avg3 = avg3 / n3
nnodes3 = nnodes3 / n3
end = time.time()
diff3 = end - start
print ""

start = time.time()
avg4 = 0.0
nnodes4 = 0
n4 = n
for i in xrange(n):
	ret = search.BFS2(graph.students[i],graph.students[i+1],graph)
	separation = len(ret[0])
	if separation != 0:
		avg4 += separation - 1
		nnodes4 += ret[1]
	else:
		n4 -= 1

	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("2-sided BFS iter " + str(i+1) + '   ' + progress + "\r")
	sys.stdout.flush()
avg4 = avg4 / n4
nnodes4 = nnodes4 / n4
end = time.time()
diff4 = end - start
print ""


# summary statistics
print "BFS -- Time:", diff1, "Avg Nodes:", nnodes1, "Avg Separation:", avg1, "Iterations:", n
print "A* untrained -- Time:", diff2, "Avg Nodes:", nnodes2, "Avg Separation:", avg2, "Iterations:", n
print "A* trained -- Time:", diff3, "Avg Nodes:", nnodes3, "Avg Separation:", avg3, "Iterations:", n
print "2-sided BFS -- Time:", diff4, "Avg Nodes:", nnodes4, "Avg Separation:", avg4, "Iterations:", n

# we used the networkx library to visualize the graph but it was too dense to be interesting
# print "creating graph"
# G = nx.Graph()
# for i in xrange(generate.NSTUDENTS):
# 	G.add_node(i)
# 	for j in xrange(i):
# 		if graph.adjMatrix[i][j] == 1:
# 			G.add_edge(i,j)
# plt.figure(3)
# nx.draw(G)

# show all graphs
plt.show()