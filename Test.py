import copy

xLength = 12
yLength = 25
env = Environment(xLength,yLength)

env.setObstacle(2,3,3,4)
env.setObstacle(2,10,7,8)

startx = 0
starty = 0
endx = 10
endy = 10

env.calculateHeuristics(startx,starty,endx,endy,"pythagorean")

env.printEnvironment()

pathQ = env.LPA_Star(0,0,endx,endy)

#print("Path:",pathQ)

env.printVisualEnvironment(pathQ)
#memory = np.zeros(np.shape(env.accessArray))
memory = np.array(env.accessArray)
gMemory = np.array(env.gArray)
#print("M:", np.shape(memory))
print("G:",gMemory)

#env.setOpen(2,7,3,4)
env.setObstacle(8,10,3,8)


pathQ2 = env.LPA_Star(0,0,endx,endy)

env.printEnvironment()
env.printVisualEnvironment(pathQ2)
#print(pathQ2)
#print(memory)
