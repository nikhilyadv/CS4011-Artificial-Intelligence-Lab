import numpy as np
import copy
import math
import random
import matplotlib.pyplot as plt

GENE = "01"
yaxis = []

def f1 (x):
    s = 0
    na = copy.deepcopy(x)
    for i in range(len(na)):
        na[i] = na[i] / 100
    for i in range(len(na)):
        s = s + na[i] * na[i]
    return s

def f2 (x):
    s = 0
    na = copy.deepcopy(x)
    for i in range(len(na)):
        na[i] = na[i] / 100
    for i in range(len(na)):
        s = s + math.floor(na[i])
    return s

def Noise (mean,sigma):
    return np.random.normal(mean, sigma)

def f3 (x):
    s = 0
    na = copy.deepcopy(x)
    for i in range(len(na)):
        na[i] = na[i] / 100
    for i in range(len(na)):
        s = s + (i + 1) * (na[i] * na[i] * na[i] * na[i])
    return s + Noise(0,1)


def fit (x):
    return f1(x) + f2(x) + f3 (x)

def isNDS (ii, pop_):
    aa = f1 (pop_[ii].n)
    bb = f2 (pop_[ii].n)
    cc = f3 (pop_[ii].n)
    for i in range(len(pop_)):
        if (i == ii):
            continue
        a = f1 (pop_[i].n)
        b = f2 (pop_[i].n)
        c = f3 (pop_[i].n)
        if (a < aa and b < bb and c < cc):
            return False
    return True

class Gene:
    def __init__ (self):
        self.n = [0 for i in range (5)]
        self.binary = [0 for i in range (5)]
        for i in range (5):
            self.n[i] = random.randint(-204, 205)
            self.binary[i] = list ("{0:010b}".format (self.n[i]))
        self.nds = False
        self.fitness = fit (self.n)

    def __lt__ (self, other):
        if (self.nds and not (other.nds)):
            return True
        elif (other.nds and not (self.nds)):
            return False
        else:  
            return self.fitness < other.fitness

def Mate (pa, pb):
    child = Gene ()
    for j in range (5):
        for i in range (len (child.binary[j])):
            pr = np.random.randint (1, 101)
            if (pr < CrossOverProb / 2):
                child.binary[j][i] = pa.binary[j][i]
            elif (pr < CrossOverProb):
                child.binary[j][i] = pb.binary[j][i]
            else:
                child.binary[j][i] = GENE[np.random.randint(0, len(GENE))];
        child.n[j] = int (''.join (child.binary[j]), 2)
        child.fitness = fit (child.n)
    return child

def Iterate(Maxgen):
    Population = []
    for i in range(0, PopSize):
        Population.append(Gene())
    newLimit = int(0.3 * PopSize);  
    uplimit = PopSize - newLimit
    global yaxis
    yaxis = []
    for gen in range(0, Maxgen):
        for i in range(len(Population)):
            if(isNDS(i, Population)):
                Population[i].nds = True
        # sort according to the values of nds first and then if 2 entries are nds then use (f1+f2+f3) to break the tie
        Population.sort()		
        newGeneration = []
        newPopulation = []
        for i in range(newLimit):
            newPopulation.append(Population[i])
            newGeneration.append(Population[i])
        t_ = newPopulation[0]
        newn = copy.deepcopy(t_.n)
        
        for i in range(len(newn)):
            newn[i] = newn[i] / 100
        print("Generation - ",gen,"    X values - ",newn)
        yaxis.append (t_.fitness)
        # only fit individuals from the population are allowed to mate
        # two parents will give birth to one child
        for i in range (uplimit):
            parenta = newGeneration[np.random.randint(0,len(newGeneration))]
            parentb = newGeneration[np.random.randint(0,len(newGeneration))]
            child_ = Mate(parenta, parentb)
            newPopulation.append(child_)
        Population = copy.deepcopy(newPopulation)
    best = Population[0].n
    return best

PopSize = 100
CrossOverProb = 90
Maxgen = 500
Iterate(Maxgen)
plt.plot(range(Maxgen), yaxis)
plt.xlabel("epoch")
plt.ylabel("fitness")
plt.title("Basic GA N = %d"%(PopSize))
plt.show()