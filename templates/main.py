import pygame, random
from car import Car
pygame.init()



screenWidth = 900
screenHeight = 800
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Dodge")  


#display.update
clock = pygame.time.Clock()
def text_objects(text, font):
    textSurface = font.render(text, True, [0,0,0])
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))

        if click[0] == 1 and action != None:
            action()
            
    else:
        pygame.draw.rect(screen, ic, (w,y,w,h))
        
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w / 2)), (y + (h / 2)) )
    screen.blit(textSurf, textRect)
    
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill([255,255,255])
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Fistfull of Cars", largeText)
        TextRect.center = ((screenWidth/2),(screenHeight/2))
        screen.blit(TextSurf, TextRect)
        
        button("Quit", 550, 450, 100, 50,[95,5,5],[255,0,0],quit)
        button("GO!", 100,450,100,50,[5,95,5],[0,255,0],game)
        
        pygame.display.update()
        clock.tick(60)



def game():
        carryOn = True
        GREEN = (20, 255, 140)
        GREY = (210, 210 ,210)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        PURPLE = (255, 0, 255)
        YELLOW = (255, 255, 0)
        CYAN = (0, 255, 255)
        BLUE = (100, 100, 255)

        speed = 1
        colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)
        all_sprites_list = pygame.sprite.Group()

        playerCar = Car(RED, 20, 30, 70)
        playerCar.rect.x = 200
        playerCar.rect.y = screenHeight - 100

        car1 = Car(PURPLE, 60, 80, random.randint(50, 100))
        car1.rect.x = 160
        car1.rect.y = -100

        car2 = Car(YELLOW, 60, 60, random.randint(50,100))
        car2.rect.x = 60
        car2.rect.y = -100

        car3 = Car(CYAN, 60, 80, random.randint(50,100))
        car3.rect.x = 260
        car3.rect.y = -300

        car4 = Car(BLUE, 60, 80, random.randint(50,100))
        car4.rect.x = 360
        car4.rect.y = -900

        all_sprites_list.add(playerCar)
        all_sprites_list.add(car1)
        all_sprites_list.add(car2)
        all_sprites_list.add(car3)
        all_sprites_list.add(car4)

        all_coming_cars = pygame.sprite.Group()
        all_coming_cars.add(car1)
        all_coming_cars.add(car2)
        all_coming_cars.add(car3)
        all_coming_cars.add(car4)
        while carryOn:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        carryOn = False
            
                    elif event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_x:
                            carryOn = False
            
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    playerCar.moveLeft(5)
                if keys[pygame.K_RIGHT]:
                    playerCar.moveRight(5)
                if keys[pygame.K_UP]:
                    speed += 0.05
                if keys[pygame.K_UP]:
                    speed -= 0.05

                for car in all_coming_cars:
                     car.moveForward(speed)
                     if car.rect.y > screenHeight:
                        car.changeSpeed(random.randint(50,100))
                        car.repaint(random.choice(colorList))
                        car.rect.y = -200

                car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
                for car in car_collision_list:
                    print("Car crash!")

                    carryOn = False
 
                all_sprites_list.update()

            
                screen.fill(GREEN)

                pygame.draw.rect(screen, GREY, [40,0, 400,screenHeight])
        
                pygame.draw.line(screen, WHITE, [140,0],[140,screenHeight],5)

                pygame.draw.line(screen, WHITE, [240, 0], [240, screenHeight], 5)

                pygame.draw.line(screen, WHITE, [340, 0], [340,screenHeight], 5)
        
                all_sprites_list.draw(screen)
 
                pygame.display.flip()

                clock.tick(60)

game_intro()
 
pygame.quit()
