# Generation of social graph

import random
import util
import sys
import math
import matplotlib.pyplot as plt

# constants for probability increase on shared characteristics
HOUSE_PROB_INC = .5
INTEREST_PROB_INC = .1
YEAR_PROB_INC = .2
BASE_PROB = 0
NSTUDENTS = 2000

# inverse square root of 2 -- bound for heuristic grid
ISQR2 = 1 / math.sqrt(2.0)

# class for individual student -- contains attributes and location
class Student:

	def __init__(self):
		self.id = 0
		self.house = random.choice(["Adams","Cabot","Currier","Dunster","Eliot",
			"Kirkland","Leverett","Lowell","Mather","Pforzheimer","Quincy",
			"Winthrop"])
		self.interest = random.choice(["academics","arts","sports"])
		self.year = random.choice([17,18,19,20])
		self.pos = [random.uniform(0,1), random.uniform(0,1)]

# randomly decides if s1, s2 friends based on shared characteristics
def maybeFriends(s1,s2):
	p = BASE_PROB
	if s1.house == s2.house:
		p += HOUSE_PROB_INC
	if s1.interest == s2.interest:
		p += INTEREST_PROB_INC
	if s1.year == s2.year:
		p += YEAR_PROB_INC
	return util.flipCoin(p)

# push students closer or farther depending on friendship status
def changeDistance(student1, student2, friends):
    dx = student2.pos[0] - student1.pos[0]
    dy = student2.pos[1] - student1.pos[1]
    change = 1.0
    if friends:
        change = 0.9
    else:
        change = 1.01
    new_dx = dx * change
    new_dy = dy * change
    new_x = student1.pos[0] + new_dx
    new_y = student1.pos[1] + new_dy
    # if new_x > ISQR2:
    #     new_x = ISQR2
    # if new_x < 0.0:
    #     new_x = 0.0
    # if new_y > ISQR2:
    #     new_y = ISQR2
    # if new_y < 0.0:
    #     new_y = 0.0

    student2.pos = [new_x, new_y] 

#
# class for social graph. contains students, friendship adjacency matrix,
# heuristic matrix, and heuristic training function, as well as various
# display / debug functions
#
class SocialGraph:

	# generates NSTUDENTS random studends, creates 
	# adjacency and heuristic matrices
	def __init__(self):

		print "Generating data set ( n =",NSTUDENTS,")"
		self.students = []
		self.adjMatrix = []
		self.heuristicMatrix = []
		for i in xrange(NSTUDENTS):
			self.adjMatrix.append([])
			self.heuristicMatrix.append([])
			for _ in xrange(NSTUDENTS):
				self.adjMatrix[i].append(0)
				self.heuristicMatrix[i].append(0)

		for i in xrange(NSTUDENTS):
			student = Student()
			student.id = i
			self.students.append(student)
		for i in xrange(NSTUDENTS):
			for j in xrange(i):
				if maybeFriends(self.students[i],self.students[j]):
					self.adjMatrix[i][j] = self.adjMatrix[j][i] = 1
		for i in xrange(NSTUDENTS):
			for j in xrange(i):
				dis = util.cartesianDistance(
					self.students[i].pos, self.students[j].pos)
				self.heuristicMatrix[i][j] = self.heuristicMatrix[j][i] = dis

	def prettyPrintGraph(self):
		for i in self.adjMatrix:
			print i

	def prettyPrintHeuristic(self):
		for i in self.heuristicMatrix:
			print i

	# trains the data set: for each iteration, finds random pair and updates
	# distance based on friendship status
	def train(self, iterations):
		for i in xrange(iterations):
			sys.stdout.write("Training: " + str(i+1) + "\r")
			sys.stdout.flush()
			p1 = random.randint(0, len(self.students)-1)
			p2 = random.randint(0, len(self.students)-1)
			while p1 == p2:
				p2 = random.randint(0, len(self.students)-1)
			s1 = self.students[p1]
			s2 = self.students[p2]
			if self.adjMatrix[s1.id][s2.id] == 1:
				# Pull p2 closer
				changeDistance(s1, s2, True)
			else:
				# Push p2 away
				changeDistance(s1, s2, False)
			self.heuristicMatrix[s1.id][s2.id] = \
			self.heuristicMatrix[s2.id][s1.id] = \
			util.cartesianDistance(s1.pos, s2.pos)
		maxDist = max(map(lambda x: max(x),self.heuristicMatrix))
		for i in xrange(NSTUDENTS):
			for j in xrange(NSTUDENTS):
				self.heuristicMatrix[i][j] /= maxDist
		print ""

	# plots each student's position as a point with customizable format string
	def plotStudents(self,style):
		xs = [student.pos[0] for student in self.students]
		ys = [student.pos[1] for student in self.students]
		plt.plot(xs,ys,style)
		minx = min(map(lambda x: x.pos[0], self.students))
		maxx = max(map(lambda x: x.pos[0], self.students))
		miny = min(map(lambda x: x.pos[1], self.students))
		maxy = max(map(lambda x: x.pos[1], self.students))
		plt.axis([minx,maxx,miny,maxy])
		plt.draw()