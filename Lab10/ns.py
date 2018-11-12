"""
Author: Sourabh Aggarwal (111601025)
Description: Not much to say, simply applying value iteration and policy iteration algorithm. See comments for more details. Note: In this code, since our probability matrix is highly sparse so I am simply hashing the state, action pair to a new state.
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
import matplotlib.pyplot as plt
#sys.stdin = open("testData.txt", "r")
# sys.stdout = open("outData.txt", "w")
# Global Data
G = 100
vmin = -0.07
vmax = 0.07
pmin = -1.2
pmax = 0.6
A = 3
mp = {}
canPrint = True
def nextState (l, i):  # 'l' is state and 'i' is action
    x = l // G
    y = l % G
    pat = pmin + x * (pmax - pmin) / (G - 1)
    vat = vmin + y * (vmax - vmin) / (G - 1)
    nwv = vat + mp[i] * 0.001 + math.cos (3 * pat) * (-.0025)
    nwp = pat + nwv
    vindex = (nwv - vmin) * (G - 1) / (vmax - vmin)
    pindex = (nwp - pmin) * (G - 1) / (pmax - pmin)
    vindex = int (round (vindex))
    pindex = int (round (pindex))
    vindex = max (0, min (vindex, G - 1))
    pindex = max (0, min (pindex, G - 1))
    return (pindex * G + vindex)
def printMat (data):  # auxilary function to just print the elements of the matrix
    print ("----------------------------------")
    for i in range (0, len (data)):
        for j in range (0, len (data[i])):
            print (data[i][j], end = ' ')
        print ("")
    print ("---------------------------------")
def U (v, R, s, gamma, optimalk):  # Bellman operator
    rv = [0 for i in range (0, len (v))]
    for i in range (0, s):
        mx = -1
        for k in range (0, A):  
            ns = nextState (i, k)
            nw = R[i] + gamma * (v[ns])
            if (nw > mx):
                optimalk[i] = k
                mx = nw
        rv[i] = mx
    return rv

def Upi (v, R, gamma, optimalk):  # Bellman operator fixed to a policy
    rv = [0 for i in range (0, len (v))]
    for i in range (0, len (optimalk)):
        rv[i] = R[i] + gamma * v[nextState (i, optimalk[i])]
    return rv

def infNorm (v, nv):  # Infinite Norm
    diffMax = -1
    for i in range (0, len (v)):
        diffMax = max (diffMax, abs (v[i] - nv[i]))
    return diffMax
markers = ['*', '<', '>']
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
    v = np.array (v)
    v = v.reshape (G, G)
    plt.imshow (v)
    plt.show ()
    for i in range (A):
        plt.scatter (p_[i], v_[i], marker = markers[i], s = 10)
        # plt.scatter (pat, vat, marker = markers[optimalk[i]], c = 'blue', s = 200)
    plt.show ()
def SolveValueIteration (R, s, gamma):  # Value iteration algo
    eps = 1e-2
    v = [1 for i in range (0, s)]
    optimalk = [-1 for i in range (0, s)]
    nv = U (v, R, s, gamma, optimalk)
    neps = infNorm (v, nv)
    i = 0
    while (neps > eps):
        print (i)
        v = nv
        nv = U (v, R, s, gamma, optimalk)
        neps = infNorm (v, nv)
        print (neps)
        i = i + 1
    PrintNice (nv, optimalk)
    # if (canPrint):
    #     print (nv)
    #     print (optimalk)
    return copy.deepcopy (optimalk)
def notSame (A, B):  # takes as input 2 matrices and tells whether they are equal or not
    eps = 1e-6
    for i in range (0, len (A)):
        for j in range (0, len (A[i])):
            if (abs (A[i][j] - B[i][j]) > eps):
                return True
    return False
def GetVfromOptimalK (optimalk, R, gamma):  # get stationary point wrt optimalk
    v = [0 for i in range (0, len (optimalk))]
    eps = 1e-6
    nv = [0 for i in range (0, len (optimalk))]
    while (True):
        nv = Upi (v, R, gamma, optimalk)
        if (infNorm (v, nv) <= 1e-2):
            break
        v = nv
    return nv
def SolvePolicyIteration (R, s, gamma):  # Policy iteration algo
    eps = 1e-6
    poptimalk = [0 for i in range (0, s)]
    v = GetVfromOptimalK (poptimalk, R, gamma)
    noptimalk = copy.deepcopy (poptimalk)
    cnter = 0
    while (True):
        print (cnter)
        U (v, R, s, gamma, noptimalk)
        v = GetVfromOptimalK (noptimalk, R, gamma)
        neps = infNorm (noptimalk, poptimalk)
        print (neps)
        if (neps <= eps):
            break
        poptimalk = copy.deepcopy (noptimalk) 
        cnter = cnter + 1
    PrintNice (v, noptimalk)
    # if (canPrint):
    #     print (v)
    #     print (noptimalk)
    return copy.deepcopy (noptimalk)
# def SimulateGame (P, R, s, optimalk):
    
def initial ():  # Sets up various input data
    global mp
    mp[0] = 0
    mp[1] = -1
    mp[2] = 1
    s = G * G  # state space
    """ Every position can be written as pmin + k * (pmax - pmin) / (G - 1) where k varies from 0 to G - 1. Similarly we have for velocity. So say state is (x, y) where x is position index and y is velocity index then f (x, y) = x * G + y is a unique bijective function. Note: (G - 1) * G + (G - 1) = G * G - 1. And it starts from 0.  """
    R = [0 for i in range (s)]
    temp = math.ceil ((0.55 - pmin) * (G - 1) / (pmax - pmin))
    for i in range (temp, G):
        for k in range (0, G):
            R [i * G + k] = 1
    gamma = 0.99
    # SolvePolicyIteration (R, s, gamma)  
    SolveValueIteration (R, s, gamma)
# sys.stdin = open("testData.txt", "r")
# sys.stdout = open("outData1.txt", "w")    
initial ()