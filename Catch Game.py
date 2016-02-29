#Imports essentials and initiates pygame
import pygame
import time
from pygame.locals import *
from random import randint, randrange, uniform
from timeit import default_timer
pygame.init()

#Names our game!
pygame.display.set_caption("Catch Game")

#Moves moving square to initial position, top left corner
x = 0
y = 0

#Color references for future use
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
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

#Sets initial Points to 0
Point = 0

#Text created for moving sprite
font = pygame.font.Font(None, 46)
text = font.render(str(Point), 1, black)
textpos = text.get_rect()
textpos.centerx = x
textpos.centery = y
screen.blit(text, textpos)

#Main loop for game
while True:
	for event in pygame.event.get():
		#Quits game if red button is pressed
		if event.type == pygame.QUIT:
			exit()
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
	
	#Font is updated on top of the mover sprite
	text = font.render(str(Point), 1, black)
	textpos.centerx = x+15
	textpos.centery = y+25
	screen.blit(text, textpos)

	#Checks for gaining Points, updates text and objective sprite
	if x == irandW and y == irandH:
		while (irandW == x and irandH == y):
			irandW = randrange(0, Width/50)*50
			irandH = randrange(0, Height/50)*50
		#Increases point variable by 1
		Point += 1