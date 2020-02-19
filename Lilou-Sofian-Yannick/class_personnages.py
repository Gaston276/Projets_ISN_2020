from random import *

class heros :
    def __init__(self) :
        self.epee=0
        self.force=self.epee*25
        self.bouclier=0
        self.potions=0
        self.argent=100
        self.defense=False
        self.pv=50
        self.pvmax=50
        self.esquive=10

    def combat(self,soldat) :
        self.force=self.epee*25
        self.esquive=10
        self.defense=False
        x=int(input("Que voulez vous faire ? 1=Attaquer, 2=Défendre, 3=Esquiver, 4=Utiliser une potion"))
        if x==1 :
            attaque(self,soldat)
        if x==2 :
            self.defense=True
        if x==3 :
            self.esquive=33
        if x==4 :
            if self.potions>0 :
                if self.pvmax-self.pv>10:
                    self.potions-=1
                    self.pv+=10
                    print("Il vous reste ", self.potions," potions et vous avez dorénavant ", self.pv, " points de vie")
                else :
                    if self.pvmax-self.pv>0 & self.pvmax-self.pv<=10 :
                        self.potions-=1
                        self.pv+=self.pvmax-self.pv
                        print("Vous avez atteint le nombre de points de vie maximum, soit ", self.pv,", et il vous reste ", self.potions, " potions.")
                    else :
                        print("Vous avez déjà atteint votre nombre de points de vie maximum, vous ne pouvez pas utiliser de potions.")
            else :
                print("Vous ne possédez plus de potions")

class pnj :
    def __init__(self) :
        maison=False


class mechants :
    def __init__(self) :
        self.force=15
        self.defense=False
        self.esquive=10
        self.pv=25
        self.epee=0
        self.bouclier=0
        self.potions=1
        self.argent=5

    def combat(self,heros) :
        self.esquive=10
        x=randint(1,3) #1=attaque 2=defense 3=dodge
        if x==1 :
            print("attaque")
            attaque(self, heros)
        if x==2 :
            print("defense")
            self.defense=True
        if x==3 :
            print("esquive")
            self.esquive=self.esquive*2


class boss :
    def __init__(self) :
        self.force= 50
        self.pv=1000
        self.argent=100
        self.epee=4
        self.potions=4

    def attaquer(self) :
        attaque(self, heros)
