import numpy as np
import pickle
import queue

class Environment:
    def __init__(self):             #read all files and create result arrays
        self.road = np.array(pickle.load(open("road",'rb'),encoding='latin1'))
        self.vehicle = np.array(pickle.load(open("vehicle", 'rb'),encoding='latin1'))
        self.time = np.array(pickle.load(open("time", 'rb'),encoding='latin1'))
        self.num = self.time.size
        self.times = np.zeros((100, 5))
        self.countvehicles = np.zeros(shape=(int(np.sqrt(self.road.size)), int(np.sqrt(self.road.size))),
                                      dtype=np.int32)

    def calspeed(self, x):                  #speed function
        return np.exp(0.5 * x) / (1 + np.exp(0.5 * x)) + 15 / (1 + np.exp(0.5 * x))

    def run(self):
        q = queue.PriorityQueue()           #min priority queue where weight is time
        index = 0
        while index != self.num:
            q.put((self.time[index], index, 0))         #insert all the cars in the min priority queue
            index += 1
        while not q.empty():                    #while their are still cars left on the roads
            temp = q.get()
            index = temp[1]
            if temp[2] != 0:
                u = self.vehicle[temp[1]][temp[2] - 1]      #previous node
            v = self.vehicle[temp[1]][temp[2]]              #current node
            self.times[index][temp[2]] = temp[0]
            if self.vehicle[index].size - 1 == temp[2]:
                continue
            w = self.vehicle[temp[1]][temp[2] + 1]          #next node
            if temp[2] != 0:
                self.countvehicles[u][v] -= 1
            speed = self.calspeed(self.countvehicles[v][w])    #get speed
            t = temp[0] + (self.road[v][w] / speed) * 60       #calculate time taken to reach next node
            self.countvehicles[v][w] += 1
            q.put((t, index, temp[2] + 1))                      #reinsert into the min priority queue

    def out(self):          #save the array to file
        np.savetxt("output.csv", self.times, delimiter=",")
#start
envi = Environment()
envi.run()
envi.out()