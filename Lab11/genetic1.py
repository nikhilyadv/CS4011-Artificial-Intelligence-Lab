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

population_size = 50
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
GOAL = "Nikhil loves genetic Algorithm"

class Human:
	def __init__(self,chromosome):
		self.chromosome = chromosome
		self.fitness = self.get_fitness()

	def get_fitness(self):
		count = 0
		for p , q in zip(self.chromosome,GOAL):
			if p!=q:
				count += 1
		return count

	# @classmethod
	# def get_random(self,start,end):
	# 	return random.randint(start,end)

	@classmethod
	def mutate_gene(self):
		return random.choice(GENES);

	@classmethod
	def create_gene(self):
		return [self.mutate_gene() for _ in range(len(GOAL))]
		# gene = ""
		# for i in range(0,len(GOAL)):
		# 	gene += self.mutate_gene()
		# return gene

	def mate(self,parent2):
		child = []
		for p , q in zip(self.chromosome,parent2.chromosome):
			prob = random.random()
			if prob < 0.45:
				child.append(p)
			elif prob < 0.9:
				child.append(q)
			else:
				child.append(self.mutate_gene())
		return Human(child)

def main():
	generation = 1
	found = False
	population = []

	for _ in range(population_size):
		gnome = Human.create_gene()
		population.append(Human(gnome))

	while not found:
		population = sorted(population, key = lambda x:x.fitness) 

		if population[0].fitness <= 0:
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