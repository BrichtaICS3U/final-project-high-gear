# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
def game(): 
        
    import pygame
    import math
    import time
    from car import Car
    pygame.init()

    # Define some colours
    # Colours are defined using RGB values
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 200, 0)
    BRIGHT_GREEN = (0, 255, 0)
    RED = (200, 0, 0)
    col = (0,0,0)
    # Open a new window
    # The window is defined as (width, height), measured in pixels
    SCREENWIDTH = 900
    SCREENHEIGHT = 800
    x = 0
    y = 0
    ook = 500
    dg = 0
    whomst = 0
    xRatio = 0
    yRatio = 0
    clutched = False
    laps = 0
    done = False
    check1 = False
    check2 = False
    check3 = False
    #cleared = USEREVENT + 1
    lap1 = 0
    lap2 = 0
    lap3 = 0
    seconds = 0
    all_sprites_list = pygame.sprite.Group()
    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("maps/thebest!.png")
    pygame.display.set_caption("REDLINE")
    fontTitle = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceTitle = fontTitle.render("wowzers", True, RED) 
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (200, 150)

     # --- Text elements
    PlayerCar = Car([255,0,0],20,40,90, 0, 2,2,1,1, 7)
    PlayerCar.rect.centerx = SCREENWIDTH/2
    PlayerCar.rect.centery = SCREENHEIGHT/2
    all_sprites_list.add(PlayerCar)
    # Define text for title of game

    # This loop will continue until the user exits the game
    carryOn = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
    start_ticks=pygame.time.get_ticks()
    while carryOn:
        # --- Main event loop ---
        for event in pygame.event.get(): # Player did something
            if event.type == pygame.QUIT: # Player clicked close button
                carryOn = False
            if event.type == pygame.KEYUP and event.key == [pygame.K_d]:
                gear += 1
                
        col = screen.get_at((int((PlayerCar.rect.centerx+30)+math.radians(900*xRatio)),int((PlayerCar.rect.centery+30)-math.radians(1000*yRatio))))
        # Get mouse location
        mouse = pygame.mouse.get_pos()
        REDLINE = PlayerCar.gear * 5
        minSpeed = REDLINE - 10 
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
            #screen.blit(PlayerCar.image, (SCREENWIDTH/2,SCREENHEIGHT/2))
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
        if laps > 0:
            seconds=(pygame.time.get_ticks()-start_ticks)/1000#
        if PlayerCar.speed >= REDLINE:
            ook += 1
            PlayerCar.speed = REDLINE
        if keys[pygame.K_w] and ook > 0:
            ook -= 5
            PlayerCar.speed += 15
        if clutched == True:
            PlayerCar.acclRate = 0
        else:
            PlayerCar.acclRate = 2
        if PlayerCar.gear == 0:
            PlayerCar.acclRate = -1
            #REDLINE = -5
        else:
            PlayerCar.acclRate = 2
            #REDLINE = PlayerCar.gear * 5
        if clutched == True and keys[pygame.K_d] and dg == 0 and PlayerCar.gear < 6:
            PlayerCar.gear += 1
            dg += 1
        if clutched == True and keys[pygame.K_a] and dg == 0 and PlayerCar.gear > 0:
            PlayerCar.gear -= 1
            dg += 1
        if dg == 1 and keys[pygame.K_d] == False and keys[pygame.K_a] == False:
            dg = 0
        if col == (35, 178, 77, 255):
            if PlayerCar.speed > 6:
                PlayerCar.speed -= 3
        #if col == (238, 29, 37, 255):
            #laps += 1
        if col == (255, 128, 40, 255):
            check1 = True
        if col == (164, 74, 165, 255):
            check2 = True
        if col == (1, 163, 233, 255):
            check3 = True
        if col == (238, 29, 37, 255) and check1 == True and check2 == True and check3 == True:
            if int(laps) == 1:
                lap1 = seconds
            elif laps == 2:
                lap2 = seconds - lap1
            elif laps == 3:
                lap3 = seconds - (lap2 + lap1)
                lap3 = seconds - (lap1 + lap2) 
            seconds = 0
            #pygame.time.set_timer(cleared,0)
            laps += 1
            check1 = False
            check2 = False
            check3 = False
        elif laps == 0 and col == (238, 29, 37, 255):
            laps += 1
        if PlayerCar.speed < minSpeed:
            PlayerCar.speed -= 1
        if laps >= 4:
            laps = 3
            done = True
        #PlayerCar.speed += PlayerCar.acclRate
        print(int(seconds), check1, check2, check3)
        #print(PlayerCar.angle, PlayerCar.speed, PlayerCar.acclRate, clutched, dg,minSpeed)

        #print(click) # Uncomment to see mouse buttons clicked in shell
        PlayerCar.drag()
        #dg = 0     
        # --- Draw code goes here
        all_sprites_list.update()
        # Clear the screen to white
        screen.fill([255,255,255])
        x -= xSpeed
        y += ySpeed 
        screen.blit(background, (x, y))
        # Queue shapes to be drawn
        all_sprites_list.draw(screen)
        if check1 == True:
            pygame.draw.rect(screen,[255, 128, 40, 255],[0,0,30,30])
        if check2 == True:
            pygame.draw.rect(screen,[164, 74, 165, 255],[30,0,30,30])
        if check3 == True:
            pygame.draw.rect(screen,[1, 163, 233, 255],[60,0,30,30])
        pygame.draw.rect(screen,[0,100,255],[0,30,15,ook])
        #pygame.draw.ellipse(screen, [0,0,0], [475,450,5,5])
        #pygame.draw.ellipse(screen, [0,0,0], [(PlayerCar.rect.centerx+30)+math.radians(900*xRatio),(PlayerCar.rect.centery+30)-math.radians(1000*yRatio),5,5])
        label1 = fontTitle.render("Speed: " + str(PlayerCar.speed * 3), 1, (255,255,0))
        label2 = fontTitle.render("Gear: " + str(PlayerCar.gear), 1, (255,255,0))
        label3 = fontTitle.render("Lap: " + str(laps), 1, (255,255,0))
        label4 = fontTitle.render("Lap 1: " + str(int(lap1)) + "s", 1, (255,255,0))
        label5 = fontTitle.render("Lap 2: " + str(int(lap2)) + "s", 1, (255,255,0))
        label6 = fontTitle.render("Lap 3: " + str(int(lap3)) + "s", 1, (255,255,0))
        athing = fontTitle.render("Track Finished!", 1, (255,255,0))
        if done == True:
            screen.blit(athing, (400,450))
        screen.blit(label1, (725, 700))
        screen.blit(label2, (725, 725))
        screen.blit(label3, (725, 750))
        screen.blit(label4, (25, 700))
        screen.blit(label5, (25, 725))
        screen.blit(label6, (25, 750))
        # Update the screen with queued shapes
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Once the main program loop is exited, stop the game engine
    pygame.quit()
