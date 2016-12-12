# Script for testing issues with accuracy between searchAgents

import generate as gen
import searchAgents as search
import random
graph = gen.SocialGraph()
x = random.choice(graph.students)
y = random.choice(graph.students)
result1 = search.BFS(x,y,graph)
result2 = (search.IDDFS(x,y,graph),0)
result3 = search.BFS2(x,y,graph)
result4 = search.aStar(x,y,graph)
print "BFS path and # nodes expanded:", result1
print "Iter. Deepening path:", result2[0]
print "2-sided BFS path and # nodes expanded:", result3
print "A* path and # nodes expanded:",result4
results = [result1,result2,result3,result4]
print "All paths same length:", all(len(result[0]) == len(result1[0]) for result in results)