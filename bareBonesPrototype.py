# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
RED = (200, 0, 0)
bx = 0
by = -424
# Open a new window
# The window is defined as (width, height), measured in pixels
SCREENWIDTH = 800
SCREENHEIGHT = 600

background = pygame.image.load("imae.png")

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Button")
speed = 1
topSpeed = 150
accelRate = 2
slowRate = 1
gear = 1
angle = 90
clutch = False
# --- Text elements

# Define text for title of game
fontTitle = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceTitle = fontTitle.render(str(gear), True, RED) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (200, 150)   # place the centre of the text

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
    relvar = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        clutch = True
        accelRate = 0
    else:
        clutch = False
        accelRate = 2
    if keys[pygame.K_UP]:
        speed += accelRate
    if clutch == True and keys[pygame.K_d] and relvar == 0:
        gear += 1
        relvar == 1
    if clutch == True and on_key_release(pygame.K_d):
        relvar == 0
    if clutch == True and keys[pygame.K_a]:
        gear -= 1
    if speed > (30 * gear):
        speed = (30*gear)
    if speed > 0:
        speed -= slowRate
    if speed > topSpeed:
        speed = topSpeed

    # Get mouse location
    mouse = pygame.mouse.get_pos()
    #print(mouse) # Uncomment to see mouse position in shell

    # Check if mouse is pressed
    click = pygame.mouse.get_pressed()
    #print(click) # Uncomment to see mouse buttons clicked in shell
    print(speed, clutch, gear)
    # --- Draw code goes here

    # Clear the screen to white

    bx += 0.5
    by += speed
    screen.blit(background,(0,by))
    screen.blit(background,(0,by))
    #screen.blit(background, (bx,by))
    # Queue shapes to be drawn
    pygame.draw.rect(screen,[255,0,0],[300,400,30,50],0)
    # Buttons

    # Green button
    
    # Red button
    

    # Text
    screen.blit(textSurfaceTitle, textRectTitle)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
