def mainMenu():
       
       #[----------------Imports----------------]#
       
       import pygame
       pygame.init()
       
       #[----------------init----------------]#
       clock = pygame.time.Clock()
       SCREENWIDTH =  900
       SCREENHEIGHT = 850
       size = (SCREENWIDTH, SCREENHEIGHT)
       screen = pygame.display.set_mode(size)
       pygame.display.set_caption("menu1")
       carryOn = True
       
       
       
       while carryOn:
       #[----------------Logic----------------]#
              for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                            carryOn = False
       






       #[----------------Shapes----------------]#
              screen.fill([255,255,255])
              pygame.display.flip()
              clock.tick(60)

       pygame.quit()





                     
       
