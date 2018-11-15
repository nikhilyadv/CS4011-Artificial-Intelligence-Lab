from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
try:
	import Queue as Q
except ImportError:
	import queue as Q
import math
import random
import sys

population_size = 100
GENES = "01"

class Human:
	def __init__(self,x):
		self.x = x#self.bintoint()
		self.flag = [True for _ in range(5)]
		for i in range(5):
			if x[i] >= 0:
				self.flag[i] = True
			else:
				self.flag[i] = False
		self.chromosome = self.InttoBin()
		# print(self.BintoInt(self.chromosome, self.flag))
		self.fitness = self.get_fitness()

	def InttoBin(self):
		temp = [0 for _ in range(5)] #= abs(self.x)
		for i in range(5):
			temp[i] = math.floor(abs(self.x[i]))
		string = [[] for _ in range(5)]
		for i in range(5):
			mask = 1
			for j in range(0,2):
				if((mask&temp[i]) >= 1):
					string[i] = ['1'] + string[i]
				else:
					string[i] = ['0'] + string[i]
				mask<<=1
		# temp = [0.0 for _ in range(5)]
		for i in range(5):
			temp[i] = math.floor((abs(self.x[i]) - math.floor(abs(self.x[i])))*100)
		for i in range(5):
			mask = 1
			for j in range(0,8):
				if((mask&temp[i]) >= 1):
					string[i] = ['1'] + string[i]
				else:
					string[i] = ['0'] + string[i]
				mask<<=1
		return string

	def f1(self,x):
		sum = 0
		for i in range(0,5):
			sum += x[i]*x[i]
		return sum

	def f2(self,x):
		sum = int(0)
		for i in range(0,5):
			sum += int(x[i])
		return sum

	def f3(self,x):
		sum = 0
		for i in range(0,5):
			sum += i * math.pow(x[i],4)
		sum += np.random.normal(loc=0,scale=1)
		return sum

	def get_fitness(self):
		self.fit = (self.f1(self.x),self.f2(self.x),self.f3(self.x))
		return self.fit[0]+self.fit[1]+self.fit[2]
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
		num = [0 for _ in range(5)]
		fl = [0 for _ in range(5)]
		for i in range(5):
			for j in range(0,2):
				if chromosome[i][10-j-1] == '1':
					num[i] += math.pow(2,j)
		for i in range(5):
			for j in range(0,8):
				if chromosome[i][8-j-1] == '1':
					fl[i] += math.pow(2,j)
		for i in range(5):
			num[i] = (num[i] + fl[i] / 100)
			if not flag[i]:
				num[i] = num[i] * -1
		return num

	@classmethod
	def mutate_gene(self):
		return random.choice(GENES)

	@classmethod
	def create_gene(self):
		#return self.BintoInt([self.mutate_gene() for _ in range(40)],random.randint(0,1))
		x = [i for i in range(5)]
		for i in range(5):
			x[i] = (np.random.random()-0.5)*2.04*2
		return x

	def mate(self,parent2):
		child = [[] for i in range(5)]
		for i in range(5):
			for p , q in zip(self.chromosome[i],parent2.chromosome[i]):
				prob = random.random()
				if prob < 0.49:
					child[i].append(p)
				elif prob < 0.98:
					child[i].append(q)
				else:
					child[i].append(self.mutate_gene())
		prob = random.random()
		if prob < 0.5:
			return Human(Human.BintoInt(child,self.flag))
		return Human(Human.BintoInt(child,parent2.flag))

def main():
	generation = 1
	found = False
	population = []
	fitplot = []
	for _ in range(population_size):
		gnome = Human.create_gene()
		population.append(Human(gnome))

	while not found:
		population = sorted(population, key = lambda x:x.fitness)	 #sorted using the tuple the fitness

		if generation == 500:
			found = True
			break

		new_generation = []

		s = int((1*population_size)/10)
		for _ in range(s):
			new_generation.extend(population[:s])

		s = int((9*population_size)/10)
		# s = int((10*population_size)/10)
		for _ in range(s):
			p1 = random.choice(population[:50])
			p2 = random.choice(population[:50])
			child = p1.mate(p2)
			new_generation.append(child)

		population = new_generation
		# population = sorted(population, key = lambda x:x.fitness)
		print("Generation : ",generation,"\tFitness : ",population[0].fitness)
		fitplot.append(population[0].fitness)
		generation += 1

	print("Generation : ",generation,"\tFitness : ",population[0].fitness)
	plt.plot(range(generation-1),fitplot)
	plt.ylabel("Fitness value")
	plt.xlabel("epoch")
	plt.title("N = 100, mutation = 0.02 without elitism")
	plt.show()

if __name__ == '__main__':
	main()
