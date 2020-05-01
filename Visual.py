import pygame, sys
from pygame.locals import *

#PyGame modules required to run Visual.py
#https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation

#After running A_Star.py or LPA_Star.py, running Visual.py will create a figure for the path and environment

windowWidth = 500
windowHeight = 500
dx = int(windowWidth/xLength)
dy = int(windowHeight/yLength)
print(dx,dy)

pygame.init()
windowSurface = pygame.display.set_mode((windowWidth,windowHeight), 0, 32)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
ORANGE = (255, 150, 0)

pixelArray = pygame.PixelArray(windowSurface)
pixelArray[0:windowWidth][0:windowHeight] = WHITE

def paint(i,j,color):
    for k in range(dx):
        pixelArray[j*dx + k][i*dy:i*dy + dy] = color

def displayEnvironment(env,path=[]):
    for i in range(len(env.gArray)):
        for j in range(len(env.gArray[0])):
            if (j,i) in path: paint(i,j,RED) # paths are shown in red
            elif env.gArray[i][j] == -1: paint(i,j,BLACK)
            elif env.gChanges[i][j] > 0: paint(i,j,BLUE) # nodes that have been updated are shown in blue
            elif env.gChanges[i][j] < 0: paint(i,j,BLUE)
            else: paint(i,j,WHITE)


displayEnvironment(env,pathLPA_02) #uncomment me to show the LPA* path and processes
#displayEnvironment(env,pathA_02) #uncomment me to show the A* path and process
print(env.gChanges)
paint(startx,starty,PURPLE)
paint(endy,endx,ORANGE)
        
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

