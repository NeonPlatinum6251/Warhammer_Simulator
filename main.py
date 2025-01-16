#import mysql.connector
import pygame
from sys import exit

#screen setup
pygame.init()
tabletop = pygame.display.set_mode((1200,880)) #origin is top left!!!
pygame.display.set_caption("Warhammer40k_Simulator")
#icon = pygame.image.load('icon.png')   #I don't have the file as png yet
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#Models = mysql.connector.connect(host = "localhost", user = "", password = "") #database not yet created 
def modelsinit():
    center = (0,0)
    singlemodel = pygame.draw.circle(tabletop,'red',center,3,0)
    
testcircle = modelsinit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.blit(singlemodel)
    pygame.display.update()
    clock.tick(60)
