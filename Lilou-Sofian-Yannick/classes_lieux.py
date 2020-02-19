
class zone :
    def __init__(self):
        self.maison=0
        self.boutique=0
        self.pnj=0
        self.ennemis=0
        self.boss=False
        self.chemins = [0,0,0,0] #[N,S,E,O]
        self.texte=''

class chateau :
    def __init__(self):
        self.type='chateau'

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

    def vendre(self, heros, objet, n): #1=épée, 2=bouclier, 3=potions, n=nombre potions
        if objet==1 :
            heros.epee=self.epee
            heros.argent=heros.argent-self.prix_epee

        if objet==2 :
            heros.bouclier=self.bouclier
            heros.argent=heros.argent-self.prix_bouclier

        if objet==3 :
            heros.potions=heros.potions+n
            heros.argent=heros.argent-(self.prix_potion*n)
            self.potions=self.potions-n

