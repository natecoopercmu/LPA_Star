pathA_01 = env.A_Star(startx,starty,endx,endy)

#shut a door
env.setObstacle(50,52,10,35)

pathA_02 = env.A_Star(startx,starty,endx,endy)

A_reprocessed = 0
for i in env.pathDictionary:
    env.gChanges[i[1]][i[0]] = 1
    if env.gChanges[i[1]][i[0]] != 0: A_reprocessed+=1
    
print("Processed:", A_reprocessed)
