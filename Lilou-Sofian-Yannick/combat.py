def attaque(attaquant, victime) :
    r=randint(1,100)
    print(r)
    if r>=victime.esquive :
        if victime.defense==True & victime.bouclier*5<attaquant.force :
            victime.pv-=(attaquant.force-victime.bouclier)
            print(victime.pv)
        else :
            if victime.defense==False & victime.bouclier*3<attaquant.force :
                victime.pv-=(attaquant.force-victime.bouclier)
                print(victime.pv)
            else :
                print("defense")
    else :
        print("esquive")