import numpy as np
import queue
import copy
import math
class puzzle:                       #CLASS
    def __init__(self):
        self.n = int(input())           #size of matrice
        self.getboard()                 #getting board from the user
        self.goal = [[] for i in range(0,self.n)]       #defining goal
        self.getloc = {}
        for i in range(0,self.n):
            for j in range(0,self.n):
                self.goal[i].append(self.n*i+j+1)
                self.getloc[self.n*i+j+1] = (i,j)
        self.goal[self.n - 1][self.n - 1] = 0
        self.goal[self.n - 1][self.n - 2] = 0
        self.g = np.asarray(self.goal)                  #np array to check calculations easily
        #print (self.goal)
        self.astar()                                    #search algo

    def getboard(self):                                 #input function
        self.blank = []
        self.start = [i for i in range(0,self.n)]
        for i in range(0,self.n):
            self.start[i] = list(map (int, input().split()))
            for j in range(0,self.n):
                if self.start[i][j] == 0:
                    self.blank.append((i,j))
    def manhattan(self,p1,p2):                     #function to calculater manhattan distance
        x,y = self.getloc[self.a[p1][p2]]
        return abs(x-p1)+abs(y-p2)
    def h(self):                                        #function to calculate heusristic
        distance = 0
        flag = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if self.a[i][j] != 0 and self.a[i][j] != self.goal[i][j]:
                    distance = distance + self.manhattan(i,j)
        return distance
    def isgoal(self):                                      #whether the current node is goal or not
        b = np.asarray(self.a)
        return np.array_equal(b, self.g)
    def v(self):                                           #whether the current node is visited or not
        s = ''.join(str(y) for x in self.a for y in x)
        if not s in self.visited:
            return True
        return False
    def visit(self):                                       #mark the current node as visited
        s = ''.join(str(y) for x in self.a for y in x)
        self.visited[s] = 1
    def astar(self):                                        #Astart search algo
        self.visited = {}
        self.a = copy.deepcopy(self.start)
        q = queue.PriorityQueue()
        g = 0
        path = []
        q.put((g+self.h(),copy.deepcopy(self.a),copy.deepcopy(self.blank),g,copy.deepcopy(path)))
        while not q.empty():
            f, self.a, self.blank, g, path = q.get()
            if self.isgoal():               # checking whether the current state is goal or not
                print("Path length - ",g)
                print(path)     # printing the path
                return True
            g = g + 1                       #increamenting the cost
            self.visit()                    #visiting the current node
            #moving blank 1
            if self.up(0):
                if self.v():
                    p = copy.deepcopy(path)
                    p.append("Up-1")
                    q.put((g + self.h(), copy.deepcopy(self.a), copy.deepcopy(self.blank), g, p))
                self.down(0)
            if self.down(0):
                if self.v():
                    p = copy.deepcopy(path)
                    p.append("Down-1")
                    q.put((g + self.h(), copy.deepcopy(self.a), copy.deepcopy(self.blank), g, p))
                self.up(0)
            if self.left(0):
                if self.v():
                    p = copy.deepcopy(path)
                    p.append("Left-1")
                    q.put((g + self.h(), copy.deepcopy(self.a), copy.deepcopy(self.blank), g, p))
                self.right(0)
            if self.right(0):
                if self.v():
                    p = copy.deepcopy(path)
                    p.append("Right-1")
                    q.put((g + self.h(), copy.deepcopy(self.a), copy.deepcopy(self.blank), g, p))
                self.left(0)
            #moving blank 2
            if self.up(1):
                if self.v():
                    p = copy.deepcopy(path)
                    p.append("Up-2")
                    q.put((g + self.h(), copy.deepcopy(self.a), copy.deepcopy(self.blank), g, p))
                self.down(1)
            if self.down(1):
                if self.v():
                    p = copy.deepcopy(path)
                    p.append("Down-2")
                    q.put((g + self.h(), copy.deepcopy(self.a), copy.deepcopy(self.blank), g, p))
                self.up(1)
            if self.left(1):
                if self.v():
                    p = copy.deepcopy(path)
                    p.append("Left-2")
                    q.put((g + self.h(), copy.deepcopy(self.a), copy.deepcopy(self.blank), g, p))
                self.right(1)
            if self.right(1):
                if self.v():
                    p = copy.deepcopy(path)
                    p.append("Right-2")
                    q.put((g + self.h(), copy.deepcopy(self.a), copy.deepcopy(self.blank), g, p))
                self.left(1)
        return False                    #search finished but goal state not found
    def up(self,flag):                  #utiltiy functions
        x , y = self.blank[flag]
        if x > 0:
            self.a[x][y] = self.a[x-1][y]
            self.a[x-1][y] = 0
            self.blank[flag] = (x-1,y)
            return True
        return False
    def down(self,flag):
        x , y = self.blank[flag]
        if x < self.n - 1:
            self.a[x][y] = self.a[x+1][y]
            self.a[x+1][y] = 0
            self.blank[flag] = (x+1,y)
            return True
        return False
    def left(self,flag):
        x , y = self.blank[flag]
        if y > 0:
            self.a[x][y] = self.a[x][y-1]
            self.a[x][y-1] = 0
            self.blank[flag] = (x,y-1)
            return True
        return False
    def right(self,flag):
        x , y = self.blank[flag]
        if y < self.n - 1:
            self.a[x][y] = self.a[x][y+1]
            self.a[x][y+1] = 0
            self.blank[flag] = (x,y+1)
            return True
        return False
envi = puzzle()                 #puzzle object