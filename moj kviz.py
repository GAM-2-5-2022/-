import pygame

import sys

import os

from pygame.locals import *


pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
clock = pygame.time.Clock()
width,height = 1000,500
screen = pygame.display.set_mode((width,height))
running=True
bg = pygame.image.load("D:/Fucked up in da crib/game/ong.jfif")
bg = pygame.transform.scale(bg,(width,height))
pygame.mouse.set_visible(1)
icon = pygame.image.load('albania_flag.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Kviz Tajm!!!!')

#pitanje ig....

font = pygame.font.SysFont('bookantiqua', 56)
text = font.render('Kako se zove tip na slici iza mene?', True, (255, 174, 0))
textRect = text.get_rect()
textRect.center = (1000 // 2, 66)


while running:
    screen.blit(bg,(0,0))
    screen.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
