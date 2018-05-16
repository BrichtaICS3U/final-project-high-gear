def mainMenu():
       
       #[----------------Imports----------------]#
       
       import pygame
       pygame.init()
       #ghang
       #[----------------init----------------]#
       clock = pygame.time.Clock()
       SCREENWIDTH =  900
       SCREENHEIGHT = 850
       size = (SCREENWIDTH, SCREENHEIGHT)
       screen = pygame.display.set_mode(size)
       pygame.display.set_caption("menu1")
       myfont = pygame.font.SysFont("monospace", 15)
       background_image = pygame.image.load("tryit.png")
       titleText = pygame.image.load("titleText.png")
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
           def __init__(self, txt, location, action, bg=(255,255,255), fg=(0,0,0), size=(80, 30), font_name="Segoe Print", font_size=16):
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
                   self.bg = (40,40,40)  # mouseover color

           def call_back(self):
               """Runs a function when clicked"""
               self.call_back_()
               
       def playAdvance():
              """A function that advances to the next level"""
              global level
              level += 2

       def settingsAdvance():
              """A function that retreats to the previous level"""
              global level
              level += 1
              
       def playReturn():
              global level
              level -= 2

       def settingsReturn():
              global level
              level -= 1

       def gameQuit():
              """A function that will quit the game and close the pygame window"""
              pygame.quit()
              sys.exit()

       def mousebuttondown(level):
              """A function that checks which button was pressed"""
              pos = pygame.mouse.get_pos()

       level = 1
       carryOn = True
       while carryOn:
              #[----------------Shapes----------------]#
              screen.fill([255,255,255])
              screen.blit(background_image, [0, 0])
              screen.blit(titleText, (70, 50))
              #create button objects and store in buttons list
              button_01 = Button("PLAY", (SCREENWIDTH/2, SCREENHEIGHT/4), playAdvance, [198,40,40], [255,255,255], (200,50))
              button_02 = Button("Previous", (SCREENWIDTH/2, SCREENHEIGHT/3), playReturn)
              button_03 = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*2/3), gameQuit, bg=(50, 200, 20))

              #arrange button groups depending on level
              level1_buttons = [button_01, button_03]
              level2_buttons = [button_02, button_03]
                  #screen.blit(buttonLable,(50,25))

              #[----------------Logic----------------]#
              for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                            quit()




              #[----------------Buttons----------------]#
              #button("PLAY", (SCREENWIDTH/3), (SCREENHEIGHT/4),200,50,[198,40,40],[66,66,66], )
              if level == 1:
                     for button in level1_buttons:
                            button.draw()
              elif level == 2:
                     for button in level2_buttons:
                            button.draw()
              pygame.display.flip()
              clock.tick(60)

       pygame.display.quit()





       
