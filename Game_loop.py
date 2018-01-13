import pygame
from ContainerGenerator import *

pygame.mixer.init()
pygame.init()

display_width = 800
display_height = 600

cranePosX = 0
cranePosY = 540

shipPosX = 0

containers = None
grabbedContainer = None

sec = None

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Container Stacker")
clock = pygame.time.Clock()

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
gameovermenuImg = pygame.image.load(resourcesFolder+"gameovermenu.png")

# boom = pygame.mixer.Sound(resourcesFolder+"boom2.wav")
quick_maffs = pygame.mixer.Sound(resourcesFolder+"quick_maffs2.wav")
takeoff = pygame.mixer.Sound(resourcesFolder+"takeoff.wav")
dun_now = pygame.mixer.Sound(resourcesFolder+"dun_now2.wav")

delCount = 0
gameEnd = 0

def crane():
    if grabbedContainer is None:
        gameDisplay.blit(craneImg,(cranePosX,cranePosY))
    else:
        gameDisplay.blit(craneGrabbedImg,(cranePosX,cranePosY))

def game_loop():

    global gameEnd
    gameEnd = 0

    global delCount
    global cranePosX
    global cranePosY
    global shipPosX
    global grabbedContainer
    delCount = 0
    cranePosX = 0
    cranePosY = 540
    shipPosX = 0
    grabbedContainer = None

    getContainers()

    start_ticks=pygame.time.get_ticks()

    done = False

    while not done:
        '''events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                gameEnd = 3

            if event.type == pygame.KEYDOWN:
                '''movement'''
                if event.key == pygame.K_LEFT and cranePosX > 0:
                    if grabbedContainer is not None and checkContainerPresentTo(pygame.K_LEFT) is False:
                        grabbedContainer.posX += -60
                        cranePosX += -60
                    elif grabbedContainer is None:
                        cranePosX += -60

                elif event.key == pygame.K_RIGHT and cranePosX < 300:
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
                    gameEnd = 1

                '''container handling'''
                if event.key == pygame.K_SPACE:
                    craneHandler()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    if 790 > mouse[0] > 710 and 90 > mouse[1] > 10:
                        getContainers()

                        cranePosX = 0
                        cranePosY = 540

                        shipPosX = 0

                        containers = None
                        grabbedContainer = None
                        delCount = 0

        
        global sec
        sec = (pygame.time.get_ticks()-start_ticks)/1000

        draw()

        if gameEnd == 1:
            done = True
            


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
                
                #boom.play()

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
                                                                quick_maffs.play()
                                                                if delCount == 6:
                                                                    global gameEnd
                                                                    gameEnd = 1
                                                                                                                                    

def getContainers():
    global containers
    global grabbedContainer
    containers = ContainerGenerator().Get()
    grabbedContainer = None

getContainers()

def endGameLoop():
    done = False
    takeoff.play()
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                global gameEnd
                gameEnd = 3
        
        global shipPosX
        if shipPosX < 65:
            shipPosX += 1       
        if shipPosX >= 65:
            shipPosX += 5
        if shipPosX == 500: 
            dun_now.play()
        if shipPosX > 700:
            gameEnd = 2
            done = True

        draw()

def game_over():
    global gameEnd
    if gameEnd == 2:
        done = False
        while not done:
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    gameEnd = 3

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    if click[0] == 1:
                        if 356 > mouse[0] > 186 and 377 > mouse[1] > 325:
                            done = True
                        if 613 > mouse[0] > 443 and 377 > mouse[1] > 325:
                            gameEnd = 3
                            done = True
                            
    draw()


def draw():
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

    sys_font = pygame.font.SysFont \
                ("None", 60)
    rendered = sys_font.render \
        (str(sec), 0, (0, 0, 0))
    gameDisplay.blit(rendered, (600, 550))

    for block in containers:
        for container in block:
            img = pygame.image.load(resourcesFolder + container.image)
            gameDisplay.blit(img, (container.posX, container.posY))

    crane()                            

    global gameEnd      
    if gameEnd == 2:
        gameDisplay.blit(gameovermenuImg, (0, 0))
        scorerendered = sys_font.render \
                    ((("Your score: ")+(str(sec))), 0, (0 ,0, 0))
        gameDisplay.blit(scorerendered, (220, 270))

    pygame.display.update()
    clock.tick(30)

while gameEnd is not 3:
    game_loop()
    if gameEnd is not 3:
        endGameLoop()
    if gameEnd is not 3:
        game_over()


pygame.quit()
quit()
