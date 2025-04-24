import pygame # imports the pygame library 
from sys import exit 

class Terrain: #the terrain class for terrain piece objects 
    def __init__(self,onclick=None): 
        valid_shapes = ["square","circle","ellipse"] #these are the shapes that can be used
        self.name = "" #the name of the terrain 
        self.radius = 0 #the size of the terrain 
        self.speed = 0 #this is how much it can move per turn
        self.shape = "" #the shape the terrain will be 
        self.height = "" # how tall the terrain is (not seen but will affect things)
        self.onclick = onclick #what happens when it is clicked 
        self.dragging = False #if the terrain is being dragged 
        self.x = 200 #the x position of the terrain, 200 is the default when it is created 
        self.y = 200 #same as above jsut  the y position 
        self.thing = None #this is a variable for  storing the shape that is drawn of the piece 
        self.name_box = InputBox(300,100,200,32, "Enter Terrain name: ") #these are the question boxes that appeared when a piece is created 
        self.height_box = InputBox(300,100,200,32, "Enter Terrain Height: ")
        self.shape_box = InputBox(300,100,200,32,"enter Terrain Shape ")
        self.radius_box = InputBox(300,100,200,32, "enter terrain size: ")
        self.questions = ["name","height", "shape", "radius"]
        self.currentquestion = 0 #the current question it is on when creating a new model 0 is the first one so it is the ddefault 
        self.font = pygame.font.Font(None,24) #the font used for when text is drawn on itself and its question boxes 
        self.color = green #the colour a terrain piece will be 

    def update(self,event): #this function makes the question boxes appear if a model is created and not completed 
        if not self.is_complete(): #checks if completed 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: #checks if enter has been pressed 
                self.next_question() # if it has calls the next_qustion fucntion 
            else:
                if self.currentquestion ==0: #checks what question its on 
                    self.name_box.clickbox(event) #checks if the input box is clicked
                elif self.currentquestion == 1:
                    self.height_box.clickbox(event)
                elif self.currentquestion == 2:
                    self.shape_box.clickbox(event)
                elif self.currentquestion == 3:
                    self.radius_box.clickbox(event)
        
    def draw(self, screen): #this function draws the question boxes depending on what question it is on 
        if not self.is_complete():
            if self.currentquestion == 0:
                self.name_box.draw(screen) #draws the question box 
            elif self.currentquestion == 1:
                self.height_box.draw(screen)
            elif self.currentquestion == 2:
                self.shape_box.draw(screen)
            elif self.currentquestion == 3:
                self.radius_box.draw(screen)
            else: 
                pass 

    def next_question(self): 
        if self.currentquestion == 0 and self.name_box.text: #this if statement is for the name question 
            self.name = self.name_box.text #makes the name in the input the name of the model 
            self.name_box.text = "" #initialises the text in the box as an empty string 
            self.currentquestion += 1 #increments a variable that denotes the question it is on  
        elif self.currentquestion == 1 and self.height_box.text: #this is for the height question 
            try:   #this is so invalid data cannot be inputted 
                self.height = int(self.height_box.text) #height is an integer
                self.height_box.text = "" 
                self.currentquestion += 1 
            except ValueError:
                print("Invalid height input!") #make this print to the screen 
        elif self.currentquestion == 2 and self.shape_box.text: #this is for the shape 
            self.shape = self.shape_box.text
            self.shape_box.text = ""
            self.currentquestion += 1
        elif self.currentquestion == 3 and self.radius_box.text: #for the radius 
            try:
                self.radius = int(self.radius_box.text)
                self.radius_box.text= ""
                self.currentquestion += 1
            except ValueError:
                print("Invalid radius input!")

    def is_complete(self): #function checks if the question counter variable has become greater than the amount of questions 
        return self.currentquestion >= len(self.questions) #returns a True or False 
 
    def drawterrain(self,x,y,shape,): #draws the model as the chosen values 
        if shape == 'square': #checks which shape the terrain is 
            pygame.draw.rect(tabletop, self.color, (x,y,self.radius,self.radius)) #draws the shape using its attributes 
            self.thing = pygame.Rect(x,y,self.radius,self.radius) #also holds the values for the shape, this is used for dragging 
            name_surface = self.font.render(self.name, True, (255, 255, 255)) #draws the name of the model onto it 
            tabletop.blit(name_surface, (self.x, self.y)) #draws it to the screen 
        elif shape == 'circle':
            pygame.draw.circle(tabletop, self.color,(x + self.radius, y + self.radius),self.radius)
            self.thing = pygame.Rect(x,y,self.radius,self.radius)
            name_surface = self.font.render(self.name, True, (255, 255, 255))
            tabletop.blit(name_surface, (self.x, self.y))
        elif shape == 'elipse':
            pygame.draw.ellipse(tabletop, self.color, (x,y,self.radius,self.radius))
            self.thing = pygame.Rect(x,y,self.radius,self.radius)
            name_surface = self.font.render(self.name, True, (255, 255, 255))
            tabletop.blit(name_surface, (self.x, self.y))        

