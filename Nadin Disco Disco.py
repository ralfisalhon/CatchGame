import pygame
import time
from pygame.locals import *
from random import randrange
pygame.init()

pygame.display.set_caption("Disco Disco")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

colors = [(0,0,255), (255,255,255), (255,200,200)]

Width = 200
Height = 200

#Creates screen and background for screen updates
screen = pygame.display.set_mode((Width,Height))
back = pygame.Surface((Width,Height))
background = back.convert()
background.fill(white)
screen.blit(background,(0,0))

while True:
	for event in pygame.event.get():
		#Checks keydown events
		if event.type == KEYDOWN:
			if event.key == K_q:
				exit()

	x = 0
	y = 0

	for z in range(4):
		for i in range(4):
			pygame.draw.rect(screen, colors[randrange(0,3)], (x,y,50,50), 0)
			x += 50
		x = 0
		y += 50

	pygame.display.update()
