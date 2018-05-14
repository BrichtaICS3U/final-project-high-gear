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
       myfont = pygame.font.SysFont("monospace", 15)
       background_image = pygame.image.load("tryit.png")
       titleText = pygame.image.load("titleText.png")
       def button(word,x,y,w,h,ic,ac,action=None):
           mouse = pygame.mouse.get_pos()
           click = pygame.mouse.get_pressed()
           if x+w > mouse[0] > x and y+h > mouse[1] > y:
                  pygame.draw.rect(screen, ac, (x,y,w,h))
                  
           else:
                  pygame.draw.rect(screen,ic,(x,y,w,h))
           buttonLable = myfont.render(str(word),1,[0,0,0])
           screen.blit(buttonLable,(x+(w/2),y+(h/2)))
           #screen.blit(buttonLable,(50,25))

       
       while carryOn:
       #[----------------Logic----------------]#
              for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                            quit()

              keys = pygame.key.get_pressed()
              if keys[pygame.K_t]:
                  carryOn = False
                  
              #label = myfont.render("Some text!", 1, (255,0,0))
              
              





       #[----------------Shapes----------------]#
              screen.fill([255,255,255])
              screen.blit(background_image, [0, 0])
              screen.blit(titleText, (70, 50))
              button("Press T to start!", 500,20,100,50,[5,95,5],[0,255,0], )
              pygame.display.flip()
              clock.tick(60)

       pygame.display.quit()





       
