class Agent:
	'''Class to count the words'''
	def __init__(self):
		self.words = 0
		self.previous = 0
	def action(self , percept):
		if percept == " " and self.previous == 1:
			self.words += 1
			self.previous = 0
		if not(percept == " ") :
			self.previous = 1
class Envirnoment:
	'''Class to open the file and read its content one by one'''
	def __init__(self , name):
		self.file = open(name , "r")
		self.index = 0
		self.agent = Agent()
	def percept(self):		#reading a character
		return self.file.read(1)
	def run(self):
		per = self.percept()
		while not per == "":		#checking end of file
			self.agent.action(per)
			per = self.percept()
		if self.agent.previous == 1:		#if there is a last word without space
			self.agent.action(" ")
		self.print_info()
	def print_info(self):				#function to print the result
		print ("Number of words = ", self.agent.words)
#start
envi = Envirnoment(input("Enter name of the file - "))
envi.run()