import pygame
from ContainerGenerator import *

pygame.mixer.init()
pygame.init()

display_width = 800
display_height = 600

cranePosX = 0
cranePosY = 540

shipPosX = 0

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Container Stacker")
clock = pygame.time.Clock()

containers = None
grabbedContainer = None

resourcesFolder = "resources/"
craneImg = pygame.image.load(resourcesFolder+"crane.png")
craneGrabbedImg = pygame.image.load(resourcesFolder+"craneGrabbed.png")
refreshImg = pygame.image.load(resourcesFolder+"refresh.png")
backgroundImg = pygame.image.load(resourcesFolder+"background.png")
shipImg = pygame.image.load(resourcesFolder+"ship.png")
pierImg = pygame.image.load(resourcesFolder+"pier.png")
c_row1Img = pygame.image.load(resourcesFolder+"c_row1.png")
c_row2Img = pygame.image.load(resourcesFolder+"c_row2.png")
c_row3Img = pygame.image.load(resourcesFolder+"c_row3.png")
c_row4Img = pygame.image.load(resourcesFolder+"c_row4.png")
c_row5Img = pygame.image.load(resourcesFolder+"c_row5.png")
c_row6Img = pygame.image.load(resourcesFolder+"c_row6.png")

boom = pygame.mixer.Sound(resourcesFolder+"boom2.wav")
takeoff = pygame.mixer.Sound(resourcesFolder+"takeoff.wav")

delCount = 0
gameEnd = False

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

                elif event.key == pygame.K_RCTRL:
                    endGameLoop()

                '''container handling'''
                if event.key == pygame.K_SPACE:
                    craneHandler()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    if 790 > mouse[0] > 710 and 90 > mouse[1] > 10:
                        getContainers()

        if gameEnd == True:
            done = True
            endGameLoop()

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
    for block in containers:
        for container in block:
            if (container.posX == cranePosX 
            and container.posY == cranePosY):
                if checkContainerPresentTo(pygame.K_UP) is False:
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
                stackCheck()
                
                boom.play()

def stackCheck():
    for block in containers:
        for container in block:
            if ((cranePosX == container.posX) and (cranePosY == container.posY) and (container.number == 1)):
                del1 = container
                for block in containers:
                    for container in block:
                        if ((cranePosX == container.posX) and ((cranePosY + 60) == container.posY) and (container.number == 2)):
                            del2 = container
                            for block in containers:
                                for container in block:
                                    if ((cranePosX == container.posX) and ((cranePosY + 120) == container.posY) and (container.number == 3)):
                                        del3 = container
                                        for block in containers:
                                            for container in block:
                                                if ((cranePosX == container.posX) and ((cranePosY + 180) == container.posY) and (container.number == 4)):
                                                    del4 = container
                                                    for block in containers:
                                                        for container in block:
                                                            if ((cranePosX == container.posX) and ((cranePosY + 240) == container.posY) and (container.number == 5)):
                                                                del5 = container
                                                                del1.posX += -1000
                                                                del2.posX += -1000
                                                                del3.posX += -1000
                                                                del4.posX += -1000
                                                                del5.posX += -1000
                                                                global delCount
                                                                delCount += 1
                                                                if delCount == 1:
                                                                    #quick_maffs
                                                                    global gameEnd
                                                                    gameEnd = True
                                                                elif delCount == 2:
                                                                    pass#skidikipapa
                                                                elif delCount == 3:
                                                                    pass#moving_cornflakes
                                                                elif delCount == 4:
                                                                    pass#2plus2is4
                                                                elif delCount == 5:
                                                                    pass#papapkakaka
                                                                elif delCount == 6:
                                                                    pass
                                                                     

def getContainers():
    global containers
    global grabbedContainer
    containers = ContainerGenerator().Get()
    grabbedContainer = None

getContainers()

def endGameLoop():
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        global shipPosX
        takeoff.play()
        shipPosX += 1       
        if shipPosX >80:
            shipPosX += 5
        if shipPosX == 250:
            pass

        draw()


def draw():
    black = (0,0,0)
    gameDisplay.blit(backgroundImg, (0, 0))
    gameDisplay.blit(shipImg, (shipPosX, 0))
    gameDisplay.blit(pierImg, (0, 0))
    if delCount > 0:
        gameDisplay.blit(c_row1Img, (shipPosX,0))
        if delCount > 1:
            gameDisplay.blit(c_row2Img, (shipPosX,0))
            if delCount > 2:
                gameDisplay.blit(c_row3Img, (shipPosX,0))
                if delCount > 3:
                    gameDisplay.blit(c_row4Img, (shipPosX,0))
                    if delCount > 4:
                        gameDisplay.blit(c_row5Img, (shipPosX,0))
                        if delCount > 5:
                            gameDisplay.blit(c_row6Img, (shipPosX,0))

    gameDisplay.blit(refreshImg,(710,10))

    for block in containers:
        for container in block:
            img = pygame.image.load(resourcesFolder + container.image)
            gameDisplay.blit(img, (container.posX, container.posY))

    crane()

    pygame.display.update()
    clock.tick(30)

game_loop()
pygame.quit()
quit()
