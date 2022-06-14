import pygame 

import sys

import os

import button

import slike

from pygame.locals import *

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
clock = pygame.time.Clock()
width, height = 1080 , 720
screen = pygame.display.set_mode((width,height))
run=True
bg = pygame.image.load("D:/Fucked up in da crib/game/ong.jpeg").convert_alpha()
bg = pygame.transform.scale(bg,(width,height))
pygame.mouse.set_visible(1)
icon = pygame.image.load('D:/Fucked up in da crib/game/albania_flag.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Kviz Tajm!!!!')

#varijable
game_paused = False
goofy_easter_egg = False
main = False
tut = 'tut'
augh = False
pitanje = 'pitanje0'
font = pygame.font.SysFont('bookantiqua', 56)
font2 = pygame.font.SysFont('bookantiqua', 42)
boja1 = (255, 174, 0)
br = 3
wrong = False

#text function
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
#main menu buttons
play_button = button.Button(100, 100, slike.play, 0.7)
options_button = button.Button(550, 300, slike.options, 0.65)
quit_button = button.Button(225, 450, slike.quit1, 0.4)
#options button
resume_button = button.Button(350, 50, slike.resume, 0.55)
goofy_button = button.Button(150, 200, slike.goofy, 0.25)
back_button = button.Button(925, 650, slike.back, 0.25)
tutorial_button = button.Button(250, 325, slike.tutorial, 0.5)
next_button = button.Button(925, 575, slike.next1, 0.25)
exit_button = button.Button(925, 500, slike.exit1, 0.25)
dont_button = button.Button(650, 500, slike.dont, 0.6)
menu_button = button.Button(925, 650, slike.menu, 0.25)
#pitanje puci
pitanje1_1_button = button.Button(100, 175, slike.pitanje1_1, 0.66)
pitanje1_2_button = button.Button(575, 175, slike.pitanje1_2, 0.66)
pitanje1_3_button = button.Button(100, 450, slike.pitanje1_3, 0.66)
pitanje1_4_button = button.Button(575, 450, slike.pitanje1_4, 0.66)

pitanje2_1_button = button.Button(100, 175, slike.pitanje2_1, 0.66)
pitanje2_2_button = button.Button(575, 175, slike.pitanje2_2, 0.66)
pitanje2_3_button = button.Button(100, 450, slike.pitanje2_3, 0.66)
pitanje2_4_button = button.Button(575, 450, slike.pitanje2_4, 0.66)

pitanje3_1_button = button.Button(100, 175, slike.pitanje3_1, 0.66)
pitanje3_2_button = button.Button(575, 175, slike.pitanje3_2, 0.66)
pitanje3_3_button = button.Button(100, 450, slike.pitanje3_3, 0.66)
pitanje3_4_button = button.Button(575, 450, slike.pitanje3_4, 0.66)

pitanje4_1_button = button.Button(100, 175, slike.pitanje4_1, 0.66)
pitanje4_2_button = button.Button(575, 175, slike.pitanje4_2, 0.66)
pitanje4_3_button = button.Button(100, 450, slike.pitanje4_3, 0.66)
pitanje4_4_button = button.Button(575, 450, slike.pitanje4_4, 0.66)

pitanje5_1_button = button.Button(100, 175, slike.pitanje5_1, 0.66)
pitanje5_2_button = button.Button(575, 175, slike.pitanje5_2, 0.66)
pitanje5_3_button = button.Button(100, 450, slike.pitanje5_3, 0.66)
pitanje5_4_button = button.Button(575, 450, slike.pitanje5_4, 0.66)

pitanje6_1_button = button.Button(100, 175, slike.pitanje6_1, 0.66)
pitanje6_2_button = button.Button(575, 175, slike.pitanje6_2, 0.66)
pitanje6_3_button = button.Button(100, 450, slike.pitanje6_3, 0.66)
pitanje6_4_button = button.Button(575, 450, slike.pitanje6_4, 0.66)

pitanje7_1_button = button.Button(100, 175, slike.pitanje7_1, 0.66)
pitanje7_2_button = button.Button(575, 175, slike.pitanje7_2, 0.66)
pitanje7_3_button = button.Button(100, 450, slike.pitanje7_3, 0.66)
pitanje7_4_button = button.Button(575, 450, slike.pitanje7_4, 0.66)

