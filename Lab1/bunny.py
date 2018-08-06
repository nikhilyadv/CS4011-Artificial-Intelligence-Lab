class Agent:
	def __init__(self):
		self.location = 0
		self.moves = 0
		self.direction = 1
		self.counter = 1
		
	def action(self , percept):
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
	def __init__(self):
		self.shore = self.getshore()
		self.agent = None
		self.agentlocation = self.getlocation()

	def getlocation(self):
		return int(input("Enter Agents position - "))
	
	def getshore(self):
		return int(input("Enter shore location - "))

	def percept(self):
		if self.agent.location + self.agentlocation == self.shore :
			return True
		return False
	
	def printinfo(self):
		location = self.agent.location + self.agentlocation
		print(location, '\t', self.agent.moves, '\t', self.percept(), '\t', self.agent.direction, '\t', self.shore)

	def simulate(self):
		while not self.percept() :
			self.agent.action(self.percept())
			self.printinfo()

envi = Envirnoment()
bunny = Agent()
envi.agent = bunny
envi.simulate()