class Model(Terrain): #terrain is the parent class to models 
    def __init__(self):
        super().__init__() #Inherits all methods stuff from Terrain
    
        self.name_box = InputBox(300,100,200,32, "Enter Model name: ") #the questions for the models 
        self.shape_box = InputBox(300,100,200,32,"enter Model Shape ")
        self.radius_box = InputBox(300,100,200,32, "enter Model size: ")
        self.questions = ["name","shape", "radius"]
        self.color = blue #the colour models will be 
    def quick_create(self,name,radius,speed,arange,melee,wounds,points,x,y): #this functions allows a model to be created without questions being asked 
        self.name = name
        self.radius = radius 
        self.speed = speed #how far it can move per turn 
        self.arange = arange #the range of a units weapon
        self.melee = melee #the melee range of a unit 
        self.wounds = wounds #how many hits to kill a unit 
        self.points = points #how many points a unit is worth 
        self.x = x
        self.y = y 
        self.shape = "circle" #models are always circles 
        self.currentquestion = 5 #quick create wants no questions asked 
        testmodel.append(self) #add it to the list of models 
    
    def slow_create(self): #create a models using questions 
        self.currentquestion = 0 

pygame.font.init() # initialises the pygame fonts 
COLOR_INACTIVE = pygame.Color("blue") # the colour of an input box when it is not active, this being when not clicked on 
COLOR_ACTIVE = pygame.Color("green") # the colour of an input box when its active 
base_font =pygame.font.Font(None,32) # the basic font i will be using 

class InputBox: #this class is used for question box objects  
    def __init__(self,x,y,w,h,label=""): #w and h being being height and width and label being the question being asked 
        self.rect = pygame.Rect(x,y,w,h) #the rectangle it will draw 
        self.color = COLOR_INACTIVE #the box will be inactive when first created 
        self.text = "" #the text is the text the user will write into the box  
        self.txt_surface = base_font.render(self.text, True, self.color) #where it will be drawn and what font it will use 
        self.active = False #if it is active or not , it starts of inactive 
        self.label = label 
    def clickbox(self, event): #this method is for when the box is clicked  
        if event.type == pygame.MOUSEBUTTONDOWN: #checks if the mouse is clicking 
            if self.rect.collidepoint(event.pos): #checks if the mouse is touching the box 
                self.active = not self.active # makes itself active meaning it can be typed in 
            else:
                self.active = False #if not, makes it inactive 
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE #changes the colour of the box depending if it active or npt 
        if event.type == pygame.KEYDOWN: #if the user is typing
            if self.active: # and it is active 
                if event.key == pygame.K_RETURN: #and the button pressed is enter
                    print(self.text) 
                    self.text = '' # empty the box 
                elif event.key == pygame.K_BACKSPACE:  #if the button pressed is backspace 
                    self.text = self.text[:-1] #takes the last letter typed away 
                else:
                    self.text += event.unicode #if its not either of these buttons add the button pressed to the text typed 
                self.txt_surface = base_font.render(self.text, True, self.color) #render the text 
    def update(self): #this method widens the box if the text starts going out /i dont think it does 
        width = max(200,self.txt_surface.getwidth()+10)
        self.rect.w = width 
    def draw(self,screen):  #this method renders all the parts of the box to the screen 
        label_surface = base_font.render(self.label,True,pygame.Color("white")) # the question 
        screen.blit(label_surface, (self.rect.x, self.rect.y -25)) #^
        pygame.draw.rect(screen, pygame.Color("black"),self.rect) #box
        screen.blit(self.txt_surface, (self.rect.x + 5,self.rect.y + 5)) #words inside 
        pygame.draw.rect(tabletop,self.color, self.rect, 2) # ^

