import pygame
from ContainerGenerator import *

pygame.init()

display_width = 800
display_height = 600

cranePosX = 0
cranePosY = 540

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Container Stacker")
clock = pygame.time.Clock()

containers = ContainerGenerator().Get()

grabbedContainer = None

resourcesFolder = "resources/"

craneImg = pygame.image.load(resourcesFolder+"crane.png")
refreshImg = pygame.image.load(resourcesFolder+"refresh.png")

def crane():
    gameDisplay.blit(craneImg,(cranePosX,cranePosY))

def game_loop():

    done = False

    while not done:
        '''events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            global cranePosX
            global cranePosY
            if event.type == pygame.KEYDOWN:
                '''movement'''
                if event.key == pygame.K_LEFT:
                    if cranePosX > 0:
                        cranePosX += -60
                        if grabbedContainer is not None:
                            grabbedContainer.posX += -60

                elif event.key == pygame.K_RIGHT:
                    if cranePosX < 720:
                        cranePosX += 60
                        if grabbedContainer is not None:
                            grabbedContainer.posX += 60
                       
                elif event.key == pygame.K_UP:
                    if cranePosY > 0:
                        cranePosY += -60
                        if grabbedContainer is not None:
                            grabbedContainer.posY += -60

                elif event.key == pygame.K_DOWN:
                    if cranePosY < 540:
                        cranePosY += 60
                        if grabbedContainer is not None:
                            grabbedContainer.posY += 60

                '''container handling'''
                if event.key == pygame.K_SPACE:
                    craneHandler()
            
            mouse = pygame.mouse.get_pos()
            pass

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
            dog = False
            if (container.posX == cranePosX 
            and container.posY == cranePosY):
                if (container.posX == cranePosX 
                and container.posY == (cranePosY - 60)):
                    dog = True
                if dog == False:
                    global grabbedContainer
                    grabbedContainer = container

def dropContainer():
    for block in containers:
        for container in block:
            global grabbedContainer
            if (
                (container.posX == cranePosX 
                and container.posY == (cranePosY + 60) 
                and container.number == (grabbedContainer.number + 1))
                or cranePosY == 540):
                grabbedContainer = None

def draw():
    white = (255,255,255)
    gameDisplay.fill(white)

    gameDisplay.blit(refreshImg,(710,10))

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
