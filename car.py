import pygame
WHITE = (255,255,255)

class Car(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, angle, speed, acclRate, breakRate, dragRate):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle
        self.speed = speed
        self.dragRate = dragRate
        self.breakRate = breakRate
        self.acclRate = acclRate
        #pygame.draw.rect(self.image, color, [0,0,width,height])
        self.image = pygame.image.load("car.png").convert_alpha()
        self.rect = self.image.get_rect()


    def accl(self):
        self.speed += self.acclRate
    def drag(self):
        if self.speed > 0:
            self.speed -= self.dragRate
        if self.speed < 0:
            self.speed += self.dragRate
    def slDown(self):
        if self.speed > 0:
            self.speed -= self.breakRate
        if self.speed < 0:
            self.speed += self.breakRate
    def rotRight(self):
        self.angle += 3
    def rotLeft(self):
        self.angle -= 3
        
   
