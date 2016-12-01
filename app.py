import util, generate, random
import searchAgents as search
import time
import sys
import matplotlib.pyplot as plt
# import networkx as nx

n = 25

graph = generate.SocialGraph()
plt.figure(1)
plt.title("Untrained (Random) Locations")
graph.plotStudents(lines=False)
print "The average person has", graph.averageFriends(), "friends."
print "The average person has", graph.averageInterests(), "interests."

start = time.time()
avg1 = 0.0
n1 = n
for i in xrange(n):
	# separation = len(search.UCS(random.choice(graph.students),random.choice(graph.students),graph))
	separation = len(search.UCS(graph.students[i],graph.students[i+1],graph))
	if separation != 0:
		avg1 += separation - 1
	else:
		n1 -= 1

	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("BFS iter " + str(i+1) + '   ' + progress + "\r")
	sys.stdout.flush()
avg1 = avg1 / n1
end = time.time()
diff1 = end - start
print ""

start = time.time()
avg4 = 0.0
n4 = n
for i in xrange(n):
	# separation = len(search.UCS(random.choice(graph.students),random.choice(graph.students),graph))
	separation = len(search.UCS(graph.students[i],graph.students[i+1],graph))
	if separation != 0:
		avg4 += separation - 1
	else:
		n4 -= 1

	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("2-sided BFS iter " + str(i+1) + '   ' + progress + "\r")
	sys.stdout.flush()
avg4 = avg4 / n4
end = time.time()
diff4 = end - start
print ""

start = time.time()
avg2 = 0.0
n2 = n
for i in xrange(n):
	separation = len(search.aStar(graph.students[i],graph.students[i+1],graph, ))
	if separation != 0:
		avg2 += separation - 1
	else:
		n2 -= 1
	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("A* untrained iter " + str(i+1) + ' ' + progress + "\r")
	sys.stdout.flush()
avg2 = avg2 / n2
end = time.time()
diff2 = end - start
print ""


graph.train(1000000)
plt.figure(2)
plt.title("Trained Locations")
graph.plotStudents('gs', lines=False)

start = time.time()
avg3 = 0.0
n3 = n
for i in xrange(n):
	separation = len(search.aStar(graph.students[i],graph.students[i+1],graph, ))
	if separation != 0:
		avg3 += separation - 1
	else:
		n3 -= 1
	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("A* trained iter " + str(i+1) + ' ' + progress + "\r")
	sys.stdout.flush()
avg3 = avg3 / n3
end = time.time()
diff3 = end - start
print ""

print "BFS -- Time:", diff1, "Avg Separation:", avg1, "Iterations:", n
print "2-sided BFS -- Time:", diff4, "Avg Separation:", avg4, "Iterations:", n
print "A* untrained -- Time:", diff2, "Avg Separation:", avg2, "Iterations:", n
print "A* trained -- Time:", diff3, "Avg Separation:", avg3, "Iterations:", n

# print "creating graph"
# G = nx.Graph()
# for i in xrange(generate.NSTUDENTS):
# 	G.add_node(i)
# 	for j in xrange(i):
# 		if graph.adjMatrix[i][j] == 1:
# 			G.add_edge(i,j)
# plt.figure(3)
# nx.draw(G)

plt.show()