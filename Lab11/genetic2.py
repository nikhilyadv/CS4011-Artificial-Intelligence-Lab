from __future__ import print_function
import numpy as np
import pickle as pk
import copy
try:
	import Queue as Q
except ImportError:
	import queue as Q
import math
import random
import sys

population_size = 100
GENES = "01"
#GOAL = "Nikhil loves genetic Algorithm"

class Human:
	def __init__(self,x):
		self.x = x#self.bintoint()
		if x >= 0:
			self.flag = True 
		else:
			self.flag = False
		self.chromosome = self.InttoBin()
		self.fitness = self.get_fitness()

	def InttoBin(self):
		temp = abs(self.x)
		string = []
		mask = 1
		for i in range(0,40):
			if((mask&temp) >= 1):
				string = ['1'] + string
			else:
				string = ['0'] + string
			mask<<=1
		return string

	def f1(self,x):
		return x * x

	def f2(self,x):
		return (x-2) * (x-2)

	def get_fitness(self):
		self.fit = (self.f1(self.x),self.f2(self.x))
		return self.fit[0]+self.fit[1]
		# count = 0
		# for p , q in zip(self.chromosome,GOAL):
		# 	if p!=q:
		# 		count += 1
		# return count

	# @classmethod
	# def get_random(self,start,end):
	# 	return random.randint(start,end)
	@classmethod
	def BintoInt(self,chromosome,flag):
		num = 0
		for i in range(0,40):
			if chromosome[40-i-1] == '1':
				num += math.pow(2,i)
		if not flag:
			num = num * -1
		return int(num)

	@classmethod
	def mutate_gene(self):
		return random.choice(GENES);

	@classmethod
	def create_gene(self):
		#return self.BintoInt([self.mutate_gene() for _ in range(40)],random.randint(0,1))
		return random.randint(-100,100)
		# gene = ""
		# for i in range(0,len(GOAL)):
		# 	gene += self.mutate_gene()
		# return gene

	def mate(self,parent2):
		child = []
		for p , q in zip(self.chromosome,parent2.chromosome):
			prob = random.random()
			if prob < 0.4:
				child.append(p)
			elif prob < 0.8:
				child.append(q)
			else:
				child.append(self.mutate_gene())
		prob = random.random()
		if prob < 0.5:
			return Human(Human.BintoInt(child,self.flag))
		return Human(Human.BintoInt(child,parent2.flag))

def main():
	generation = 1
	found = False
	population = []

	for _ in range(population_size):
		gnome = Human.create_gene()
		population.append(Human(gnome))

	while not found:
		population = sorted(population, key = lambda x:x.fitness) 

		if population[0].fitness <= 0 or generation == 100:
			found = True
			break

		new_generation = []

		s = int((1*population_size)/10)
		for _ in range(s):
			new_generation.extend(population[:s])

		s = int((9*population_size)/10)
		for _ in range(s):
			p1 = random.choice(population[:50])
			p2 = random.choice(population[:50])
			child = p1.mate(p2)
			new_generation.append(child)

		population = new_generation

		print("Generation : ",generation,"\tString : ","".join(population[0].chromosome),"\tFitness : ",population[0].fitness)

		generation += 1

	print("Generation : ",generation,"\tString : ","".join(population[0].chromosome),"\tFitness : ",population[0].fitness)

if __name__ == '__main__':
	main()
	# x = Human.create_gene()
	# x = 7
	# print(x ," ",Human(x).chromosome)
	# x = -7
	# print(x ," ",Human(x).chromosome)