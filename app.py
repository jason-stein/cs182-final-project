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

start = time.time()
avg1 = 0.0
n1 = n
for i in xrange(n):
	# separation = len(search.UCS(random.choice(graph.students),random.choice(graph.students),graph))
	separation = len(search.UCS(graph.students[i],graph.students[i+1],graph))
	if separation != 0:
		avg1 += separation
	else:
		n1 -= 1

	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("UCS iter " + str(i+1) + '   ' + progress + "\r")
	sys.stdout.flush()
avg1 = avg1 / n1
end = time.time()
diff1 = end - start
print ""

start = time.time()
avg2 = 0.0
n2 = n
for i in xrange(n):
	separation = len(search.aStar(graph.students[i],graph.students[i+1],graph, ))
	if separation != 0:
		avg2 += separation
	else:
		n2 -= 1
	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("aStar untrained iter " + str(i+1) + ' ' + progress + "\r")
	sys.stdout.flush()
avg2 = avg2 / n2
end = time.time()
diff2 = end - start
print ""


graph.train(400000)
plt.figure(2)
plt.title("Trained Locations")
graph.plotStudents('gs', lines=False)

start = time.time()
avg3 = 0.0
n3 = n
for i in xrange(n):
	separation = len(search.aStar(graph.students[i],graph.students[i+1],graph, ))
	if separation != 0:
		avg3 += separation
	else:
		n3 -= 1
	progress = '|' + '#' * int(float(i+1) / float(n) * 10) + ' '  * (10 - int(float(i+1) / float(n) * 10)) + '|'
	sys.stdout.write("aStar trained iter " + str(i+1) + ' ' + progress + "\r")
	sys.stdout.flush()
avg3 = avg3 / n3
end = time.time()
diff3 = end - start
print ""

print "UCS -- Time:", diff1, " Avg:", avg1, " Iterations:", n
print "aStar untrained -- Time:", diff2, " Avg:", avg2, " Iterations:", n
print "aStar trained -- Time:", diff3, " Avg:", avg3, " Iterations:", n
print "The average person has", graph.averageFriends(), "friends."

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