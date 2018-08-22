import numpy as np
import math
from random import randint
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

class navigation:				#storing the grid and related information
	def __init__(self):
		self.n = 100
		#self.grid = getarray()
		self.grid = np.array(np.random.randint(0, 6, (100, 100)) == np.zeros((100, 100)), dtype = np.int32)			#generating random grid
		print(self.grid)
		#self.goal = [int(input()),int(input())]

	def getarray(self):
		a = np.zeros([self.n,self.n])
		for i in range(0,self.n):
			for j in range(0,self.n):
				a[i][j] = int(input())
		return a
envi = navigation()