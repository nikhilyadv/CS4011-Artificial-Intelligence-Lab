import numpy as np
import copy
import math
import random
import matplotlib.pyplot as plt

GENE = "01"
yaxis = []
xaxis = []

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

def Iterate ():
    Population = []
    for i in range(0, PopSize):
        Population.append(Gene())
    newLimit = int(0.5 * PopSize);  
    uplimit = PopSize - newLimit
    global yaxis
    yaxis = []
    global xaxis
    xaxis = []
    for gen in range(0, 500):
        xaxis.append(gen + 1)
        for i in range(len(Population)):
            if(isNDS(i, Population)):
                Population[i].nds = True
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
        for i in range (uplimit):
            parenta = newGeneration[np.random.randint(0, len (newGeneration))]
            parentb = newGeneration[np.random.randint(0, len (newGeneration))]
            child_ = Mate(parenta, parentb)
            newPopulation.append(child_)
        Population = copy.deepcopy(newPopulation)
    best = Population[0].n
    return best

PopSize = 100
CrossOverProb = 90
Iterate()
plt.plot(xaxis, yaxis)
plt.xlabel("epoch")
plt.ylabel("fitness")
plt.title("Basic GA N = %d"%(PopSize))
# plt.savefig('Basic'+'.png')
plt.show()