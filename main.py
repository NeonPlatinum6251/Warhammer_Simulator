import pygame
from sys import exit
#screen setup
pygame.init()
tabletop = pygame.display.set_mode((1200,880))
pygame.display.set_caption("Warhammer40k_Simulator")
#icon = pygame.image.load('icon.png')   #I don't have the file as png yet
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()

test_surface = pygame.Surface((80,80))
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tabletop.blit(test_surface,(0,0)) #origin is top left!!!
    pygame.display.update()
    clock.tick(60)