pitanje8_1_button = button.Button(100, 175, slike.pitanje8_1, 0.66)
pitanje8_2_button = button.Button(575, 175, slike.pitanje8_2, 0.66)
pitanje8_3_button = button.Button(100, 450, slike.pitanje8_3, 0.66)
pitanje8_4_button = button.Button(575, 450, slike.pitanje8_4, 0.66)

pitanje9_1_button = button.Button(100, 175, slike.pitanje9_1, 0.66)
pitanje9_2_button = button.Button(575, 175, slike.pitanje9_2, 0.66)
pitanje9_3_button = button.Button(100, 450, slike.pitanje9_3, 0.66)
pitanje9_4_button = button.Button(575, 450, slike.pitanje9_4, 0.66)

pitanje0_1_button = button.Button(100, 175, slike.pitanje0_1, 0.66)
pitanje0_2_button = button.Button(575, 175, slike.pitanje0_2, 0.66)
pitanje0_3_button = button.Button(100, 450, slike.pitanje0_3, 0.66)
pitanje0_4_button = button.Button(575, 450, slike.pitanje0_4, 0.66)

while run:
#goofy
    screen.blit(bg,(0,0))
    if goofy_easter_egg == True and tut == 'tut' and augh == False and pitanje == 'pitanje0':
        screen.blit(slike.slika1,(0,0))
        screen.blit(slike.slika2,(350,50))
        screen.blit(slike.slika3,(25,175))
        screen.blit(slike.slika4,(250,400))
        screen.blit(slike.slika5,(-20,300))
        screen.blit(slike.slika6,(375,213))
        screen.blit(slike.slika7,(650,300))
        screen.blit(slike.slika8,(500,450))
        screen.blit(slike.slika9,(640,20))
        screen.blit(slike.slika10,(-50,500))
        screen.blit(slike.slika11,(200,525))
        screen.blit(slike.slika12,(750,515))
        if back_button.draw(screen):
            main = False
            goofy_easter_egg = False

#paused

    if game_paused == True and goofy_easter_egg == False and main == False and tut == 'tut' and augh == False and pitanje == 'pitanje0':
        if resume_button.draw(screen):
            game_paused = False
        if goofy_button.draw(screen):
            goofy_easter_egg = True
            main = True
        if tutorial_button.draw(screen):
            tut = 'tut1'
        if dont_button.draw(screen):
            augh = True
#tutorial
    if tut == 'tut1':
        screen.blit(slike.tut1,(0,0))
        if back_button.draw(screen):
            tut = 'tut'
        if next_button.draw(screen):
            tut = 'tut2'
        if exit_button.draw(screen):
            tut='tut'
    if tut == 'tut2':
        screen.blit(slike.tut2,(0,0))
        if back_button.draw(screen):
            tut = 'tut1'
        if exit_button.draw(screen):
            tut='tut'
        if next_button.draw(screen):
            tut = 'tut3'
    if tut == 'tut3':
        screen.blit(slike.tut3,(0,0))
        if back_button.draw(screen):
            tut = 'tut2'
        if next_button.draw(screen):
            tut = 'tut4'
        if exit_button.draw(screen):
            tut='tut'
    if tut == 'tut4':
        screen.blit(slike.tut4,(0,0))
        if back_button.draw(screen):
            tut = 'tut3'
        if next_button.draw(screen):
            tut = 'tut5'
        if exit_button.draw(screen):
            tut='tut'
    if tut == 'tut5':
        screen.blit(slike.tut5,(0,0))
        if back_button.draw(screen):
            tut = 'tut4'
        if next_button.draw(screen):
            tut = 'tut6'
        if exit_button.draw(screen):
            tut='tut'
    if tut == 'tut6':
        screen.blit(slike.tut6,(0,0))
        if back_button.draw(screen):
            tut = 'tut5'
        if next_button.draw(screen):
            tut = 'tut'
#brao
    if augh == True and pitanje == 'pitanje0':
        screen.blit(slike.slika13,(0,0))
        draw_text('A sad rokni SPACE kad si već dirao!', font, (255, 255, 255), 75, 150)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
