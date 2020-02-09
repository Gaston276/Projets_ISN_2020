from random import *

class zone :
    def __init__(self):
        self.maisons=0
        self.boutiques=0
        self.pnj=0
        self.ennemis=0
        self.boss=False
        self.chemins = [0,0,0,0] #[N,S,E,O]
        self.texte=''

class chateau :

class maison :
    def __init__(self):
        self.pnj=0
        self.potions=0
        self.argent=0
        self.texte=''

    def chercher(self):
        if self.potions>0 :
            self.potions=-1
            heros.potions=+1
        if self.argent>0 :
            heros.argent=+self.argent
            self.argent=0

class boutique :
    def __init__(self):
        self.epee=0
        self.prix_epee=self.epee*100
        self.bouclier=0
        self.prix_bouclier=self.bouclier*75
        self.potions=0
        self.prix_potion=50
        self.texte=''

    def vendre(self, heros, objet, n)
        if objet=1 :
            heros.epee=self.epee
            heros.argent=heros.argent-self.prix_epee

        if objet=2 :
            heros.bouclier=self.bouclier
            heros.argent=heros.argent-self.prix_bouclier

        if objet=3 :
            heros.potions=heros.potions+n
            heros.argent=heros.argent-(self.prix_potion*n)
            self.potions=self.potions-n


def initialisation_map():
    case1=zone()
    case1.maison=1
    case1.chemins=[0,0,8,0]
    maison_depart=maison()
    maison_départ.pnj=1
    tuto=pnj()

    case2=zone()
    case2.chemins=[3,0,7,0]

    case3=zone()
    case3.ennemis=1
    case3.chemins=[4,2,0,0]
    soldat_foret1=mechants()

    case4=zone()
    case4.chemins=[0,3,5,0]

    case5=zone()
    case5.ennemis=1
    case5.chemins=[0,6,12,4]
    soldat_foret2=mechants()

    case6=zone()
    case6.maison=2
    case6.boutique=1
    case6.chemins=[5,0,11,0]
    maison_foret1=maison()
    maison_foret2=maison()
    maison_foret2.pnj=1
    pnj_foret=pnj()
    boutique_foret=boutique()
    boutique_foret.epee=2
    boutique_foret.bouclier=1
    boutique_foret.potions=2

    case7=zone()
    case7.ennemis=1
    case7.chemins=[0,8,0,2]
    tuto_combat=mechants()

    case8=zone()
    case8.chemins=[7,0,0,2]

    case9=zone()
    case9.ennemis=1
    case9.chemins=[10,0,16,0]
    soldat_champs1=mechants()

    case10=zone()
    case10.pnj=1
    case10.chemins=[11,9,15,0]
    pnj_champs1=pnj()

    case11=zone()
    case11.ennemis=1
    case11.chemins=[12,10,14,6]
    soldat_champs2=mechants()

    case12=zone()
    case12.chemins=[0,11,0,5]

    case13=zone()
    case13.ennemis=2
    case13.boutique=1
    case13.chemins=[0,14,0,20]
    soldat_marchand1=mechants()
    soldat_marchand2=mechants()
    boutique=boutique()
    boutique.epee=4
    boutique.bouclier=3

    case14=zone()
    case14.chemins=[13,15,19,0]

    case15=zone()
    case15.ennemis=1
    case15.chemins=[14,16,18,10]
    soldat_champs3=mechants()

    case16=zone()
    case16.pnj=1
    case16.maison=1
    case16.chemins=[15,0,17,9]
    pecheur=pnj()
    maison_lac=maison()

    case17=zone()
    case17.ennemis=1
    case17.chemins=[18,0,24,16]
    soldat_lac=mechants()

    case18=zone()
    case18.ennemis=1
    case18.maison=0
    case18.chemins=[19,17,23,15]
    soldat_village1=mechants()
    maison_village1=maison()

    case19=zone()
    case19.pnj=0
    case19.ennemis=2
    case19.maison=3
    case19.chemins=[20,18,22,14]
    soldat_village2=mechants()
    soldat_village3=mechants()
    maison_village2=maison()
    maison_village3=maison()
    maison_village4=maison()

    case20=zone()
    casex.chemins=[0,19,21,13]

    case21=zone()
    case21.boutique=1
    case21.chemins=[0,0,0,20]
    cheat=boutique()
    cheat.epee=75
    cheat.prix_epee=0
    cheat.bouclier=75
    cheat.prix_bouclier=0
    cheat.potions=100
    cheat.prix_potions=0

    case22=chateau()

    case23=zone()
    casex.ennemis=3
    casex.maison=2
    casex.boutique=1
    casex.chemins=[22,24,0,18]
    soldat_ville1=mechants()
    soldat_ville2=mechants()
    soldat_ville3=mechants()
    maison_ville1=maison()
    maison_ville2=maison()
    boutique_ville=boutique()
    boutique_ville.epee=3
    boutique_ville.bouclier=2
    boutique_ville.potions=5

    casex=zone()
    casex.ennemis=1
    casex.maison=1
    casex.chemins=[23,0,0,17]
    soldat_village4=mechants()
    maison_village5=maison()