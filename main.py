import pygame
from sys import exit

class Terrain: #the terrain class where all info for terrain will be
    def __init__(self,onclick=None): 
        in_height = None #need to initialise it so it can be used in the loop and same with below
        in_radius = None # ditto 
        valid_shapes = ["square","circle","ellipse"] #these are the shapes that can be used
        self.name = ""
        self.radius = 0
        self.speed = 0 #this is how much it can move per turn
        self.shape = ""
        self.height = ""
        self.onclick = onclick #clicky stuff

        self.name_box = InputBox(300,100,200,32, "Enter Terrain name: ")
        self.height_box = InputBox(300,100,200,32, "Enter Terrain Height: ")
        self.shape_box = InputBox(300,100,200,32,"enter Terrain Shape ")
        self.radius_box = InputBox(300,100,200,32, "enter terrain size: ")

        self.questions = ["name","height", "shape", "radius"]
        self.currentquestion = 0

    def update(self,event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.next_question()
        else:
            if self.currentquestion ==0:
                self.name_box.clickbox(event)
            elif self.currentquestion == 1:
                self.height_box.clickbox(event)
            elif self.currentquestion == 2:
                self.shape_box.clickbox(event)
            elif self.currentquestion == 3:
                self.radius_box.clickbox(event)
        
    def draw(self, screen):
        screen.fill((0,0,0))
        if self.currentquestion == 0:
            self.name_box.draw(screen)
        elif self.currentquestion == 1:
            self.height_box.draw(screen)
        elif self.currentquestion == 2:
            self.shape_box.draw(screen)
        elif self.currentquestion == 3:
            self.radius_box.draw(screen)

    def next_question(self):
        if self.currentquestion == 0 and self.name_box.text:
            self.name = self.name_box.text
            self.name_box.text = ""
            self.currentquestion += 1
        elif self.currentquestion == 1 and self.height_box.text:
            try:
                self.height = int(self.height_box.text)
                self.height_box.text = ""
                self.currentquestion += 1
            except ValueError:
                print("Invalid height input!")
        elif self.currentquestion == 2 and self.shape_box.text:
            self.shape = self.shape_box.text
            self.shape_box.text = ""
            self.currentquestion += 1
        elif self.currentquestion == 3 and self.radius_box.text:
            try:
                self.radius = int(self.radius_box.text)
                self.radius_box= ""
                self.currentquestion += 1
            except ValueError:
                print("Invalid radius input!")

    def is_complete(self):
        return self.currentquestion >= len(self.questions)
 
    def drawterrain(self,x,y,shape): #draws the model as the chosen values
        if shape == 'square':
            pygame.draw.rect(tabletop, green, (x,y,self.radius,self.radius)) #so why you drawing a f@#!ing circle then
        elif shape == 'circle':
            pygame.draw.circle(tabletop, green,(x + size // 2, y + self.radius // 2),self.radius //2)
        elif shape == 'elipse':
            pygame.draw.ellipse(tabletop, green, (x,y,self.radius,self.radius // 2))
        else:
            print("Theres an Error somewhere buddy!")
    
class Model(Terrain): #terrain is the parent class to models 
    def __init__(self):
        super().__init__() #Inherits all the stuff from Terrain and allows to add more without the one above overriding
        self.arange = 12
        self.melee = 2
        self.wounds = 5
        self.points = 90
        self.x = 250
        self.y=250

    def drawmodel(self,tabletop):
        pygame.draw.circle(tabletop,(255,0,0),(self.x,self.y) ,self.radius)
    '''
    def move(self,new_x, new_y, grid):
        grid_x = new_x // 10
        grid_y = new_y // 10
        if grid[grid_y][grid_x] is None:
            self.x = new_x
            self.y =new_y
    '''     
pygame.font.init()
COLOR_INACTIVE = pygame.Color("blue")
COLOR_ACTIVE = pygame.Color("green")
base_font =pygame.font.Font(None,32)

class InputBox:
    def __init__(self,x,y,w,h,label=""):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = COLOR_INACTIVE
        self.text = ""
        self.txt_surface = base_font.render(self.text, True, self.color)
        self.active = False
        self.label = label
    def clickbox(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:  
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = base_font.render(self.text, True, self.color)
    def update(self):
        width = max(200,self.txt_surface.getwidth()+10)
        self.rect.w = width 
    def draw(self,screen):
        label_surface = base_font.render(self.label,True,pygame.Color("white"))
        screen.blit(label_surface, (self.rect.x, self.rect.y -25))
        pygame.draw.rect(screen, pygame.Color("black"),self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5,self.rect.y + 5))
        pygame.draw.rect(tabletop,self.color, self.rect, 2)

#initialise variables and lists

base_terrain_pieces = []
base_models = [] #these are the starting models , might make it an array
selected_model = None #which model is selected 
pygame.init() #initialises pygame
tabletop = pygame.display.set_mode((1200,880)) #origin is top left!!! # i could make some tabletops with some pngs 
pygame.display.set_caption("Warhammer40k_Simulator") #this names the window 
#icon = pygame.image.load('icon.png')   #I don't have the file as png yet
#pygame.display.set_icon(icon)
 # draw the hotbar
clock = pygame.time.Clock() 
mouse = pygame.mouse
green = (0,255,0)

gridsize = 10 #the amount of pixels an individual square takes up in the grid  
gridwidth = 120 #how many squares wide
gridheight = 90 # how many squares tall
grid =[[None for _ in range(gridwidth)] for _ in range(gridheight)] #creates the grid as an empty 2D array 

#test objects
testmodel = Model()

while True:  #this is the main loop where all the display stuff will happen
    tabletop.fill((0,0,0))
    for event in pygame.event.get(): #when an event happens 
        if event.type == pygame.QUIT: #this loop makes sure python closes properly
            pygame.quit() #stops 
            exit()
        testmodel.update(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            testmodel.next_question()
    testmodel.draw(tabletop)
    if testmodel.is_complete():
          testmodel.drawmodel(tabletop)
    pygame.draw.rect(tabletop,(176,176,176),(0,0,100,1200))
    pygame.display.update() #updates whats on the screen
    clock.tick(60)

'''
class Button: #for clicking
    def __init__(self,x,y,bwidth,bheight,buttontext,onclick): 
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
#def drag_n_drop():
'''
