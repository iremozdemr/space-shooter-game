#display surface:
#the canvas that everything will be drawn on
#you can only have one at a time

#event loop
#check events
#this also include x to close the game

#pygame grafikleri iki şekilde ekranda gösterebilir
#1-image veya text ile
#2-pixeller ile

#display surface:
#ana ekran

#surface
#ana ekranın üzerine koyulan ekran

#print(pygame.ver)

#pygame.init() tam tersi pygame.quit()

#pygame.display.update()
#tüm ekranı günceller
#pygame.display.flip()
#ekranın bir kısmını günceller

#pygame'de image kullanırken
#image'da hiç transparent pixel yoksa convert kullan
#image'da transparent pixel vars convert_alpha kullan

import pygame 
import random

pygame.init()

pygame.display.set_caption("space shooter")
running = True

display_surface = pygame.display.set_mode((1280,720))
player_surface = pygame.image.load("images/player.png").convert_alpha()
star_surface = pygame.image.load("images/star.png").convert_alpha()

player_x = 100
player_y = 100

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(pygame.Color("orchid1"))

    player_x = player_x + 0.1

    display_surface.blit(player_surface,(player_x,player_y))
    #ekranın üstüne başka bir ekran eklemek için kullanılır

    for i in range(20):
        star_x = random.randint(0,1280)
        star_y = random.randint(0,720)
        display_surface.blit(star_surface,(star_x,star_y))

    pygame.display.update()
    
pygame.quit()