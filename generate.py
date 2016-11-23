# Generation of social graph

import random
import util

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

def maybeFriends(s1,s2):		# randomly decides if s1, s2 friends based on 
	p = BASE_PROB				# shared characteristics
	if s1.house == s2.house:
		p += HOUSE_PROB_INC
	if s1.interest == s2.interest:
		p += INTEREST_PROB_INC
	if s1.year == s2.year:
		p += YEAR_PROB_INC
	return util.flipCoin(p)

class SocialGraph:

	def __init__(self):

		self.students = []
		self.adjMatrix = []
		for i in xrange(NSTUDENTS):
			self.adjMatrix.append([])
			for _ in xrange(NSTUDENTS):
				self.adjMatrix[i].append(0)

		for i in xrange(NSTUDENTS):
			student = Student()
			student.id = i
			self.students.append(student)
		for i in xrange(NSTUDENTS):
			for j in xrange(i):
				if maybeFriends(self.students[i],self.students[j]):
					self.adjMatrix[i][j] = self.adjMatrix[j][i] = 1

	def prettyPrintGraph(self):
		for i in self.adjMatrix:
			print i

