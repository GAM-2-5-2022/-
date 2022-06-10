import pygame

import sys

import os

import button

from pygame.locals import *


pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
clock = pygame.time.Clock()
width,height = 1080 , 720
screen = pygame.display.set_mode((width,height))
run=True
bg = pygame.image.load("D:/Fucked up in da crib/game/ong.jfif").convert_alpha()
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

#buttons
pitanje1 = pygame.image.load('play2.png').convert_alpha()

#button class or sth

start_button = button.Button(100, 250, pitanje1, 0.5)
while run:
    screen.blit(bg,(0,0))
    screen.blit(text, textRect)
    if start_button.draw(screen):
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
