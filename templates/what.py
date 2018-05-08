import pygame

screenWidth = 900
screenHeight = 800
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Redline")
background = pygame.image.load("imae.jpg")
clock = pygame.time.Clock()

def button(word,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
        else:
            pygame.draw.rect(screen,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w / 2)), (y + (h / 2)) )
    screen.blit(textSurf, textRect)

intro()
def intro():
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
        screen.blit(background,(0,0))
        screen.blit(TextSurf, TextRect)
        
        button("Quit", 550, 450, 100, 50,[95,5,5],[255,0,0],quit)
        button("GO!", 100,450,100,50,[5,95,5],[0,255,0],game)
        
        pygame.display.update()
        clock.tick(60)
            
