import pygame, sys, random, math
pygame.init
from pygame.locals import *
import time

size = widht, height = 1020, 720
title = "PACMAN"
WHITE = (255, 255, 255)
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
DIRECTION = [K_DOWN,K_UP,K_LEFT,K_RIGHT]


fenetre = pygame.display.set_mode(size)
pygame.display.set_caption(title);
pygame.init()



#-----------------------PACMAN--------------------------------------------------
class Pacman():
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.bloque = None
        self.vitesse = 5
        # on connait la taille de notre image
        self.image = pygame.Surface([30,30])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # defini une image pour Pacman
        self.image = pygame.image.load("pacman.png").convert_alpha()
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
            
            
    def avance(self,direction):
        if self.bloque == None:
            if direction == K_RIGHT:
                self.rect.x += self.vitesse
                self.image = pygame.image.load("pacman.png").convert_alpha()
            elif direction == K_LEFT:
                self.rect.x -= self.vitesse
                self.image = pygame.image.load("pacman1.png").convert_alpha()
            elif direction == K_UP:
                self.rect.y -= self.vitesse
                self.image = pygame.image.load("pacman2.png").convert_alpha()
            elif direction == K_DOWN:
                self.rect.y += self.vitesse
                self.image = pygame.image.load("pacman3.png").convert_alpha()
                pygame.display.flip()


    #Add this draw function so we can draw individual sprites
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    #Sauvegarde la direction qui a produit le contact
    def collision_sol(self,direction):
        if self.bloque == None:
            self.bloque = direction
        elif self.bloque != direction:
            self.bloque = None


# Déplacement de Pacman
        if event.type== KEYDOWN:
            if event.key in DIRECTION:
                        if (pygame.sprite.collide_mask(Pacman,Mur)):
                            mess = "Tu a été touché"
                            print(pygame.sprite.collide_mask(Mur,Pacman),event.key)
                            Pacman.collision_sol(event.key)
                        else:
                            Pacman.bloque = None

                        Pacman.avance(event.key)

        # Test la collision entre un sprite et un groupe de sprites pixel perfect
        collision=pygame.sprite.spritecollide(Pacman,gpe_murs, False, pygame.sprite.collide_mask)
        if collision:
            mess = " Collision avec les murs"

pygame.key.set_repeat(2,00)


#-----------------------MUR ----------------------------------------------------
class Mur(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # on connait la taille de notre image
        self.image = pygame.Surface([30,30])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # defini une image pour le mur
        self.image = pygame.image.load("mur.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
#-------------------------------------------------------------------------------


#-----------------------POINT---------------------------------------------------
class Point(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # on connait la taille de notre image
        self.image = pygame.Surface([30,30])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # defini une image pour le mur
        self.image = pygame.image.load("point.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
#-------------------------------------------------------------------------------


#-----------------------POINT---------------------------------------------------
class PointGros(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # on connait la taille de notre image
        self.image = pygame.Surface([30,30])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # defini une image pour le mur
        self.image = pygame.image.load("pointGros.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
#-------------------------------------------------------------------------------


map = [[1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
       [1,3,2,2,2,2,2,1,0,1,2,2,2,2,2,3,1],
       [1,2,1,1,2,1,2,2,2,2,2,1,2,1,1,2,1],
       [1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1],
       [1,2,2,1,2,2,2,2,1,2,2,2,2,2,2,2,1],
       [1,1,2,1,2,1,1,2,2,2,1,1,2,1,2,1,1],
       [1,2,2,2,2,2,1,1,2,1,1,2,2,1,2,2,1],
       [1,2,1,2,1,2,2,2,2,2,2,2,1,1,1,2,1],
       [1,2,1,2,1,2,1,1,2,1,1,2,2,2,2,2,1],
       [1,2,1,2,1,2,2,2,2,2,2,2,1,2,1,2,1],
       [1,2,2,2,1,2,1,1,1,1,1,2,1,2,1,2,1],
       [1,2,1,1,1,2,1,0,0,0,1,2,2,2,2,2,1],
       [1,2,2,2,2,2,1,0,0,0,1,2,1,1,1,2,1],
       [1,2,1,2,1,2,1,1,0,1,1,2,1,2,2,2,1],
       [1,2,1,2,1,2,2,2,2,2,2,2,1,2,1,2,1],
       [1,2,2,2,2,2,1,1,2,1,1,2,1,2,1,2,1],
       [1,2,1,1,1,2,2,2,2,2,2,2,1,2,1,2,1],
       [1,2,2,1,2,2,1,1,2,1,1,2,2,2,2,2,1],
       [1,1,2,1,2,1,1,2,2,2,1,1,2,1,2,1,1],
       [1,2,2,2,2,2,2,2,1,2,2,2,2,1,2,2,1],
       [1,2,1,1,2,1,2,1,1,1,2,1,2,1,1,2,1],
       [1,2,1,1,2,1,2,2,2,2,2,1,2,1,1,2,1],
       [1,3,2,2,2,2,2,1,0,1,2,2,2,2,2,3,1],
       [1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1]]
        


gpe_murs = pygame.sprite.Group()
for i,l in enumerate(map):
    
    for j,c in enumerate(l):
        if c==1:
            brique = Mur()
            brique.rect.x = j*30+510
            brique.rect.y = i*30
            gpe_murs.add(brique)
            

gpe_point = pygame.sprite.Group()
for i,l in enumerate(map):
    
    for j,c in enumerate(l):
        if c==2:
            point = Point()
            point.rect.x = j*30+510
            point.rect.y = i*30
            gpe_murs.add(point)



gpe_pointGros = pygame.sprite.Group()
for i,l in enumerate(map):
    
    for j,c in enumerate(l):
        if c==3:
            pointGros = PointGros()
            pointGros.rect.x = j*30+510
            pointGros.rect.y = i*30
            gpe_murs.add(pointGros)


pygame.display.flip() 

continuer=True
perso = Pacman()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit(0)
        mess = ""
        if event.type==pygame.QUIT:
            continuer=False
            sys.exit(0)
            
        if event.type== KEYDOWN:
            perso.avance(event.key)
         
    fenetre.fill((0,0,0))
    gpe_murs.draw(fenetre)
    perso.draw(fenetre)
    pygame.display.flip()