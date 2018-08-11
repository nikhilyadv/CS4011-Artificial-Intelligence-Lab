class Agent:
	'''Class to implement bunny functionality'''
	def __init__(self):
		self.location = 0		#To store relative position of the bunny
		self.moves = 0			#To count the moves.
		self.direction = 1		#To maintain the current direction
		self.counter = 1		#To check the max limit in each direction
		
	def action(self , percept):
		'''Simple logic to implement back and forth idea of traversal'''
		if percept == True :
			return
		if self.location < self.counter and self.direction == 1 :
			self.location += 1
		elif self.location == self.counter and self.direction == 1 :
			self.direction = -1
			self.location -= 1
		elif abs(self.location) < self.counter and self.direction == -1 :
			self.location -= 1
		else:
			self.direction = 1
			self.location += 1
			self.counter += 1 
		self.moves += 1

class Envirnoment:
	'''Class to implement the 1D line in which the bunny can move'''
	def __init__(self):
		self.shore = self.getshore()	#imput shore location
		self.agent = Agent()			#initialize bunny
		self.agentlocation = self.getlocation()	#get bunny's location

	def getlocation(self):
		return int(input("Enter Agents position - "))
	
	def getshore(self):
		return int(input("Enter shore location - "))

	def percept(self):
		'''Check whether shore is reached or not'''
		if self.agent.location + self.agentlocation == self.shore :
			return True
		return False
	
	def print_info(self):	#function to print the result
		location = self.agent.location + self.agentlocation
		print(location, '\t', self.agent.moves, '\t', self.percept(), '\t', self.agent.direction, '\t', self.shore)

	def simulate(self):
		'''Function to simulate the envirnoment and agent functioning'''
		while not self.percept() :
			self.agent.action(self.percept())
			self.print_info()
#start
envi = Envirnoment()
envi.simulate()