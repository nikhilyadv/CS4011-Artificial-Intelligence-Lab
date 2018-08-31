import numpy as np
import queue
import copy

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
		self.a = self.getarray()													#input array
		self.goal = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])		#goal state or final configuration
		self.print_info()
		if self.check():															#perform bfs only if the parity of input is correct
			self.bfs()

	def getarray(self):
		a = np.zeros([self.n,self.n],dtype = int)
		for i in range(0,self.n):
			for j in range(0,self.n):
				a[i][j] = int(input())
				if a[i][j] == 0:
					self.position = [i,j]
		return a

	def check(self):
		if self.checkparityn2logn() == True:
			print("Solvable")
			return True
		print("Not Solvable")
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

	def isgoal(self):
		return np.array_equal(self.a,self.goal)

	def bfs(self):
		q = queue.Queue()			#FIFO queue
		visited = {}				#dict to hash
		path = []					#to store final path or moves
		q.put((copy.deepcopy(self.a),copy.deepcopy(self.position),copy.deepcopy(path)))	#position of zero is stored to avoid unnecessary n^2 caculation per node
		while not q.empty() :
			self.a , self.position , path = q.get()
			if self.isgoal():						#checking whether the current state is goal or not
				print(path)							#printing the path
				return True
			arr = self.a.flatten()	
			visited[arr.tostring()] = 1				#hashing
			if self.up():							#check and move if possible
				arr = self.a.flatten()
				if not arr.tostring() in visited:
					p = copy.deepcopy(path)
					p.append('U')
					q.put((copy.deepcopy(self.a),copy.deepcopy(self.position),p))
				self.down()								#re-doing the move
			if self.left():
				arr = self.a.flatten()
				if not arr.tostring() in visited:
					p = copy.deepcopy(path)
					p.append('L')
					q.put((copy.deepcopy(self.a), copy.deepcopy(self.position), p))
				self.right()
			if self.right():
				arr = self.a.flatten()
				if not arr.tostring() in visited:
					p = copy.deepcopy(path)
					p.append('R')
					q.put((copy.deepcopy(self.a), copy.deepcopy(self.position), p))
				self.left()
			if self.down():
				arr = self.a.flatten()
				if not arr.tostring() in visited:
					p = copy.deepcopy(path)
					p.append('D')
					q.put((copy.deepcopy(self.a), copy.deepcopy(self.position), p))
				self.up()
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
