#Imports essentials and initiates pygame
import pygame
import time
from pygame.locals import *
from random import randrange
pygame.init()

#Names our game!
pygame.display.set_caption("Catch Game")

#Moves moving square to initial position, top left corner
x = 0
y = 0

#Color references for future use #(RED,GREEN,BLUE)
blue = (0,0,255)
white = (255,255,255)
pink = (255,200,200)

#Sets game screen size in pixels
Width = 200
Height = 200

#Creates screen and background for screen updates
screen = pygame.display.set_mode((Width,Height))
back = pygame.Surface((Width,Height))
background = back.convert()
background.fill(white)
screen.blit(background,(0,0))

#Moves objective to a random initial position
irandW = randrange(0, Width/50)*50
irandH = randrange(0, Height/50)*50

#Main loop for game
while True:
	for event in pygame.event.get():
		#Checks keydown events
		if event.type == KEYDOWN:
			if event.key == K_q:
				exit()
			if event.key == K_LEFT and x > 0:
				x = x - 50
			if event.key == K_RIGHT and x < (Width-50):
				x = x + 50
			if event.key == K_UP and y > 0:
				y = y - 50
			if event.key == K_DOWN and y < (Height-50):
				y = y + 50
	#Updates display for the UI
	pygame.display.update()
	
	#After update, screen is created once again for next update
	screen.blit(background,(0,0))
	pygame.draw.rect(screen, pink, (irandW+12.5,irandH+12.5,25,25), 0)
	pygame.draw.rect(screen, blue, (x,y,50,50), 0)

	#Updates objective sprite
	if x == irandW and y == irandH:
		irandW = randrange(0, Width/50)*50
		irandH = randrange(0, Height/50)*50