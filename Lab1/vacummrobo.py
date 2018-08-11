class pair:
    '''Class to create pair , add them and then check for equality'''
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
    def add(self, a):
        return pair(self.x + a.x, self.y + a.y)
    def equals(self, a):
        return (self.x == a.x and self.y == a.y)
class Agent:
    '''Class of Robot'''
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    def __init__ (self):
        self.current = pair(0, 0)
        self.dir = 1
        self.moves = 0
        self.alive = True       #alive represents power on or off
    def move(self, percept):
        '''Take move after checking envirnoment and then next determining location'''
        if not self.alive:
            return
        self.dir = self.ddir()
        self.current.x += self.dr[self.dir]
        self.current.y += self.dc[self.dir]
        self.moves += 1
        if percept:
            self.alive = False 
    def ddir(self):
        '''Logic to determine direction'''
        k = self.moves
        a = int((1 + (1 + 4 * k) ** (0.5)) // 2)
        b = int(k ** (0.5))
        if(a * (a - 1) == k or b * b == k):
            self.dir = (self.dir + 1) % 4
        return self.dir
class Environment:
    def __init__ (self, dirt, agent): 
        self.agent = Agent()
        self.lagent = agent
        self.dirt = dirt
    def percept(self):
        loc = self.agent.current.add(self.lagent)
        return (loc.equals(self.dirt))          #bool
    def step(self):                             #one move
        self.agent.move(self.percept())
        self.print_info()                       #print info at each step
    def print_info(self):                       #print function
        loc = self.agent.current.add(self.lagent)
        print("(" + str(loc.x) + ", " + str(loc.y) + ")")
    def run(self):
        while 1:                    #Do some cleaning
            if not self.agent.alive:
                return
            self.step()
#start
dirt = pair(int(input("Enter Dirt location (x,y) - ")), int(input()))
agent = pair(int(input("Enter Robot location (x,y) - ")), int(input()))
envi = Environment(dirt, agent)
envi.run()