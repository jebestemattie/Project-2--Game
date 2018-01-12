import pygame

start_ticks=pygame.time.get_ticks() #starter tick
while mainloop: # mainloop
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    if seconds>10: # if more than 10 seconds close the game
        break
    print (seconds) #print how many seconds








# import pygame
# from pygame.locals import KEYDOWN, K_ESCAPE, RLEACCEL
 
# class Make_Countdown(pygame.sprite.DirtySprite):
#     """
#    xpos and ypos are the coords where the text will be centeres and printed. By defaault they are screen_centerx and screen_centery. If you leave posx = None and posy = None these values will be used. If you enter any values, those will be used.
#    Font size need to be supplied along with the colour of text, lownum and hinum.
#    Countdown = True by default. hinum -> lownum
#    Countdown = False lownum -> hinum
#    if a font is not supplied (path), the default pygame font will be used.
#    Fading out is set by default.
#    Time will hold each number on screen for that duration If fade is set that time will be used to fade out."""
 
#     def __init__(self, posx = None, posy = None, colour = (255, 50, 64), number = 5, font = None, fontsize = 200, fade_speed = 20, countdown = True, fadeout = True):
 
#         pygame.sprite.DirtySprite.__init__(self)
 
#         self.screen = pygame.display.get_surface()
 
#         if self.screen == None:
#             print("none")
#             self.screen =pygame.display.set_mode((300, 300), 1, 32)
 
#         self.subsurface = self.screen.subsurface(0, 0, self.screen.get_width(), self.screen.get_height()).convert_alpha()
#         self.back = self.screen
#         self.background = (0, 0, 0)
#         self.alpha = 255
#         if posx == None:
#             self.posx = self.screen.get_width() / 2
#         else:
#             self.posx = posx
#         if posy == None:
#             self.posy = self.screen.get_height() / 2
#         else:
#             self.posy = posy
#         self.fontsize = fontsize
#         self.colour = colour
#         self.lownum = 1
#         self.hinum = number
#         self.font = font
#         self.count_down = countdown
#         self.fade = fadeout
#         self.fade_speed = fade_speed
#         self.imagelist = []
 
#         self.renderedfont = pygame.font.Font(self.font, self.fontsize)
 
#         for x in xrange(self.lownum, self.hinum + 1):  # we want to count hinum as well so + 1
 
#             matext = self.renderedfont.render(str(x), True, self.colour, (0, 0, 0)).convert()
 
#             matext.set_colorkey(0, RLEACCEL)
 
#             matext.set_alpha(255)
 
#             self.imagelist.append(matext)
 
 
 
#     def run(self, variable):
 
#         direction = variable
 
#         if direction == "down":
 
#             self.imagelist = reversed(self.imagelist)
 
#         for image in self.imagelist:
 
#             self.alpha = 255
#             # the calculation below makes the sprite be printed by its center coord
#             posx = self.posx - (image.get_width() / 2)
#             posy = self.posy - (image.get_height() / 2)
#             self.subsurface = self.screen.subsurface(posx, posy, image.get_width(), image.get_height()).convert_alpha()
#             for x in xrange(50):
 
#                 self.alpha -= 5
#                 image.set_alpha(self.alpha)
 
#                 self.screen.blit(image, (posx, posy))
 
#                 pygame.display.update()
#                 pygame.time.wait(self.fade_speed)  # how long to pause
#                 self.screen.blit(self.subsurface, (posx, posy))
 
#             for e in pygame.event.get():
#                 if e.type == KEYDOWN and e.key == K_ESCAPE:
#                     raise SystemExit
 
 
 
# if __name__ == '__main__':
#     pygame.init()
#     counter = Make_Countdown()
#     #counter.run("up")
#     counter.run("down")