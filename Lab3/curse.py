import numpy as np
import math
from random import randint
import matplotlib.pyplot as plt

class Envirnoment1:
	def __init__ (self, l):
		self.l = l
		self.s = math.ceil(l/2)
		self.moves = 0
	def goal(self):
		if self.s == self.l:
			return True
		return False
	def randmove(self):
		return randint(0,1)
	def assign(self):
		num = self.randmove()
		if num == 0:
			self.m = -1
		else:
			self.m = 1
	def action(self):
		self.assign()
		self.s = self.s + self.m
		if self.s == -1 :
			self.s = 0
		self.moves = self.moves + 1
	def run(self):
		while not self.goal():
			self.action()
		#self.print_info()
	def print_info(self):
		print ("Envirnoment->1D moves taken = ",self.moves)

class Envirnoment2:
	def __init__ (self, l):
		self.l = l
		self.s = np.array([math.ceil(l/2),math.ceil(l/2)])
		self.moves = 0
	def goal(self):
		if self.s[0] == self.l and self.s[1] == self.l:
			return True
		return False
	def randmove(self):
		return randint(0,3)
	def assign(self):
		num = self.randmove()
		if num == 0:
			self.m = np.array([0,1])
		elif num == 1:
			self.m = np.array([1,0])
		elif num == 2:
			self.m = np.array([0,-1])
		else:
			self.m = np.array([-1,0])
	def action(self):
		self.assign()
		self.s = self.s + self.m
		if self.s[0] == -1:
			self.s[0] = 0
		elif self.s[0] == self.l + 1 :
			self.s[0] = self.l
		if self.s[1] == -1:
			self.s[1] = 0
		elif self.s[1] == self.l + 1 :
			self.s[1] = self.l
		self.moves = self.moves + 1
	def run(self):
		while not self.goal():
			self.action()
		#self.print_info()
	def print_info(self):
		print ("Envirnoment->2D moves taken = ",self.moves)

class Envirnoment3:
	def __init__ (self, l):
		self.l = l
		self.s = np.array([math.ceil(l/2),math.ceil(l/2),math.ceil(l/2)])
		self.moves = 0
	def goal(self):
		if self.s[0] == self.l and self.s[1] == self.l and self.s[2] == self.l:
			return True
		return False
	def randmove(self):
		return randint(0,5)
	def assign(self):
		num = self.randmove()
		if num == 0:
			self.m = np.array([0,0,1])
		elif num == 1:
			self.m = np.array([0,1,0])
		elif num == 2:
			self.m = np.array([1,0,0])
		elif num == 3:
			self.m = np.array([-1,0,0])
		elif num == 4:
			self.m = np.array([0,-1,0])
		else:
			self.m = np.array([0,0,-1])
	def action(self):
		self.assign()
		self.s = self.s + self.m
		if self.s[0] == -1:
			self.s[0] = 0
		elif self.s[0] == self.l + 1 :
			self.s[0] = self.l
		if self.s[1] == -1:
			self.s[1] = 0
		elif self.s[1] == self.l + 1 :
			self.s[1] = self.l
		if self.s[2] == -1:
			self.s[2] = 0
		elif self.s[2] == self.l + 1 :
			self.s[2] = self.l
		self.moves = self.moves + 1
	def run(self):
		while not self.goal():
			self.action()
		#self.print_info()
	def print_info(self):
		print ("Envirnoment->3D moves taken = ",self.moves)
res1 = np.array([0,0,0,0,0,0,0,0,0])
res2 = np.array([0,0,0,0,0,0,0,0,0])
res3 = np.array([0,0,0,0,0,0,0,0,0])
for l in range(2,11):
	for i in range (0,101):
		e1 = Envirnoment1(l)
		e2 = Envirnoment2(l)
		e3 = Envirnoment3(l)
		e1.run()
		e2.run()
		e3.run()
		res1[l-2] += e1.moves
		res2[l-2] += e2.moves
		res3[l-2] += e3.moves
	res1[l-2] = res1[l-2] / 100
	res2[l-2] = res2[l-2] / 100
	res3[l-2] = res3[l-2] / 100
l = [2,3,4,5,6,7,8,9,10]
plt.plot(l , res1)
plt.plot(l , res2)
plt.plot(l , res3)
plt.xlabel('l')
plt.ylabel('moves')
plt.show()

