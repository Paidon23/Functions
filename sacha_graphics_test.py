__author__ = 'sacha'


import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1020, 720))

###pour mockup gui###
background = pygame.image.load('gui/background.png')
buttons = pygame.image.load('gui/buttons.png')
select1 = pygame.image.load('gui/select1.png')
select2 = pygame.image.load('gui/select2.png')
select3 = pygame.image.load('gui/select3.png')
####################

selected = 1
mouseX = -1
mouseY = -1

x = 0
ancien_coord = (0, 0)
function = input("Enter the function: ")
screen.fill((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

###pour mockup gui###
        # elif event.type == MOUSEBUTTONDOWN:
        #     mouseX, mouseY = pygame.mouse.get_pos()


        # if 20 <= mouseX <= 320 and 20 <= mouseY <= 80:
        #     selected = 1
        # elif 360 <= mouseX <= 660 and 20 <= mouseY <= 80:
        #     selected = 2
        # elif 700 <= mouseX <= 1000 and 20 <= mouseY <= 80:
        #     selected = 3
        # else:
        #     mouseX, mouseY = -1, -1

        # screen.blit(background, (0, 0))
        # if selected == 1:
        #     screen.blit(select1, (0, 0))
        # elif selected == 2:
        #     screen.blit(select2, (0, 0))
        # else:
        #     screen.blit(select3, (0, 0))
        # screen.blit(buttons, (0, 0))
###################

        if x <= 1020:
            y = eval(function)


        pygame.draw.line(screen, (0, 0, 0), (x, 720 - y), ancien_coord, 1)

        ancien_coord = (x, 720 - y)
        x += 1

        pygame.display.flip()
