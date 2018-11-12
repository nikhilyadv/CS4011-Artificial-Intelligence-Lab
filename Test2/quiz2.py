import numpy as np
import matplotlib.pyplot as plt
import random
from itertools import permutations

def unique_perms(series):
	return {"".join(p) for p in permutations(series)}

permutation = sorted(unique_perms('1122334455'))

wickets = 3
overs = 10
economy = [3,3.5,4,4.5,5]
strike = [33,30,24,18,15]
# oversleft = [2,2,2,2,2]
policy = np.ones(10) * -1

def init(v):
	for i in range(overs):
		v[0][i+1] = 0
	for i in range(wickets):
		v[i+1][0] = 0

def bellman(v,wicketsleft,oversleft,order):
	if wicketsleft == 0 or oversleft == 0:
		return 0
	maximum = -1
	bolwer = (int(order[10-oversleft])-1)
	# print(bolwer)
	pout = (6/strike[bolwer])
	value = economy[bolwer] + pout * v[wicketsleft-1][oversleft-1] + (1-pout) * v[wicketsleft][oversleft-1]
	return value

def main():
	oversleft = [2, 2, 2, 2, 2]
	#print(v)
	#print(policy)
	policy = ""
	min = 1e10
	# print(permutation[0])
	# bellman([],2,3,permutation[0])
	# v = np.ones((wickets + 1, overs + 1)) * -1
	# init(v)
	# for i in range(1, 4):
	# 	for j in range(1, 11):
	# 		v[i][j] = bellman(v, i, j, permutation[0])
	# for i in range(10):
	# 	print(permutation[i])
	for i in range(len(permutation)):
		v = np.ones((wickets + 1, overs + 1)) * -1
		init(v)
		for j in range(1,4):
			for k in range(1,11):
				v[j][k] = bellman(v,j,k,permutation[i])
		if (v[3][10] < min):
			policy = permutation[i]
			min = v[3][10]
	print(policy)
	print(min)
if __name__ == "__main__":
	main()