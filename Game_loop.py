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
craneGrabbedImg = pygame.image.load(resourcesFolder+"craneGrabbed.png")
refreshImg = pygame.image.load(resourcesFolder+"refresh.png")

def crane():
    if grabbedContainer is None:
        gameDisplay.blit(craneImg,(cranePosX,cranePosY))
    else:
        gameDisplay.blit(craneGrabbedImg,(cranePosX,cranePosY))

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
                if event.key == pygame.K_LEFT and cranePosX > 0:
                    if grabbedContainer is not None and checkContainerPresentTo(pygame.K_LEFT) is False:
                        grabbedContainer.posX += -60
                        cranePosX += -60
                    elif grabbedContainer is None:
                        cranePosX += -60

                elif event.key == pygame.K_RIGHT and cranePosX < 720:
                    if grabbedContainer is not None and checkContainerPresentTo(pygame.K_RIGHT) is False:
                        grabbedContainer.posX += 60
                        cranePosX += 60
                    elif grabbedContainer is None:
                        cranePosX += 60
                       
                elif event.key == pygame.K_UP and cranePosY > 0:
                    if grabbedContainer is not None and checkContainerPresentTo(pygame.K_UP) is False:
                        grabbedContainer.posY += -60
                        cranePosY += -60
                    elif grabbedContainer is None:
                        cranePosY += -60

                elif event.key == pygame.K_DOWN and cranePosY < 540:
                    if grabbedContainer is not None and checkContainerPresentTo(pygame.K_DOWN) is False:
                        grabbedContainer.posY += 60
                        cranePosY += 60
                    elif grabbedContainer is None:
                        cranePosY += 60

                '''container handling'''
                if event.key == pygame.K_SPACE:
                    craneHandler()
            
            mouse = pygame.mouse.get_pos()
            pass

        draw()

def checkContainerPresentTo(direction):
    if direction == pygame.K_LEFT:
        return checkContainerPresentAt(cranePosX - 60, cranePosY)
    elif direction == pygame.K_RIGHT:
        return checkContainerPresentAt(cranePosX + 60, cranePosY)
    elif direction == pygame.K_UP:
        return checkContainerPresentAt(cranePosX, cranePosY - 60)
    elif direction == pygame.K_DOWN:
        return checkContainerPresentAt(cranePosX, cranePosY + 60)

def checkContainerPresentAt(x, y):
    for block in containers:
        for container in block:
            if (container.posX == x and container.posY == y):
                return True
    return False

def craneHandler():
    global grabbedContainer
    if grabbedContainer is None:
        grabContainer()
    else:
        dropContainer()

def grabContainer():
    #TODO: if UP direction has a block, don't grab (use checkContainerTo(UP))
    for block in containers:
        for container in block:
            bork = False
            if (container.posX == cranePosX 
            and container.posY == cranePosY):
                if (container.posX == cranePosX 
                and container.posY == (cranePosY - 60)):
                    bork = True
                if bork == False:
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
