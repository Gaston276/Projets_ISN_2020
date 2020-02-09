import sys,math,random,pygame

# PARAMETRES DU JEU
WIDTH = 640
HEIGHT = 480
FPS = 60
TITLE = "Mon jeu"
BLEU = (0,0,255)

class Carre(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.Surface(50,50)
        self.image.fill(BLEU)
        self.image.set_colorkey(BLEU)



# INITIALISATION DU JEU
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE);
rectScreen = screen.get_rect()


# ... A COMPLETER AVEC LE CODE DE VOS INITIALISATIONS ...
carre = pygame.image.load("bleu-carre.png").convert_alpha()
rectCarre = bleu-carre.get_rect()
rectChat.topleft = (100,50)
# BOUCLE DE JEU
clock = pygame.time.Clock()
while True:
	time = clock.tick(FPS)

	# GESTION DES EVENEMENTS
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
screen.blit(carre,rectCarre)


	# ... A COMPLETER AVEC LE CODE DE VOTRE JEU ...

	# MAJ DE L'AFFICHAGE



