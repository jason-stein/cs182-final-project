import generate as gen
import searchAgents as search
import random
graph = gen.SocialGraph()
x = random.choice(graph.students)
y = random.choice(graph.students)
result1 = search.UCS(x,y,graph)
result2 = search.IDDFS(x,y,graph)
print result1
print result2
print len(result1) == len(result2)