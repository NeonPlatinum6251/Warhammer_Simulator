#import mysql.connector
import pygame
from sys import exit

def screensetup():#screen setup
    pygame.init()
    tabletop = pygame.display.set_mode((1200,880)) #origin is top left!!!
    pygame.display.set_caption("Warhammer40k_Simulator")
    #icon = pygame.image.load('icon.png')   #I don't have the file as png yet
    #pygame.display.set_icon(icon)
    pygame.draw.rect(tabletop,(176,176,176),(0,0,100,1200))
clock = pygame.time.Clock()
# Models = mysql.connector.connect(host = "localhost", user = "", password = "") #database not yet created
#mycursor = Models.cursor()
screensetup()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)

class Button(pygame.sprite):
    def __init__(self,)