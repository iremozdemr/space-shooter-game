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

#blit():
#ekranın üstüne başka bir ekran eklemek için kullanılır

import pygame 
import random

pygame.init()
pygame.display.set_caption("space shooter")
running = True
clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((1280,720))

star_surface = pygame.image.load("images/star.png").convert_alpha()
star_positions = []*20

for i in range(20):
    star_x = random.randint(0,1280)
    star_y = random.randint(0,720)

    star_positions.append((star_x,star_y))

meteor_surface = pygame.image.load("images/meteor.png").convert_alpha()
meteor_rectangle = meteor_surface.get_rect(center = (640,360))

laser_surface = pygame.image.load("images/laser.png").convert_alpha()
laser_rectangle = laser_surface.get_rect(bottomleft = (20,700))

player_surface = pygame.image.load("images/player.png").convert_alpha()
player_rectangle = player_surface.get_rect(center = (640,360))
player_direction = pygame.math.Vector2(0,0)
player_speed = 300

while running:
    dt = clock.tick(100) / 1000

    display_surface.fill(pygame.Color("darkgray"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(20):
        display_surface.blit(star_surface,star_positions[i])

    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    
    if player_rectangle.left <= 0 or player_rectangle.right >= 1280:
        player_direction.x *= -1

    if player_rectangle.top <= 0 or player_rectangle.bottom >= 720:
        player_direction.y *= -1
    
    player_rectangle.center += player_direction * player_speed * dt

    display_surface.blit(meteor_surface,meteor_rectangle)
    display_surface.blit(laser_surface,laser_rectangle)
    display_surface.blit(player_surface,player_rectangle)

    pygame.display.update()
    
pygame.quit()