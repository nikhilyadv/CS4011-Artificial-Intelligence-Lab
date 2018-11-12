import numpy as np
import math
import matplotlib.pyplot as plt
import random

y = 0.9

def prob(n,l):
	return (math.pow(l,n)*math.exp(-l)/math.factorial(n))

v = np.zeros((20,10,10))
action = np.zeros((20,10,10))

def infNorm (v, nv):  # Infinite Norm
	diffMax = -1
	for i in range (0, len (v)):
		diffMax = max (diffMax, abs (v[i] - nv[i]))
	return diffMax


def U(v,optimalk):


def valueiteration():
	eps = 0.1
	v = np.zeros((20,10,10))
	optimalk = np.zeros((20,10,10))
	nv = U(v,optimalk)
	while(infnorm(v,nv) > 0.1):
		pass

def main():
	pass

if __name__ == "__main__":
	main()