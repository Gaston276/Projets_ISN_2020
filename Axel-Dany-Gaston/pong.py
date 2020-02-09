import sys,math,random,pygame
from pygame.locals import *

WIDTH = 1100
HEIDGHT = 600
FPS = 60
TITLE = "PONG"

class Carre(pygame.sprite.Sprite):

    def __init__(self):
    
        super().__init__()
    
        self.image = pygame.Surface([300,300])
        self.image.fill(BLUE)
        self.image.set_colorkey(BLUE)
        self.image = pygame.image.load("carre.png").convert_alpha()
        self.rect = self.image.get_rect()

class Etoile(pygame.sprite.Sprite):

    def __init__(self):
    
        super().__init__()
    
        self.image = pygame.Surface([300,300])
        self.image.fill(BLUE)
        self.image.set_colorkey(BLUE)
        self.image = pygame.image.load("bonus étoile.png").convert_alpha()
        self.rect = self.image.get_rect()


pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIDGHT))
pygame.display.set_caption(TITLE)
rectScreen = screen.get_rect

places = [(0,50)]

clock = pygame.time.Clock()
while True:
    time = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit(0)
            
    keys = pygame.key.get_pressed()
    vxCarre = 50
    vyCarre = 30
    
    
    pygame.display.update()