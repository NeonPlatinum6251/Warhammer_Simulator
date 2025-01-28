#import mysql.connector
import pygame
from sys import exit

pygame.init()
tabletop = pygame.display.set_mode((1200,880)) #origin is top left!!!
pygame.display.set_caption("Warhammer40k_Simulator")
#icon = pygame.image.load('icon.png')   #I don't have the file as png yet
#pygame.display.set_icon(icon)
pygame.draw.rect(tabletop,(176,176,176),(0,0,100,1200)) # draw the hotbar

clock = pygame.time.Clock()
# Models = mysql.connector.connect(host = "localhost", user = "", password = "") #database not yet created
#mycursor = Models.cursor()

def runscreen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update() #updates whats on the screen
        clock.tick(60)

#im gonna write all my classes here
class Terrain:
    def __init__(self,name,radius,speed,height):
        self.name = name #the name obvs
        self.radius = radius #this is not always the radius as i was originally only using circles this is just the size in inches of a shape
        self.speed = speed #this is how much it can move per turn 
        self.height = height #units will able to climb over terrain so height is needed
        self.shape = shape #the shape of the terrain duh 

class Model(Terrain):
    def__init__(self,name,radius,speed,height,):
        Super().__init__(name,radius,speed,height) #Inherits all the stuff from Terrain and allows to add more without the one above overriding
#lowkey cant remeber what i was gonna put here so im not doing it rn


def createTerrain():
    inheight = '' #need to initialise it so it can be used in the loop and same with below
    inradius = ''
    validshapes = [square,circle,elipse] #these are the shapes that can be used
    inname = input("Enter the terrain's name: ") 
    inspeed = 9999 #Terrain cannot move at all in a game so it is very high so it can be moved anywhere on the board
    while isdigit(inheight) == False:  #can't have any invalid inputs now can we
        inheight = int(input("Enter the height of the Terrain piece: "))
    while inshape not in validshapes:
        inshape = input("Enter the shape of the terrain piece (must be square, circle or elipse): ")
    while isdigit(inradius) == False:
        inradius = int(input("Enter the size of the Terrain piece: "))
    terraininfo = Terrain(inname,inradius,inspeed,inheight)
    return terraininfo #spit all that info out into something

def drawterrain():
    info=createTerrain()
    if info.shape == 'square':
        pygame.draw.rect(tabletop,green,(400,600,info.radius,info.radius)) #draws it for now but im thinking i make it a surface then blit it for collisions and such
    elif info.shape == 'circle':
    elif info.shape == 'elipse':
    else:
        print("Theres an Error somewhere buddy") #not sure when this would happen but I imagine the error would be in createTerrain

    
    
