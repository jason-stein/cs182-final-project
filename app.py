import util, generate, random
import searchAgents as search
import time

n = 10

graph = generate.SocialGraph()

start = time.time()
avg1 = 0.0
n1 = n
for i in xrange(n):
	# separation = len(search.BFS(random.choice(graph.students),random.choice(graph.students),graph))
	separation = len(search.BFS(graph.students[i],graph.students[i+1],graph))
	if separation != 0:
		avg1 += separation
	else:
		n1 -= 1
	print 'BFS iter:', i+1
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
	print 'aStar iter:', i+1
avg2 = avg2 / n2
end = time.time()
diff2 = end - start

print ""

print "BFS -- Time:", diff1, " Avg:", avg1, " Iterations:", n
print "aStar -- Time:", diff2, " Avg:", avg2, " Iterations:", n