import pygame, sys
pygame.init()

# Define some colours
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SCREENWIDTH = 700
SCREENHEIGHT = 500
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
background = pygame.image.load("imae.jpg")
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('menu-song.wav')
pygame.mixer.music.play(-1) 



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
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(80, 30), font_name="7 Squared Regular", font_size=10):
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

def helloFunction():
    """A generic function that prints something in the shell"""
    print('Hello in the shell')

def my_next_function():
    """A function that advances to the next level"""
    global level
    level += 1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 1

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()
def soundON():
    print("Sound: ON")
def soundOFF():
    pygame.mixer.music.pause()
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

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_01 = Button("PLAY", (SCREENWIDTH/2, 200), helloFunction,bg=(0,234,223))
button_04 = Button("SETTINGS", (SCREENWIDTH/2,240),my_next_function,bg = (0,212,19))
button_02 = Button("BACK", (SCREENWIDTH/2, 240), my_previous_function, bg = (0,212,19))
button_03 = Button("Quit", (SCREENWIDTH/2, 280), my_quit_function, bg=(212,0,0))
button_05 = Button("PAUSE", (SCREENWIDTH/2,200),soundOFF, bg=(0,234,223))
#arrange button groups depending on level
level1_buttons = [button_01, button_03, button_04]
level2_buttons = [button_02, button_03,button_05]

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
        pygame.draw.rect(screen, [255,255,255], (200,40,460,40))
        text = font.render("go fast weeeeeee!", 1, (10, 10, 10))
        screen.blit(text, (200,50))
        
        for button in level1_buttons:
            button.draw()
    elif level == 2:
        screen.blit(background,(0,0))
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, [255,255,255], (350,40,125,40))
        text = font.render("SETTINGS", 1, (10, 10, 10))
        screen.blit(text, (350,50)) 
        for button in level2_buttons:
            button.draw()

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
