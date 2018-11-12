'''
Name - NIKHIL KUMAR YADAV
Fairly simple code just implemented policy and value iterations. I have organized my functions with help from sourabh
'''
from __future__ import print_function
import numpy as np
import pickle as pk
import copy
try:
	import Queue as Q  # ver. < 3.0
except ImportError:
	import queue as Q
import math
import random
import sys

N = 20
s = N*N
vmin = -0.07
vmax = 0.07
pmin = -1.2
pmax = 0.6
A = 3
Actions = np.array([-1,0,1])

def U (v, P, R, gamma, optimalk):  # Bellman operator
	rv = np.zeros((v.size))
	for i in range (0, v.size):
		mx = -1
		for k in range (0, A):  # action space
			sum_ = 0
			for l in range (0, s):
				sum_ += (P[k][i][l] * v[l])
			nw = R[i] + gamma * sum_
			if (nw > mx):
				optimalk[i] = k
				mx = nw
		rv[i] = mx
	return rv

def infNorm (v, newv):  # Infinite Norm
	diffMax = 0
	for i in range (0, v.size):
		diffMax = max (diffMax, abs (v[i] - newv[i]))
	return diffMax

def ValueIteration (P, R, s, gamma):  # Value iteration algo
	eps = 1e-6
	v = np.ones((s))
	optimalk = -1 * np.ones((s))
	newv = U (v, P, R, gamma, optimalk)
	while (infNorm (v, newv) > eps):
		v = newv
		newv = U (v, P, R, gamma, optimalk)
	Pi = getPfromK (P, optimalk)
	#print (newv)
	print (optimalk)

def getPfromK (P, optimalk):  # get policy from optimal actions
	Pi = np.zeros((optimalk.size,optimalk.size))		#s*s
	for i in range (0, optimalk.size):
		for j in range (0, optimalk.size):
			Pi[i][j] = P[int(optimalk[i])][i][j]
	return Pi

def notSame (A, B):  # takes as input 2 matrices and tells whether they are equal or not
	eps = 1e-6
	for i in range (0, s):			# policy s*s
		for j in range (0, s):
			if (abs (A[i][j] - B[i][j]) > eps):
				return True
	return False

def PolicyIteration (P, R, s, gamma):  # Policy iteration algo
	policyt = P[0]  # giving some initial policy
	policyt = np.asarray (policyt)
	I = np.identity (s, dtype = float)
	v = np.linalg.inv (I - gamma * policyt) @ R
    # print ("v")
    # print (v)
	optimalk = np.zeros((s))
	v = U (v, P, R, gamma, optimalk)
    # print (optimalk)
	policytp1 = getPfromK (P, optimalk)
	while (notSame (policyt, policytp1)):
		# print (optimalk)
		policyt = policytp1
		v = np.linalg.inv (I - gamma * policyt) @ R
		v = U (v, P, R, gamma, optimalk)
		policytp1 = getPfromK (P, optimalk)
	#print (v)
	print (optimalk)


def init():
	P = np.zeros((A,s,s))
	for i in range (0, A):  # action
		for k in range (0, N):  # position
			for j in range (0, N):  # velocity
				pat = pmin + k * (pmax - pmin) / (N - 1)
				vat = vmin + j * (vmax - vmin) / (N - 1)
				newv = vat + Actions[i] * 0.1 + math.cos (2 * pat) * (-.25)
				newp = pat + newv
				vindex = (newv - vmin) * (N - 1) / (vmax - vmin)
				pindex = (newp - pmin) * (N - 1) / (pmax - pmin)
				vindex = int (round (vindex))
				pindex = int (round (pindex))
				# print (vindex, pindex)
				if (vindex >= N):
					vindex = N - 1
				if (pindex >= N):
					pindex = N - 1
				P[i][k * N + j][pindex * N + vindex] = 1
	R = -1 * np.ones((s))
	temp = math.ceil ((0.55 - pmin) * (N - 1) / (pmax - pmin))
	for i in range (temp, N):
		for k in range (0, N):
			R [i * N + k] = 100
	gamma = 0.99
	print("Policy Iteration")
	PolicyIteration (P, R, s, gamma) 
	print("Value Iteration")
	ValueIteration (P, R, s, gamma)

init()