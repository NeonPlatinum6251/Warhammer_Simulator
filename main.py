#libraries
from Terrain import Terrain
import pygame
from sys import exit

#initialise variables and lists
base_terrain_pieces = []
base_models = [] #these are the starting models , might make it an array
pygame.init() #initialises pygame
tabletop = pygame.display.set_mode((1200,880)) #origin is top left!!! # i could make some tabletops with some pngs 
pygame.display.set_caption("Warhammer40k_Simulator") #this names the window 
#icon = pygame.image.load('icon.png')   #I don't have the file as png yet
#pygame.display.set_icon(icon)
pygame.draw.rect(tabletop,(176,176,176),(0,0,100,1200)) # draw the hotbar make it scrollable by taking the scroll input moving stuff and when it tocuhes a tiny bar at the top to make it disapear
clock = pygame.time.Clock() 
mouse = pygame.mouse()

gridsize = 10
gridwidth = 120
gridheight = 90
grid =[[None for _ in range(gridwidth)] for _ in range(gridheight)]

while True:  #this is the main loop where all the display stuff will happen
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #this loop makes sure python closes properly
            pygame.quit() 
            exit()
        #if event.type == pygame.MOUSEBUTTONDOWN:

    pygame.display.update() #updates whats on the screen
    clock.tick(60)

#im gonna write some of my classes here

class Button: #for clicking
    def __init__(self,x,y,bwidth,bheight,buttontext,onclick): #I JUST REMEMBERED MODELS AND STUFF NEED BUTTON FUNCTIONS DELETE THIS GIVE the STUFF TO Terrrain instead trust me/ nah its chill just needs on click
        self.x = x
        self.y = y
        self.bwidth = bwidth
        self.bheight = bheight
        self.buttontext = buttontext
        self.onclick = onclick
        self.font = pygame.font.Font(None,24)
        
    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 100), (self.x, self.y, self.bwidth, self.bheight))
        text_surface = self.font.render(self.buttontext, True, (255, 255, 255))
        surface.blit(text_surface, (self.x + 5, self.y + 5))

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if self.x <= mx <= self.x + self.bwidth and self.y <= my <= self.y + self.bheight:
                self.onclick()
    
def placefirstmodels(basemodels): # places the starting models in the hotbar 
    model_there = True #used to check if there is already a model where its trying to place
    #for i in len(base_models): #does it for each starter model
        #while model_there == True: 
            #if # a model is at placex and placey
                #placey += 400 #move it down
            #else: #all good?
                #drawterrain(placex,placey) #draw it in the place 
                #model_there = False #makes sure it doesnt do it again
def 