#main
    else:
        if main == False and game_paused == False and tut == 'tut' and augh == False and pitanje == 'pitanje0':
            if options_button.draw(screen):
                game_paused = True
            if play_button.draw(screen):
                pitanje = 'pitanje1'
            if quit_button.draw(screen):
                run = False

#pitanja
    if pitanje == 'pitanje1' and wrong == False:
        draw_text('Kako se zove dinosaur koji ima 500 zubiju?', font, boja1, 10, 25)
        if pitanje1_1_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje1_2_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje1_3_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje1_4_button.draw(screen):
            pitanje = 'pitanje2'
            
    if pitanje == 'pitanje2' and wrong == False:
        draw_text('Koja se valuta koristi u Poljskoj?', font, boja1, 10, 25)
        if pitanje2_1_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje2_2_button.draw(screen):
            pitanje = 'pitanje3'
        if pitanje2_3_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje2_4_button.draw(screen):
            br -= 1
            if br == 0:
                run = False

    if pitanje == 'pitanje3' and wrong == False:
        draw_text('Koji je glavni grad Finske?', font, boja1, 10, 25)
        if pitanje3_1_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje3_2_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje3_3_button.draw(screen):
            pitanje = 'pitanje4'
        if pitanje3_4_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
                
    if pitanje == 'pitanje4' and wrong == False:
        draw_text('Iz koje drćave potječe sir "Brie"?', font, boja1, 10, 25)
        if pitanje4_1_button.draw(screen):
            pitanje = 'pitanje5'
        if pitanje4_2_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje4_3_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje4_4_button.draw(screen):
            br -= 1
            if br == 0:
                run = False

    if pitanje == 'pitanje5' and wrong == False:
        draw_text('Koje je pravo prezime kraljice Elizabete II.?', font, boja1, 10, 25)
        if pitanje5_1_button.draw(screen):
            pitanje = 'pitanje6'
        if pitanje5_2_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje5_3_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje5_4_button.draw(screen):
            br -= 1
            if br == 0:
                run = False

    if pitanje == 'pitanje6' and wrong == False:
        draw_text('Koliko je vremenskih zona u Rusiji?', font, boja1, 10, 25)
        if pitanje6_1_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje6_2_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje6_3_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje6_4_button.draw(screen):
            pitanje = 'pitanje7'

    if pitanje == 'pitanje7' and wrong == False:
        draw_text('Koji je, površinski, najveći organ?', font, boja1, 10, 25)
        if pitanje7_1_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje7_2_button.draw(screen):
            pitanje = 'pitanje8'
        if pitanje7_3_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje7_4_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
    
    if pitanje == 'pitanje8' and wrong == False:
        draw_text('Koja je država SAD-a na istočnoj obali?', font, boja1, 10, 25)
        if pitanje8_1_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje8_2_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje8_3_button.draw(screen):
            pitanje = 'pitanje9'
        if pitanje8_4_button.draw(screen):
            br -= 1
            if br == 0:
                run = False

        
    if pitanje == 'pitanje9' and wrong == False:
        draw_text('Koje je ime zadnjeg egipatskog faraona?', font, boja1, 10, 25)
        if pitanje9_1_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje9_2_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje9_3_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje9_4_button.draw(screen):
            pitanje = 'pitanje10'
        
    if pitanje == 'pitanje10' and wrong == False:
        draw_text('Ko sloloa fight?', font, boja1, 10, 25)
        if pitanje0_1_button.draw(screen):
            pitanje = 'pitanje11'
        if pitanje0_2_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje0_3_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
        if pitanje0_4_button.draw(screen):
            br -= 1
            if br == 0:
                run = False
    if pitanje == 'pitanje11':
        screen.fill((212, 175, 55))
        text = 'Svaka cast zavrsio si quiz s ovoliko života:'
        draw_text(text, font2, (0, 255, 0), 100, 100)
        draw_text(str(br), font2, (0, 255, 0), 900, 100)
        screen.blit(slike.tu, (100, 200))
        screen.blit(slike.karlo, (600, 300))
        screen.blit(slike.ja, (50, 450))
        screen.blit(slike.man, (350, 450))
        screen.blit(slike.gej, (0, 0))
        screen.blit(slike.jes, (960, 0))
        if menu_button.draw(screen):
            pitanje='pitanje0'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
