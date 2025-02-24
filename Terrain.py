lass Terrain: #the terrain class where all info for terrain will be
    def __init__(self,name,radius,speed,height,onclick): 
        in_height = '' #need to initialise it so it can be used in the loop and same with below
        in_radius = '' # ditto 
        valid_shapes = [square,circle,elipse] #these are the shapes that can be used
        self.name = input("Enter the terrain's name: ")  #the name obvs
        self.radius = radius #this is not always the radius as i was originally only using circles this is just the size in inches of a shape
        self.speed = 99999 #this is how much it can move per turn 
        while isdigit(in_height) == False: #loop makes sure there is a valid input
            self.height = int(input("Enter the height of the terrain: ")) #units will able to climb over terrain so height is needed
            in_height = self.height        
        while in_shape not in valid_shapes: #makes sure input is valid
            self.shape = input("Enter the shape of the terrain piece (must be square, circle or elipse): ") #the shape of the terrain duh 
            in_shape = self.shape
        self.onclick = onclick #clicky stuff
        while isdigit(inradius) == False:
            self.radius = int(input("Enter the size of the Terrain piece: "))
            in_radius = self.radius

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
    def __init__(self,name,radius,speed,height,arange,melee,wounds,points):
        Super().__init__(name,radius,speed,height) #Inherits all the stuff from Terrain and allows to add more without the one above overriding
        self.arange = arange
        self.melee = melee
        self.wounds = wounds
        self.points = points
