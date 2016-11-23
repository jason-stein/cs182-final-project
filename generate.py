# Generation of social graph

import random
import util
import sys

HOUSE_PROB_INC = .4
INTEREST_PROB_INC = .1
YEAR_PROB_INC = .1
BASE_PROB = .05
NSTUDENTS = 2000


class Student:

	def __init__(self):
		self.id = 0
		self.house = random.choice(["Adams","Cabot","Currier","Dunster","Eliot",
			"Kirkland","Leverett","Lowell","Mather","Pforzheimer","Quincy",
			"Winthrop"])
		self.interest = random.choice(["academics","arts","sports"])
		self.year = random.choice([17,18,19,20])
		self.pos = [random.random(), random.random()]

def maybeFriends(s1,s2):		# randomly decides if s1, s2 friends based on 
	p = BASE_PROB				# shared characteristics
	if s1.house == s2.house:
		p += HOUSE_PROB_INC
	if s1.interest == s2.interest:
		p += INTEREST_PROB_INC
	if s1.year == s2.year:
		p += YEAR_PROB_INC
	return util.flipCoin(p)

def changeDistance(student1, student2, friends):
    dx = student2.pos[0] - student1.pos[0]
    dy = student2.pos[1] - student1.pos[1]
    change = 1.0
    if friends:
        change = 0.9
    else:
        change = 1.1
    new_dx = dx * change
    new_dy = dy * change
    new_x = student1.pos[0] + new_dx
    new_y = student1.pos[1] + new_dy
    if new_x > 1.0:
        new_x = 1.0
    if new_x < 0.0:
        new_x = 0.0
    if new_y > 1.0:
        new_y = 1.0
    if new_y < 0.0:
        new_y = 0.0

    student2.pos = [new_x, new_y] 

class SocialGraph:

	def __init__(self):

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
				dis = util.cartesianDistance(self.students[i].pos, self.students[j].pos)
				self.heuristicMatrix[i][j] = self.heuristicMatrix[j][i] = dis

	def prettyPrintGraph(self):
		for i in self.adjMatrix:
			print i
	def prettyPrintHeuristic(self):
		for i in self.heuristicMatrix:
			print i

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
			self.heuristicMatrix[s1.id][s2.id] = self.heuristicMatrix[s2.id][s1.id] = util.cartesianDistance(s1.pos, s2.pos)
		print ""
