#libraries
#import mysql.connector
import pygame
from sys import exit

#initialise global variables and lists
basemodels = [] #these are the starting models , might make it an array
pygame.init() #initialises pygame
tabletop = pygame.display.set_mode((1200,880)) #origin is top left!!! # i could make some tabletops with some pngs 
pygame.display.set_caption("Warhammer40k_Simulator") #this names the window 
#icon = pygame.image.load('icon.png')   #I don't have the file as png yet
#pygame.display.set_icon(icon)
pygame.draw.rect(tabletop,(176,176,176),(0,0,100,1200)) # draw the hotbar make it scrollable by taking the scroll input moving stuff and when it tocuhes a tiny bar at the top to make it disapear
clock = pygame.time.Clock() #
# Models = mysql.connector.connect(host = "localhost", user = "", password = "") #database not yet created
#mycursor = Models.cursor()

while True:  #this is the main loop where all the display stuff will happen
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #this loop makes sure python closes properly
            pygame.quit() 
            exit()
    pygame.display.update() #updates whats on the screen
    clock.tick(60)

#im gonna write all my classes here
class Terrain: #the terrain class where all info for terrain will be
    def __init__(self,name,radius,speed,height,onclick): 
        inheight = '' #need to initialise it so it can be used in the loop and same with below
        inradius = '' # ditto 
        validshapes = [square,circle,elipse] #these are the shapes that can be used
        self.name = input("Enter the terrain's name: ")  #the name obvs
        self.radius = radius #this is not always the radius as i was originally only using circles this is just the size in inches of a shape
        self.speed = 99999 #this is how much it can move per turn 
        while isdigit(inheight) == False: #loop makes sure there is a valid input
            self.height = int(input("Enter the height of the terrain: ")) #units will able to climb over terrain so height is needed
            inheight = self.height        
        while inshape not in validshapes: #makes sure input is valid
            self.shape = input("Enter the shape of the terrain piece (must be square, circle or elipse): ") #the shape of the terrain duh 
            inshape = self.shape
        self.onclick = onclick #clicky stuff
        while isdigit(inradius) == False:
            self.radius = int(input("Enter the size of the Terrain piece: "))
            inradius = self.radius

    def drawterrain(placex,placey): #draws the model as the chosen values
        if self.shape == 'square':
            pygame.draw.rect(tabletop,green,(placex,placey,info.radius,info.radius)) #draws it for now but im thinking i make it a surface then blit it for collisions and such
        elif self.shape == 'circle':
            pass
        elif self.shape == 'elipse':
            pass
        else:
            print("Theres an Error somewhere buddy!") #not sure when this would happen but I imagine the error would be in 
        

class Model(Terrain): #terrain is the parent class to models 
    def __init__(self,name,radius,speed,height,arange,melee,wounds):
        Super().__init__(name,radius,speed,height) #Inherits all the stuff from Terrain and allows to add more without the one above overriding
        self.arange = arange
        self.melee = melee
        self.wounds = wounds

class Button: #for clicking
    def __init__(self,x,y,bwidth,bheight,buttontext,onclick): #I JUST REMEMBERED MODELS AND STUFF NEED BUTTON FUNCTIONS DELETE THIS GIVE the STUFF TO Terrrain instead trust me/ nah its chill just needs on click
        self.x = x
        self.y = y
        self.bwidth = bwidth
        self.bheight = bheight
        self.buttontext = buttontext
        self.onclick = onclick

def placefirstmodels(basemodels): # places the starting models in the hotbar 
    modelthere = True #used to check if there is already a model where its trying to place
    for i in len(basemodels): #does it for each starter model
        while modelthere == True: 
            #if # a model is at placex and placey
                placey += 400 #move it down
            else: #all good?
                drawterrain(placex,placey) #draw it in the place 
                modelthere = False #makes sure it doesnt do it again

def 

        
