#Nate Cooper
import numpy as np
import heapq

#Environment class defines graph properties and allows for A* and LPA* searches

class Environment:
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.gArray = np.ones((h,w)) * np.double(99999) # gValues
        self.pathMemory = {} # will be used for LPA_Star
        self.gChanges = np.zeros((h,w))
        self.heuristic = "pythagorean"
    
    def setObstacle(self,x1,x2,y1,y2):
        for i in range(x1,x2):
            for j in range(y1,y2):
                self.setG(i,j, -1)           
    
    def setOpen(self,x1,x2,y1,y2):
        for i in range(x1,x2):
            for j in range(y1,y2):
                self.setG(i,j, 999)
    
    def printEnvironment(self):
        np.set_printoptions(precision=0,floatmode='fixed')
        for i in range((self.height)):
            print(self.gArray[i])
            print("\n")
    
    def printVisualEnvironment(self,pathQ=[]):
        visualMatrix = [x for x in range(self.width)]
        
        for i in range(self.height):
            for j in range(self.width):
                if (self.getG(j,i) < 0):
                    visualMatrix[j] = "XX"
                elif ((j,i) in pathQ):
                    visualMatrix[j] = round(self.getG(j,i))
                else:
                    visualMatrix[j] = "  "
            print(visualMatrix)
                
    def getH(self,x,y):
        if (self.getG(x,y) < 0): return -1
        elif (self.heuristic == "taxicab"): # Manhattan distance between points
            return np.abs(y-endy)+np.abs(x-endx)
        elif (self.heuristic == "pythagorean"): # direct distance between points
            return (np.abs(y-endy)**2+np.abs(x-endx)**2)**0.5
        elif (self.heuristic == "dijkstra"): # dijkstra doesn't use heuristic values; baseline
            return 0
        elif (self.heuristic == "inverse"): # terrible heuristic
            return 1 / ((np.abs(y-endy)+np.abs(x-endx)) + 1)
        return -2
    
    def getG(self,x,y):
        return self.gArray[y][x]
    
    def setG(self,x,y,g_value):
        self.gArray[y][x] = g_value
    
    def updateG(self,x,y):
        if (self.getG(x,y) <= 0): return # start node always 0
        n = self.getNeighbors(x, y)
        if (len(n) == 0): return 
        g_value = 999
        for i in range(len(n)):
            if (self.getG(n[i][0],n[i][1]) < g_value and self.getG(n[i][0], n[i][1]) >= 0):
                g_value = self.getG(n[i][0],n[i][1])
            
        self.setG(x,y,g_value+1)
    
    def getNeighbors(self,x,y):
        n = []
        if (x > 0): n.append((x-1,y))
        if (x < self.width - 1): n.append((x+1,y))
        if (y > 0): n.append((x,y-1))
        if (y < self.height - 1): n.append((x,y+1))
        return n # (x,y)
    
    def A_Star(self,startx,starty,endx,endy):
        self.setG(startx,starty,0)
        q = priorityQueue()
        self.pathDictionary = {}
        
        q.insert(startx,starty,self)
        currentPoint = (-1,-1)
        
        while(len(q.queue) > 0 and currentPoint[1] != (endx,endy)):
            
            currentPoint = q.pop()
            
            if (self.getG(currentPoint[1][0],currentPoint[1][1]) >= 0):
                
                n = self.getNeighbors(currentPoint[1][0],currentPoint[1][1])
                
                for i in range(len(n)):
                    q.insert(n[i][0],n[i][1],self)
                 
                    if (n[i] not in self.pathDictionary.keys()): self.pathDictionary[(n[i][0],n[i][1])] = currentPoint[1]
                    
        #print((endx,endy))
        for node in self.pathDictionary:
            
            #print("node",node, pathDictionary[node])
            self.updateG(node[0], node[1])
        #print("begin backtrack")
        pathFindingPoint = (endx,endy)
        pathQ = []
        
        while(pathFindingPoint!=(startx,starty)):
            
            n = self.getNeighbors(pathFindingPoint[0], pathFindingPoint[1])
                        
            pathFindingPoint = self.pathDictionary[pathFindingPoint]
            
            pathQ.append(pathFindingPoint)
        
        return pathQ
    
    
    def LPA_Star(self,startx,starty,endx,endy,Memory = []):
        
        if (len(Memory) == 0):
            return self.A_Star(startx,starty,endx,endy)
        
        ChangedArray = np.zeros((self.height,self.width))
        updateQueue = []
        
        for i in range(len(ChangedArray)):
            for j in range(len(ChangedArray[0])):
                
                if (self.getG(j,i) < Memory[i][j]):
                    updateQueue.append((j, i))
                    n = self.getNeighbors(j, i) #(x,y)
                    for node in n:
                        updateQueue.append((node[0],node[1]))
                if (self.getG(j,i) > Memory[i][j]):
                    updateQueue.append((j, i))
                    n = self.getNeighbors(j, i) #(x,y)
                    for node in n:
                        updateQueue.append((node[0],node[1]))
        
        self.gChanges = Memory - self.gArray
        
        return self.A_Star(startx,starty,endx,endy)
        
class priorityQueue:
    def __init__(self):
        self.visited = set()
        self.queue = []
    def isVisited(self,x,y):
        return (x,y) in self.visited
    
    def insert(self,x,y,env):
        # make sure your are not adding a duplicate point or a point that has been visited
        if ((x,y) in self.visited or (env.getH(x,y),(x,y)) in self.queue or env.getG(x,y) < 0): return
        
        else: 
            heapq.heappush(self.queue,(env.getH(x,y),(x,y)))
            
    def pop(self):
        x = heapq.heappop(self.queue)
        self.visited.add(x[1])
        return x
        
