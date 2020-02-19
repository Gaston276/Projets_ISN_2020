def initialisation_map():
    l = [[0 for i in range(5)] for j in range(3)]
    for k in range(5) :
        for l in range(3) :
            l[k][l] = zone()

    l[0][1].ennemis=1
    soldat_foret1=mechants()

    l[0][3].maison=1
    maison_depart=maison()
    maison_depart.pnj=1
    tuto=pnj()

    l[1][0].ennemis=1
    soldat_foret2=mechants()

    l[1][1].maison=2
    l[1][1].boutique=1
    maison_foret1=maison()
    maison_foret2=maison()
    maison_foret2.pnj=1
    pnj_foret=pnj()
    boutique_foret=boutique()
    boutique_foret.epee=2
    boutique_foret.bouclier=1
    boutique_foret.potions=2

    l[1][2].ennemis=1
    tuto_combat=mechants()

    l[2][3].ennemis=1
    soldat_champs1=mechants()

    l[2][2].pnj=1
    pnj_champs1=pnj()

    l[2][1].ennemis=1
    soldat_champs2=mechants()

    l[3][0].ennemis=2
    l[3][0].boutique=1
    soldat_marchand1=mechants()
    soldat_marchand2=mechants()
    boutique1=boutique()
    boutique1.epee=4
    boutique1.bouclier=3

    l[3][2].ennemis=1
    soldat_champs3=mechants()

    l[3][3].pnj=1
    l[3][3].maison=1
    l[3][3].chemins=[15,0,17,9]
    pecheur=pnj()
    maison_lac=maison()

    l[4][3].ennemis=1
    soldat_lac=mechants()

    l[4][2].ennemis=1
    l[4][2].maison=0
    soldat_village1=mechants()
    maison_village1=maison()

    l[4][1].pnj=0
    l[4][1].ennemis=2
    l[4][1].maison=3
    soldat_village2=mechants()
    soldat_village3=mechants()
    maison_village2=maison()
    maison_village3=maison()
    maison_village4=maison()

    l[5][0].boutique=1
    cheat=boutique()
    cheat.epee=75
    cheat.prix_epee=0
    cheat.bouclier=75
    cheat.prix_bouclier=0
    cheat.potions=100
    cheat.prix_potions=0

    l[5][1]=chateau()

    l[5][2].ennemis=3
    l[5][2].maison=2
    l[5][2].boutique=1
    soldat_ville1=mechants()
    soldat_ville2=mechants()
    soldat_ville3=mechants()
    maison_ville1=maison()
    maison_ville2=maison()
    boutique_ville=boutique()
    boutique_ville.epee=3
    boutique_ville.bouclier=2
    boutique_ville.potions=5

    l[5][3].ennemis=1
    l[5][3].maison=1
    soldat_village4=mechants()
    maison_village5=maison()