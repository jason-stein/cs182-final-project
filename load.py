import snap

def loadFacebookGraph():
	G1 = snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)
	adjMatrix = []
	ite = G1.BegNI()
	for i in xrange(G1.GetNodes()):
		edges = []
		for j in xrange(G1.GetNodes()):
			if ite.IsNbrNId(j):
				edges.append(1)
			else:
				edges.append(0)
		adjMatrix.append(edges)
		ite.Next()
	print "Facebook graph loaded"
	return adjMatrix