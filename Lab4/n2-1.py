import numpy as np
import math
from random import randint
import matplotlib.pyplot as plt

class segtree:						# class for segtree
	def __init__(self,n):
		self.n = n
		self.a = np.zeros(4*n)
		#for i in range(0,n):
		#	self.a[n+i] = arr[i]
		#self.build()

	def build(self):
		for i in range(self.n-1,0,-1):
			self.a[i] = self.a[i<<1] + self.a[i<<1 | 1]

	def update(self,index,value):
		index += self.n
		self.a[index] = value
		i = index
		while i > 1:
			self.a[i>>1] = self.a[i] + self.a[i^1]
			i >>= 1


	def query(self,l,r):		#from l to r-1
		res = 0
		l += self.n
		r += self.n
		while l < r:
			if l&1 :
				res += self.a[l]
				l += 1
			if r&1 :
				r -= 1
				res += self.a[r]
			l >>= 1
			r >>= 1
		return res


class n2puzzle :					# puzzle board
	def __init__(self):
		self.n = int(input())
		self.position = [0,0]
		self.a = self.getarray()
		#self.final = self.getarray()	"Enter n - "
		self.print_info()

	def getarray(self):
		a = np.zeros([self.n,self.n],dtype = int)
		for i in range(0,self.n):
			for j in range(0,self.n):
				a[i][j] = int(input())
				if a[i][j] == 0:
					self.position = [i,j]
		return a

	def check(self):
		if self.checkparityn2() == True:		
			print("Solvable")
		else:
			print("Not Solvable")

	def checkparityn4(self):			# using 2 loops
		arr = self.a.flatten()
		inversions = 0
		for i in range(0,self.n*self.n - 1):
			for j in range(i+1,self.n*self.n):
				if arr[i] and arr[j] and arr[i] > arr[j] :
					inversions += 1
		if self.n % 2 == 0:
			pos = 0
			for i in range(0,self.n):
				for j in range(0,self.n):
					if self.a[i][j] == 0:
						pos = (self.n-i) % 2
			if pos % 2 == 0 and inversions % 2 == 1:
				return True
			if pos % 2 == 1 and inversions % 2 == 0:
				return True
		else :
			if inversions % 2 == 0:
				return True
		return False

	def checkparityn2logn(self):		# using segtrees
		arr = self.a.flatten()
		arr = arr.tolist()
		zeropos = self.n - self.position[0] - 1 + self.n - self.position[1] - 1
		arr.remove(0)
		n = len(arr)
		seg = segtree(n)
		res = 0
		for i in range(0,n):
			seg.update(arr[i],1)
			res += arr[i] -seg.query(0,arr[i])
		res += zeropos
		parity = res % 2
		if parity:
			return True
		return False

	def checkparityn2(self):			# using cycle check method
		arr = self.a.flatten().tolist()
		arr.remove(0)
		n = len(arr)
		visited = np.zeros(n)
		counter = 0
		cycles = 0
		for i in range(0,n):
			if not visited[i]:
				counter = i
				while not visited[counter]:
					visited[counter] = 1
					counter = arr[counter] - 1
				cycles += 1
		parity = (n + 1 - cycles) % 2
		if parity:
			return True
		return False

	def up(self):						#valid moves for the board
		i = self.position[0]
		j = self.position[1]
		if i > 0 :
			self.a[i][j] = self.a[i-1][j]
			self.a[i-1][j] = 0
			self.position[0] = i - 1
			return True
		return False

	def down(self):
		i = self.position[0]
		j = self.position[1]
		if i < self.n - 1 :
			self.a[i][j] = self.a[i+1][j]
			self.a[i+1][j] = 0
			self.position[0] = i + 1
			return True
		return False
	
	def right(self):
		i = self.position[0]
		j = self.position[1]
		if j < self.n - 1 :
			self.a[i][j] = self.a[i][j+1]
			self.a[i][j+1] = 0
			self.position[1] = j + 1
			return True
		return False

	def left(self):
		i = self.position[0]
		j = self.position[1]
		if j > 0 :
			self.a[i][j] = self.a[i][j-1]
			self.a[i][j-1] = 0
			self.position[1] = j - 1
			return True
		return False

	def print_info(self):
		print(self.a)
		print("Pos - ",self.position)
		
envi = n2puzzle()
envi.check()
