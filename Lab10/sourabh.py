"""
Author: Sourabh Aggarwal (111601025)
Description: Not much to say, simply applying value iteration and policy iteration algorithm. See comments for more details.
"""
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
# Global Data
G = 50
vmin = -0.07
vmax = 0.07
pmin = -1.2
pmax = 0.6
A = 3
mp = {}

def printMat (data):  # auxilary function to just print the elements of the matrix
    print ("----------------------------------")
    for i in range (0, len (data)):
        for j in range (0, len (data[i])):
            print (data[i][j], end = ' ')
        print ("")
    print ("---------------------------------")
def U (v, P, R, gamma, optimalk):  # Bellman operator
    rv = [0 for i in range (0, len (v))]
    for i in range (0, len (v)):
        mx = -1
        for k in range (0, len (P)):  # assumption, len (P) is A
            sum_ = 0
            for l in range (0, G * G):
                sum_ += (P[k][i][l] * v[l])
            nw = R[i] + gamma * sum_
            if (nw > mx):
                optimalk[i] = k
                mx = nw
        rv[i] = mx
    return rv

def infNorm (v, nv):  # Infinite Norm
    diffMax = -1
    for i in range (0, len (v)):
        diffMax = max (diffMax, abs (v[i] - nv[i]))
    return diffMax
def SolveValueIteration (P, R, s, gamma):  # Value iteration algo
    eps = 1e-6
    v = [1 for i in range (0, s)]
    optimalk = [-1 for i in range (0, s)]
    nv = U (v, P, R, gamma, optimalk)
    #while (infNorm (v, nv) > eps):
    for c in range(1000):
        print(c)
        v = nv
        nv = U (v, P, R, gamma, optimalk)
    Pi = getPFromK (P, optimalk)
    print (nv)
    PrintNice(nv,optimalk)
    # printMat (Pi)
def getPFromK (P, optimalk):  # get policy from optimal actions
    Pi = [[0 for i in range (0, len (optimalk))] for j in range (0, len (optimalk))] 
    for i in range (0, len (optimalk)):
        for j in range (0, len (optimalk)):
            Pi[i][j] = P[optimalk[i]][i][j]
    Pi = np.asarray (Pi)
    return Pi
def notSame (A, B):  # takes as input 2 matrices and tells whether they are equal or not
    eps = 1e-6
    for i in range (0, len (A)):
        for j in range (0, len (A[i])):
            if (abs (A[i][j] - B[i][j]) > eps):
                return True
    return False
def SolvePolicyIteration (P, R, s, gamma):  # Policy iteration algo
    policyt = P[0]  # giving some initial policy
    policyt = np.asarray (policyt)
    I = np.identity (s, dtype = float)
    v = np.linalg.inv (I - gamma * policyt) @ R
    # print ("v")
    # print (v)
    optimalk = [0 for i in range (0, s)]
    U (v, P, R, gamma, optimalk)
    # print (optimalk)
    policytp1 = getPFromK (P, optimalk)
    while (notSame (policyt, policytp1)):
        # print (optimalk)
        policyt = policytp1
        v = np.linalg.inv (I - gamma * policyt) @ R
        U (v, P, R, gamma, optimalk)
        policytp1 = getPFromK (P, optimalk)
    print (v)
    print (optimalk)
    # printMat (policytp1)
def PrintNice (v, optimalk):
   p_ = [[] for i in range (A)]
   v_ = [[] for i in range (A)]
   print ("this is ")
   print (len (v))

   for i in range (len (v)):
       x = i // G
       y = i % G
       pat = pmin + x * (pmax - pmin) / (G - 1)
       vat = vmin + y * (vmax - vmin) / (G - 1)
       p_[optimalk[i]].append (pat)
       v_[optimalk[i]].append (vat)
   # print ("Done")
   # print (p[0])
   # print (p[1])
   # print (p[2])
   for i in range (A):
       plt.scatter (p_[i], v_[i], marker = markers[i], s = 10)
       # plt.scatter (pat, vat, marker = markers[optimalk[i]], c = 'blue', s = 200)
   plt.show ()
def initial ():  # Sets up various input data
    global mp
    mp[0] = -1
    mp[1] = 0
    mp[2] = 1
    s = G * G  # state space
    P = [[[0 for i in range (0, s)] for j in range (0, s)] for k in range (A)]  # A * state * state
    for i in range (0, A):  # action
        for k in range (0, G):  # position
            for j in range (0, G):  # velocity
                pat = pmin + k * (pmax - pmin) / (G - 1)
                vat = vmin + j * (vmax - vmin) / (G - 1)
                nv = vat + mp[i] * 0.001 + math.cos (3 * pat) * (-.0025)
                np = pat + nv
                vindex = (nv - vmin) * (G - 1) / (vmax - vmin)
                pindex = (np - pmin) * (G - 1) / (pmax - pmin)
                vindex = int (round (vindex))
                pindex = int (round (pindex))
                # print (vindex, pindex)
                if (vindex >= G):
                    vindex = G - 1
                if (pindex >= G):
                    pindex = G - 1
                P[i][k * G + j][pindex * G + vindex] = 1
        # printMat (P[i])
    s = G * G
    # printMat (P)
    R = [0 for i in range (s)]
    temp = math.ceil ((0.55 - pmin) * (G - 1) / (pmax - pmin))
    for i in range (temp, G):
        for k in range (0, G):
            R [i * G + k] = 1
    # print (R)
    gamma = 0.99
    #SolvePolicyIteration (P, R, s, gamma)  
    SolveValueIteration (P, R, s, gamma)
initial ()