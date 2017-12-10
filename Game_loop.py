import pygame
from ContainerGenerator import *

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

cranePosX = 0
cranePosY = 540

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Container Stacker")
clock = pygame.time.Clock()

containers = ContainerGenerator().Get()

grabbedContainer = None

resourcesFolder = "resources/"

craneImg = pygame.image.load(resourcesFolder+"crane.png")

def crane():
    gameDisplay.blit(craneImg,(cranePosX,cranePosY))

def game_loop():

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

#            RIPRIPRIPRIP
#            if (event.type == pygame.KEYDOWN and event.mod == pygame.KMOD_ALT and event.key == pygame.K_F4):
#                   done = True

            ###MOVEMENT
            global cranePosX
            global cranePosY
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cranePosX += -60
                    if grabbedContainer is not None:
                        grabbedContainer.posX += -60

                elif event.key == pygame.K_RIGHT:
                    cranePosX += 60
                    if grabbedContainer is not None:
                        grabbedContainer.posX += 60
                        
                elif event.key == pygame.K_UP:
                    cranePosY += -60
                    if grabbedContainer is not None:
                        grabbedContainer.posY += -60

                elif event.key == pygame.K_DOWN:
                    cranePosY += 60
                    if grabbedContainer is not None:
                        grabbedContainer.posY += 60
                        
                elif event.key == pygame.K_SPACE:
                    craneHandler()

            #als grabbedContainer bestaat, move hem mee met de crane
            if cranePosX > 720:
                cranePosX = 720
            if cranePosX < 0:
                cranePosX = 0

            if cranePosY > 540:
                cranePosY = 540
            if cranePosY < 0:
                cranePosY = 0

        draw()

def craneHandler():
    global grabbedContainer
    if grabbedContainer is None:
        grabContainer()
    else:
        dropContainer()

def grabContainer():
    for block in containers:
        for container in block:
            if container.posX == cranePosX and container.posY == cranePosY:
                global grabbedContainer
                grabbedContainer = container

def dropContainer():
    pass
    #code om grabbedContainer 'los te laten'
    

def draw():
    gameDisplay.fill(white)

    for block in containers:
        for container in block:
            img = pygame.image.load(resourcesFolder + container.image)
            gameDisplay.blit(img, (container.posX, container.posY))

    crane()

    pygame.display.update()
    clock.tick(60)

game_loop()
pygame.quit()
quit()
