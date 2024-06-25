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

#rectangle oluşturma:

#1-en baştan oluşturabilirsin:
#pygame.Rect(pos,size)
#pygame.FRect(pos,size)

#2-surface kullanarak oluşturabilirsin:
#surface size = rectangle size
#pygame.get_rect(point = pos)
#pygame.get_frect(point = pos)

import pygame 
import random
import math

pygame.init()

pygame.display.set_caption("space shooter")
running = True

display_surface = pygame.display.set_mode((1280,720))
player_surface = pygame.image.load("images/player.png").convert_alpha()
star_surface = pygame.image.load("images/star.png").convert_alpha()

player_rectangle = player_surface.get_rect(center = (60,60))
num = player_rectangle.left

star_positions = []*20

for i in range(20):
    star_x = random.randint(0,1280)
    star_y = random.randint(0,720)

    star_positions.append((star_x,star_y))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(pygame.Color("darkgray"))

    for i in range(20):
        display_surface.blit(star_surface,star_positions[i])

    num += 0.1
    player_rectangle.left = math.floor(num)

    display_surface.blit(player_surface,player_rectangle)
    #ekranın üstüne başka bir ekran eklemek için kullanılır

    pygame.display.update()
    
pygame.quit()