import numpy as np
import queue
import copy

class n2puzzle :					# puzzle board
	def __init__(self):
		self.n = int(input())
		self.position = [0,0]
		self.a = self.getarray()
		self.goal = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])
		self.print_info()
		#self.check()
		self.bfs()

	def getarray(self):
		a = np.zeros([self.n,self.n],dtype = int)
		for i in range(0,self.n):
			for j in range(0,self.n):
				a[i][j] = i*self.n + j + 1         #int(input())
		red = [int(input()),int(input())]
		self.position = [int(input()), int(input())]
		a[red[0]][red[1]] = a[0][self.n - 1]
		a[0][self.n-1] = red[0]*self.n + red[1] + 1
		a[self.n-1][self.n-1] = a[self.position[0]][self.position[1]]
		a[self.position[0]][self.position[1]] = 0
		return a

	def check(self):
		if self.checkparityn2() == True:
			print("Solvable")
		else:
			print("Not Solvable")

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

	def isgoal(self):
		if self.a[0][self.n-1] == 4:
			return True
		return False
		# return np.array_equal(self.a,self.goal)

	def bfs(self):
		q = queue.Queue()
		visited = {}
		path = []
		q.put((copy.deepcopy(self.a),copy.deepcopy(self.position),copy.deepcopy(path)))
		while not q.empty() :
			self.a , self.position , path = q.get()
			if self.isgoal():
				print("Min steps = ",len(path))
				print(path)
				return True
			arr = self.a.flatten()
			visited[arr.tostring()] = 1
			if self.up():
				arr = self.a.flatten()
				if not arr.tostring() in visited:
					p = copy.deepcopy(path)
					p.append('U')
					q.put((copy.deepcopy(self.a),copy.deepcopy(self.position),p))
				self.down()
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
