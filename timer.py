import pygame
from random import randint

pygame.init()
pygame.font.init()

display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

def pause():
	puasExit = False
	while not puasExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				puasExit = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					puasExit = True
					return False

		print('PAUSE IS RUNNING') # check the output to see this being printed
		pygame.display.update()
		clock.tick(30)


def game_loop():

	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameExit = pause()

		print('GAME IS RUNNING') # check the output to see this being printed

		pygame.display.update()
		clock.tick(30)

game_loop()