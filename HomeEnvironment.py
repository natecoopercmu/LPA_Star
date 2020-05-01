xLength = 120
yLength = 70

env = Environment(xLength,yLength)

#outer walls
env.setObstacle(0,120,0,70)
env.setOpen(2,118,2,68)

#Room walls
env.setObstacle(50,90,10,25)
env.setObstacle(50,90,45,50)
env.setObstacle(50,90,0,70)
env.setObstacle(0,51,40,45)
env.setOpen(65,90,45,68)
env.setOpen(65,90,2,20)
env.setOpen(2,118,20,30)
env.setOpen(2,118,55,60)
env.setOpen(10,30,40,45)

#hallway and front door
env.setOpen(52,58,2,70)

#tables
env.setObstacle(13,23,50,60)
env.setObstacle(10,30,10,30)
env.setObstacle(85,105,10,20)   


startx = 5
starty = 5
endx = 115
endy = 65

