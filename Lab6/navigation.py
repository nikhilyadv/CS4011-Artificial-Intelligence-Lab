import numpy as np
import queue
import operator
import math
class navigation:
    def __init__(self):				#initalizing and taking inputs from user
        self.n = int(input("Enter the size of the square grid"))
        #creating a grid using probability of obtacles as 1/6
        self.grid = np.array(np.random.randint(0, 6, (self.n, self.n)) == np.zeros((self.n,self.n)), dtype = np.int32)	#self.getarray()
        print(self.grid)			#printing the generated grid
        self.start = tuple(map(int,input("Enter the starting coordinates : ").split()))
        self.end = tuple(map(int,input("Enter the final coordinates : ").split()))
        self.dir = int(input("Enter the number of direction 4/8 : "))
        self.type = int(input("Enter 0 for manhattan distance and 1 for euclidean distance : "))
        if not self.astar():				#check if path exists
            print ("Sorry path does not exits!!!")
    def getarray(self):
        a = [i for i in range (0, self.n)]  
        for i in range(0,self.n):
            a[i] = list(map (int, input().split()))
        return np.asarray(a)
    def h(self,curr):		#calculating cost to go
        if self.type == 0:
            return int(abs(curr[0]-self.end[0]) + abs(curr[1]-self.end[1]))
        return int(math.sqrt((curr[0]-self.end[0])**2 + (curr[1]-self.end[1])**2))
    def possible(self,i,j):	#checking if the move is legit or not
        if i >= 0 and i <= self.n - 1 and j >= 0 and j <= self.n - 1 and self.grid[i][j] == 0:
            return True
        return False
    def trace(self,parent):	#printing the path if it is found
        path = []
        curr = self.end
        while curr != (-1,-1):
            path.append(curr)
            curr = parent[curr[0]][curr[1]]
        print ("Length of path = ",len(path))
        for i in reversed(path):
            if (i != self.end):
                print (i,end='->')
                continue
            print (i)
    def astar(self):		#A* algorithm
        dx = [-1,0,1,0,1,-1,1,-1]
        dy = [0,-1,0,1,1,1,-1,-1]
        dist = [[self.n*self.n for i in range(0,self.n)] for j in range(0,self.n)]
        dist[self.start[0]][self.start[1]] = 0
        parent = [[(-1,-1) for i in range(0,self.n)] for j in range(0,self.n)]
        q = queue.PriorityQueue()
        g = 0
        q.put((g+self.h(self.start) , g , self.start))
        while not q.empty():
            f , g , curr = q.get()		#f = g + h
            if (curr == self.end):		#success
                self.trace(parent)
                return True
            g = g + 1					#next move cost
            for i in range(0,self.dir):
                t = tuple(map(operator.add, curr, (dx[i], dy[i])))
                if self.possible(t[0],t[1]) and g < dist[t[0]][t[1]]:
                    parent[t[0]][t[1]] = curr
                    q.put((g+self.h(t),g,t))
                    dist[t[0]][t[1]] = g
        return False					#path does not exists
env = navigation()