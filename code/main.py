#display surface:
#the canvas that everything will be drawn on
#you can only have one at a time

#event loop
#check events
#this also include x to close the game

#print(pygame.ver)

#pygame.init() tam tersi pygame.quit()

#pygame.display.update()
#tüm ekranı günceller
#pygame.display.flip()
#ekranın bir kısmını günceller

import pygame 

#general setup
pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
running = True

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    display_surface.fill("pink")
    pygame.display.update()
    
pygame.quit()