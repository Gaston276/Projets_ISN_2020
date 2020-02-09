import sys,math,random,pygame

WIDTH = 1000
HEIGHT = 1000
FPS = 60
TITLE = "JeuLedion"


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE);
rectScreen = screen.get_rect()




#( image_fond = pygame.image.load("titouan.jpg").convert() )

#Background
fond = pygame.image.load("titouan.jpg").convert()

class Pion:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.v = 0
            self.r = 0
        
        def accelerer(self, acceleration):
            if self.v < 10 and self.v > 20 :
                self.v = acceleration + self.v
            elif self.v+acceleration <12 and self.v+acceleration >-2:
                self.v = acceleration + self.v

        def deplacer(self):
            self.x = self.v * cos(radians(self.r)) + self.x
            self.y = self.v * sin(radians(self.r)) + self.y

        def tourner(self,rotation):

            self.r = rotation + self.r


        def xy(self):
            return self.x, self.y

roi = pygame.image.load("RoiNoir.png").convert_alpha()
#Boucle
clock = pygame.time.Clock()
while True:
    screen.blit(roi,(500,500))
    pygame.display.flip()
    screen.blit(fond,(0,0))
    pygame.display.update()
    time = clock.tick(FPS)
pygame.quit()
    
