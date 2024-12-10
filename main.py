import pygame
from sys import exit
#screen setup
pygame.init()
tabletop = pygame.display.set_mode((1200,880))
pygame.display.set_caption("Warhammer40k_Simulator")
#icon = pygame.image.load('icon.png')   #I don't have the file as png yet
#pygame.display.set_icon(icon)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