class Button: #this is used for button objects such as the create new model button 
    def __init__(self,x,y,w,h,buttontext="",onclick=None): 
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.buttontext = buttontext
        self.onclick = onclick
        self.font = pygame.font.Font(None,24)
        self.rect = pygame.Rect(self.x,self.y,self.w, self.h)

    def draw(self, surface): #draws it to screen 
        pygame.draw.rect(tabletop, (100, 100, 100), self.rect)
        text_surface = self.font.render(self.buttontext, True, (255, 255, 255))
        surface.blit(text_surface, (self.x + 5, self.y + 5))

    def check_click(self, event): #cheks if it is being clicked and if it is call that onclick is connected to  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.onclick:
                    self.onclick()

def create_terrain(): #creates a new terrain 
    newmodel = Terrain() #newmodel is made a terrain which automatically calls all the stuff to create it as it is not complete 
    testmodel.append(newmodel) #adds it to the list of models 
    print(newmodel)
    print(len(testmodel))

def create_model(): #similar to above but for models 
    newmodel1 = Model() 
    newmodel1.slow_create() #slow create needs to be called to create a model yourself 
    testmodel.append(newmodel1)
    
#initialise variables and lists
testmodel = [] # list of models 
selected_model = None #which model is selected 
pygame.init() #initialises pygame
tabletop = pygame.display.set_mode((1200,880)) # i could make some tabletops with some pngs 
pygame.display.set_caption("Warhammer40k_Simulator") #this names the window 
#icon = pygame.image.load('icon.png')   #I don't have the file as png yet
#pygame.display.set_icon(icon)

clock = pygame.time.Clock() #these are just abbreviations 
mouse = pygame.mouse
green = (0,255,0) #the colour green 
blue = (0,0,255)

#test objects
testbutton = Button(110,800,150,50,"create new Terrain",create_terrain) #create new terrain button 
modelbutton = Button(110,720,150,50,"create new model",create_model) #create new model button 
dragging = False #deez nuts 
pointfont = pygame.font.Font(None,24)

def pointcounter():
    totalpoints = 0 
    for model in testmodel:
        if model:
            totalpoints += model.points
    pointstext = "Army Value:" + str(totalpoints)
    pointsurface = pointfont.render(pointstext,True,(255,255,255))
    tabletop.blit(pointsurface, (550,0))


def placebasemodels(): #this function creates some default models 
    Terminator = Model()
    Terminator.quick_create("Terminator",50,5,24,2,5,34,1,20)
    testmodel.append(Terminator)

    Einhyr_Heartguard = Model()
    Einhyr_Heartguard.quick_create("Terminator",50,5,24,3,6,30,1,140)
    testmodel.append(Einhyr_Heartguard)

placebasemodels()


while True:  #this is the main loop where all the things that are seen and need to happen every frame 
    for event in pygame.event.get(): #when an event happens 
        if event.type == pygame.QUIT: #this loop makes sure python closes properly
            pygame.quit() #stops 
            exit() #mega stops 

        testbutton.check_click(event) #checks if the buttons are clicked 
        modelbutton.draw(tabletop)
        modelbutton.check_click(event)

        #// go through each model because im awesome :3 #elflove
        for model in testmodel:
            if model:
                model.update(event) #finish creating models if they are not done 

    tabletop.fill((0,0,0)) # clears the screen 
    pygame.draw.rect(tabletop,(176,176,176),(0,0,100,1200)) #draws the hotbar 
    pointcounter()
    for model in testmodel:
        if model:
            if model.is_complete(): #checks if the model is complete
                model.drawterrain(model.x,model.y,model.shape)
            model.draw(tabletop)
        
    if all(model.is_complete() for model in testmodel):
        testbutton.draw(tabletop)
        modelbutton.draw(tabletop)
    
    modelbutton.check_click(event)
    for model in testmodel: #dragging and dropping is really really iffy and not just the loops badum tss 
            if model:
                if model.thing:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x,mouse_y = pygame.mouse.get_pos()
                        if model.thing.collidepoint(event.pos):
                            selected_model = model 
                            offset_x = mouse_x - model.x
                            offset_y = mouse_y - model.y

                    if event.type == pygame.MOUSEBUTTONUP:
                        selected_model = None 
        
                    if selected_model and event.type == pygame.MOUSEMOTION:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        selected_model.x = mouse_x - offset_x
                        selected_model.y = mouse_y - offset_y
    
    pygame.display.update() #updates whats on the screen
    clock.tick(60)

    '''
    stuff i need to add for it to be complete:
    when no mouse motion and model not touching hotbar and not clicked display all the range and shit   
    models cannot be placed on top of each other
    '''
    # i could make some tabletops with some pngs 
