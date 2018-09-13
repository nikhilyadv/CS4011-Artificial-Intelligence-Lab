import numpy as np
import queue
import copy
import math
class navigation:
    def __init__(self):						#initailizing and taking inputs
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
      a , b , c = map(float , input().split())		# a = congestion , b = budget , c = rate
      if a == 0:
        self.busspeed = 10
      elif a == 1:
        self.busspeed = 37.5
      elif a == 2:
        self.busspeed = 50
      self.cyclespeed = 25
      self.budget = b
      self.rate = c
      self.asearch()
      print("Done")									#exit message
    def h(self,num):								#function to calculate hueristic eculdean distance
      a , b = self.checktuple[self.goal]
      c , d = self.checktuple[num]
      return math.sqrt((a-c)**2+(b-d)**2)
    def ht(self,num):								#function to calculate time hueristic
      a = self.h(num)
      return (a / self.cyclespeed , a / self.busspeed)
    def printpath(self,path,g,budget):						#utiltiy function to print the final path
      print("Path ",end="")
      for i in range(0,len(path)):
        u , v = self.checktuple[path[i][0]]
        print("(",int(u),",",int(v),")",end="")
        if i != len(path) - 1:
          print(" ->",end=(path[i+1][1]+" "))
      print("\nTotal time taken - ",g)
      print("Budget left - ",budget)
    def asearch(self):								#A* search algo
      Q = queue.PriorityQueue()
      g = 0
      budget = self.budget
      path = [(self.start,0)]
      u = self.start
      a , b = self.ht(u)
      Q.put((g + a , u , g , budget , copy.deepcopy(path)))
      Q.put((g + b , u , g , budget , copy.deepcopy(path)))
      while not Q.empty():
        f , u , g , budget , path = Q.get()
        if budget < 0 :							#avoiding negative budget condition
          continue
        if u == self.goal:
          self.printpath(path,g,budget)
          return True
        for i in range(0,len(self.adjlist[u])):
          v , w = self.adjlist[u][i]
          a , b = self.ht(v)					#hueristic
          #if bus
          if w > 3:								#taking bus only if path weight is > than 3
            path.append((v,'B'))
            Q.put(((g+(w/self.busspeed)+a),v,(g+(w/self.busspeed)),(budget - self.rate*w),copy.deepcopy(path)))
            path.pop()
          #if cycle
          path.append((v, 'C'))
          Q.put(((g + (w / self.cyclespeed) + b), v, (g + (w / self.cyclespeed)), budget , copy.deepcopy(path)))
          path.pop()
      return False
env = navigation()