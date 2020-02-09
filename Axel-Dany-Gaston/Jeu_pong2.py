#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame, sys, random, math
from pygame.locals import *

WIDTH = 1000
HEIGHT = 600
FPS = 60
TITLE = "Mon jeu"
Vert = (0,255,0)
White = (255,255,255)


class Carre(pygame.sprite.Sprite):

    def _init_(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(White)
        self.image.set_colorkey(White)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

class Jeu():

    def __init__(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        pygame.display.set_caption('NotreFenetre')
        self.clock = pygame.time.Clock()

    def new(self):

        self.carres = pygame.sprite.Group()
        self.carres.add(Carre())
        for p in places:
            Carre = Carre()
            Carre.rect.x = p[0]
            Carre.rect.y = p[1]

    def update(self):
        self.all_sprites.update()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.new()
            self.update()
            self.draw()
            self.events()

    def draw(self):
        self.sprite.draw(self.fenetre)
        pygame.display.flip()
        Sprite.image = Carre

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

pygame.init()

fenetre = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Monjeu")

balle = Carre(Vert, 50, 50)
balle.rect.x = 100
balle.rect.y = 100

gpe_Carre = pygame.sprite.Group()
gpe_Carre.add(balle)

gpe_Carre.draw(fenetre)

while True:
    print()