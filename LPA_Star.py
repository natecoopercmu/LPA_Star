pathLPA_01 = env.LPA_Star(startx,starty,endx,endy)
memory_01[:] = env.gArray

#shut a door
env.setObstacle(50,52,10,35)

pathLPA_02 = env.LPA_Star(startx,starty,endx,endy)

#env.printVisualEnvironment()
g = env.gArray
m = memory_01
env.gChanges = env.gArray - memory_01
L = env.gChanges

LPA_reprocessed = 0
for i in range(len(env.gChanges)):
    for j in range(len(env.gChanges[0])):
        if env.gChanges[i][j] != 0: LPA_reprocessed+=1

print("Processed:",LPA_reprocessed)