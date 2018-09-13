import numpy as np
import queue
import copy
import math
class navigation:
    def __init__(self):                 #initailizing and taking inputs
      self.n = int(input())
      self.e = int(input())
      self.checktuple = {}
      self.checknum = {}
      count = 0
      for i in range(0,self.n):
        a , b = map(float , input().split())
        self.checknum[(a,b)] = count;
        self.checktuple[count] = (a,b)
        count = count + 1
      self.adjlist = [[] for i in range(0,self.n)]
      for i in range(0,self.e):
        fx , fy , tx , ty , w = map (float, input().split())
        u = self.checknum[(fx,fy)]
        v = self.checknum[(tx,ty)]
        self.adjlist[u].append((v,w))
        self.adjlist[v].append((u,w))
      a , b , c , d = map(float , input().split())
      self.start = self.checknum[(a,b)]
      self.goal = self.checknum[(c,d)]
      self.asearch()
      print("Done")                                   #exit message
    def h(self,num):                                  #function to calculate hueristic
      a , b = self.checktuple[self.goal]
      c , d = self.checktuple[num]
      return math.sqrt((a-c)**2+(b-d)**2)
    def printpath(self,path,g):                       #utility function to print the final path
      print("Path ",end="")
      for i in range(0,len(path)):
        u , v = self.checktuple[path[i]]
        print("(",int(u),",",int(v),")",end="")
        if i != len(path) - 1:
          print(" -> ",end="")
      print("\nTotal path cost - ",g)
    def asearch(self):                                #A* saerch algo
      visited = {}
      Q = queue.PriorityQueue()
      g = 0
      path = [self.start]
      u = self.start;
      Q.put((g + self.h(u) , u , g , path))
      while not Q.empty():
        f , u , g ,path = Q.get()
        visited[u] = 1
        if u == self.goal:
          self.printpath(path,g)
          return True
        for i in range(0,len(self.adjlist[u])):
          v , w = self.adjlist[u][i]
          if v not in visited:
            path.append(v)
            Q.put(((g + w + self.h(v)) , v , (g+w) , copy.deepcopy(path)))
            path.pop()
      return False
env = navigation()