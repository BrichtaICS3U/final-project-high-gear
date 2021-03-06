# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
from Game import game, callLaps
#from Game import lap1
pygame.init()

# Define some colours
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
#global sMap
sMap = 1
scored = False
req = 0 
SCREENWIDTH = 900
SCREENHEIGHT = 800
time1 = 120
pygame.display.set_caption("REDLINE")
background = pygame.image.load("back.png")
wasd = pygame.image.load("wasd.png")
arr  = pygame.image.load("arr.png")
tips = pygame.image.load("tips.png")
logo = pygame.image.load("logo.png")
whatdo = pygame.image.load("whatdo.png")
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
fontTitle = pygame.font.Font('freesansbold.ttf', 32)
level = 1
carryOn = True
clock = pygame.time.Clock()
class Button():
    """This is a class for a generic button.
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(80, 30), font_name="Courier New", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()
        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GRAY  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()


def my_next_function():
    """A function that advances to the next level"""
    global level
    level = 2 

def howScreen():
    """Go to the instructions page"""
    global level
    level = 3

def tellMap():
    global sMap
    return sMap
"""
def map1Start():
    global level
    global sMap
    sMap = 1
    level = 2

"""
def nextMap():
    global level
    global sMap
    sMap += 1
    level = 2
 

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level = 1
    print("ya walid")

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 3:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 4:
        for button in level4_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 5:
        for button in level5_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 6:
        for button in level6_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()



#create button objects and store in buttons list
button_01 = Button("Play!", (SCREENWIDTH/2, SCREENHEIGHT/3), my_next_function,size = (140,30),bg=(20,255,20))
button_02 = Button("Previous", (700, 150), my_previous_function)
button_03 = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_quit_function, bg=(255, 20, 20))
button_04 = Button("Instructions", (SCREENWIDTH/2, SCREENHEIGHT/2), howScreen,size = (140,30))
#button_05 = Button("Map 1",(150,450),map1Start)
button_06 = Button("Try again",(450,475),my_next_function,size=(100,30))
button_07 = Button("Next map",(450,475),nextMap)
#button_07 = Button("Car 1",(350,350),redPick)
#arrange button groups depending on level
level1_buttons = [button_04, button_03, button_01]
level2_buttons = [button_02, button_03]
level3_buttons = [button_02]
level4_buttons = [button_03,button_07]
level5_buttons = [button_02,button_02]
level6_buttons = [button_03,button_06] 

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)
    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)
    # Draw buttons
    if level == 1:
        screen.blit(background,(0,0))
        font = pygame.font.Font(None, 36)
        text = font.render("REDLINE", 1, (0,0,0))
        screen.blit(logo,(278,35))
        for button in level1_buttons:
            button.draw()

    elif level == 2:
        game()
        lap1,lap2,lap3,laps = 0,0,0,0
        lap1,lap2,lap3,laps = callLaps()
        if int(lap1+lap2+lap3) <= time1 and laps >= 3:
            level = 4
        else:
            level = 6
    elif level == 3:
        screen.blit(background,(0,0))
        screen.blit(whatdo,(0,325))
        screen.blit(wasd,(15,45))
        screen.blit(tips, (450,400))
        screen.blit(arr,(245,45))
        font = pygame.font.Font(None, 36)
        text = font.render("'How do I work this thing?'", 1, (0,0,0))
        asdw1 = font.render("W: Boost", 1, (0,0,0))
        asdw2 = font.render("S: Clutch", 1, (0,0,0))
        asdw3 = font.render("D: Gear Up", 1, (0,0,0))
        asdw4 = font.render("A: Gear Down", 1, (0,0,0))
        oh1 = font.render("^: Accelerate", 1, (0,0,0))
        oh2 = font.render("v: Brake", 1, (0,0,0))
        oh3 = font.render(">: Turn Right", 1, (0,0,0))
        oh4 = font.render("<: Turn Left", 1, (0,0,0))
        screen.blit(text, ((SCREENWIDTH/2), (35)))
        screen.blit(asdw1,((35),(180)))
        screen.blit(asdw2,((35),(200)))
        screen.blit(asdw3,((35),(220)))
        screen.blit(asdw4,((35),(240)))
        screen.blit(oh1,((285),(180)))
        screen.blit(oh2,((285),(200)))
        screen.blit(oh3,((285),(220)))
        screen.blit(oh4,((285),(240)))   
        for button in level3_buttons:
            button.draw()
    elif level == 4:
        screen.blit(background,(0,0))
        onelap = font.render("Lap 1: " + str(int(lap1)) + "s", 1, (0,0,0))
        twolap = font.render("Lap 2: " + str(int(lap2)) + "s", 1, (0,0,0))
        thrlap = font.render("Lap 3: " + str(int(lap3)) + "s", 1, (0,0,0))
        flap = font.render("Total: " + str(int(lap1 + lap2 + lap3)), 1, (0,0,0))
        result = font.render("You finished the track!",3,(0,0,0))
        screen.blit(result,(400,200))
        screen.blit(onelap,((35),(180)))
        screen.blit(twolap,((35),(200)))
        screen.blit(thrlap,((35),(220)))
        screen.blit(flap,((35),(260)))
        for button in level4_buttons:
            button.draw()
    elif level == 5:
        screen.blit(background,(0,0))
        tit = font.render("Select Level!", 1, (0,0,0))
        screen.blit(tit,((400),(180)))
        for button in level5_buttons:
            button.draw()
    elif level == 6:
        screen.blit(background,(0,0))
        result = font.render("You failed to finish the track...",3,(0,0,0))
        onelap = font.render("Lap 1: " + str(int(lap1)) + "s", 1, (0,0,0))
        twolap = font.render("Lap 2: " + str(int(lap2)) + "s", 1, (0,0,0))
        thrlap = font.render("Lap 3: " + str(int(lap3)) + "s", 1, (0,0,0))
        flap = font.render("Total: " + str(int(lap1 + lap2 + lap3)), 1, (0,0,0))
        screen.blit(onelap,((35),(180)))
        screen.blit(twolap,((35),(200)))
        screen.blit(thrlap,((35),(220)))
        screen.blit(flap,((35),(260)))
        screen.blit(result,(400,200))
        for button in level6_buttons:
            button.draw()

    # Update the screen with queued shapes
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
