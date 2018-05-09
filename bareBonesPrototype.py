# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
import math 
from car import Car
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
RED = (200, 0, 0)
# Open a new window
# The window is defined as (width, height), measured in pixels
SCREENWIDTH = 900
SCREENHEIGHT = 850
x = 0
y = 0
xRatio = 0
yRatio = 0
clutched = False
all_sprites_list = pygame.sprite.Group()
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
background = pygame.image.load("FURYROAD.png")
pygame.display.set_caption("REDLINE")
fontTitle = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceTitle = fontTitle.render("wowzers", True, RED) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (200, 150)

 # --- Text elements
PlayerCar = Car([255,0,0],40,20,0, 0, 2,2,1)
PlayerCar.rect.centerx = SCREENWIDTH/2
PlayerCar.rect.centery = SCREENHEIGHT/2
all_sprites_list.add(PlayerCar)
# Define text for title of game

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
            
    # Get mouse location
    mouse = pygame.mouse.get_pos()
    #print(mouse) # Uncomment to see mouse position in shell
    # Check if mouse is pressed
    click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        PlayerCar.accl()
    if keys[pygame.K_DOWN]:
        PlayerCar.slDown()
    if keys[pygame.K_LEFT]:
        PlayerCar.rotRight()
        screen.blit(PlayerCar.image, (SCREENWIDTH/2,SCREENHEIGHT/2))
    if keys[pygame.K_RIGHT]:
        PlayerCar.rotLeft()
    if keys[pygame.K_s]:
        clutched = True
    else:
        clutched = False
    xRatio = math.cos(math.radians(PlayerCar.angle))
    yRatio = math.sin(math.radians(PlayerCar.angle))
    xSpeed = xRatio * PlayerCar.speed
    ySpeed = yRatio * PlayerCar.speed
    if PlayerCar.speed >= 20:
        PlayerCar.speed = 20
    if clutched == True:
        PlayerCar.acclRate = 0
    print(PlayerCar.angle, PlayerCar.speed, xRatio, xSpeed, clutched)

    #print(click) # Uncomment to see mouse buttons clicked in shell
    PlayerCar.drag()
    # --- Draw code goes here
    all_sprites_list.update()
    # Clear the screen to white
    screen.fill([255,255,255])
    x -= xSpeed
    y += ySpeed 
    screen.blit(background, (x, y))
    # Queue shapes to be drawn
    all_sprites_list.draw(screen)
    pygame.draw.rect(screen,[0,0,0],[700,750,100,50])
    label = fontTitle.render(str(PlayerCar.speed), 1, (255,255,0))
    screen.blit(label, (725, 750))
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
