import pygame
import Container

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Container Stacker")
clock = pygame.time.Clock()

numbers = Container.GetNumbers()

craneImg = pygame.image.load("crane.png")

containerImg1 = pygame.image.load("container1.png")
containerImg2 = pygame.image.load("container2.png")
containerImg3 = pygame.image.load("container3.png")
containerImg4 = pygame.image.load("container4.png")
containerImg5 = pygame.image.load("container5.png")

def crane(x,y):
    gameDisplay.blit(craneImg,(x,y))

def grid():
    rooster11 = (numbers[0][0])
    #rooster12 = numbers[0][1]
    #rooster13 = numbers[0][2]
    #rooster14 = numbers[0][3]
    #rooster15 = numbers[0][4]
    #rooster16 = numbers[0][5]

    #rooster2.1

    if rooster11 == 1:
        gameDisplay.blit(containerImg1,(0,540))
    if rooster11 == 2:
        gameDisplay.blit(containerImg2,(0,540))
    if rooster11 == 3:
        gameDisplay.blit(containerImg3,(0,540))
    if rooster11 == 4:
        gameDisplay.blit(containerImg4,(0,540))
    if rooster11 == 5:
        gameDisplay.blit(containerImg5,(0,540))

def game_loop():

    x = (0)
    y = (540)

    x_change = 0
    y_change = 0

    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

#            RIPRIPRIPRIP
#            if (event.type == pygame.KEYDOWN and event.mod == pygame.KMOD_ALT and event.key == pygame.K_F4):
#                   done = True

            ###MOVEMENT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -60
                elif event.key == pygame.K_RIGHT:
                    x_change = 60
                elif event.key == pygame.K_UP:
                    y_change = -60
                elif event.key == pygame.K_DOWN:
                    y_change = 60

            if x > 740:
                x = 740
            if x < 0:
                x = 0
            if y > 540:
                y = 540
            if y < 0:
                y = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        crane(x,y)

		#Hier draw je je grid.
		#Doe je het eerder, dan wordt het onzichtbaar aangezien alles overschreven wordt met wit. (line 100)
		#Doe je het buiten deze game loop dan wordt het niet getekend.
        grid()

        pygame.display.update()
        clock.tick(30)

game_loop()
pygame.quit()
quit()
