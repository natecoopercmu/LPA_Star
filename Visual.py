import pygame, sys
from pygame.locals import *

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
            if (j,i) in path: paint(i,j,RED)
            elif env.gArray[i][j] == -1: paint(i,j,BLACK)
            elif env.gChanges[i][j] > 0: paint(i,j,BLUE)
            elif env.gChanges[i][j] < 0: paint(i,j,BLUE)
            else: paint(i,j,WHITE)


displayEnvironment(env,pathLPA_02)
#displayEnvironment(env,pathA_02)
print(env.gChanges)
paint(startx,starty,PURPLE)
paint(endy,endx,ORANGE)
        
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

