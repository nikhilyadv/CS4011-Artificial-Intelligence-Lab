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
outLis = []
tim = []
Domain = "01"
populationSize = 100
# assumption, a's have integer value and is a list
def f1 (a):
    sm = 0
    na = copy.deepcopy (a)
    for i in range (len (na)):
        na[i] = na[i] / 100
    for i in range (len (na)):
        sm = sm + na[i] * na[i]
    return sm
def f2 (a):
    sm = 0
    na = copy.deepcopy (a)
    for i in range (len (na)):
        na[i] = na[i] / 100
    for i in range (len (na)):
        sm = sm + math.floor (na[i])
    return sm
def gaussNoise ():
    return np.random.normal (0, 1)
def f3 (a):
    sm = 0
    na = copy.deepcopy (a)
    for i in range (len (na)):
        na[i] = na[i] / 100
    for i in range (len (na)):
        sm = sm + (i + 1) * (na[i] * na[i] * na[i] * na[i])
    sm = sm + gaussNoise ()
    return sm
def sum_ (a):
    return f1(a) + f2(a) + f3 (a)
def isNDS (index, Data):
    oz = f1 (Data[index].n)
    oo = f2 (Data[index].n)
    ot = f3 (Data[index].n)
    for i in range (len (Data)):
        if (i == index):
            continue
        z = f1 (Data[i].n)
        o = f2 (Data[i].n)
        t = f3 (Data[i].n)
        if (z < oz and o < oo and t < ot):
            return False
    return True

class Gene:
    def __init__ (self):
        self.n = [0 for i in range (5)]
        self.bin_ = [0 for i in range (5)]
        for i in range (5):
            self.n[i] = random.randint (-204, 205)
            self.bin_[i] = list ("{0:010b}".format (self.n[i]))
        self.nds = False
        self.fitness = sum_ (self.n)

    def __lt__ (self, other):
        if (self.nds and not (other.nds)):
            return True
        elif (other.nds and not (self.nds)):
            return False
        else:  # either both are nds or both are not nds, in either case we want to minimize the total loss
            return self.fitness < other.fitness
def Solve ():
    Data = []
    for i in range (0, populationSize):
        Data.append (Gene ())
    newLimit = int (0.5 * populationSize);  # Elitism
    offLimit = populationSize - newLimit
    global outLis
    outLis = []
    global tim
    tim = []
    tim.append (1)
    for i in range (len (Data)):
        if (isNDS (i, Data)):
            Data[i].nds = True
    Data.sort ()
    outLis.append (Data[0].fitness)
    toRet = Data[0].n
    return toRet
def plotit (n,k):
    plt.scatter (tim, outLis)
    plt.xlabel("epoch")
    plt.ylabel("fitness")
    plt.title("GA with Randomness N = %d"%n)
    plt.savefig ("Random" + str(k + 1) + ".png")
    plt.clf ()
    # plt.show ()
sys.stdin = open("in.txt", "r")
sys.stdout = open("out.txt", "w")
i = 0
for n in [50, 100, 200]:
    populationSize = n
    ans_ = Solve ()
    plotit (n,i)
    i += 1
