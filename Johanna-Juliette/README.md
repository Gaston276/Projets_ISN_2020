## Pistes  à explorer

* [Récuperer des données de distance](https://docs.google.com/spreadsheets/d/10PVZZTfl0Czx4e1Z93wIK29ltrYIwFqLDqa6qmNy-rE/edit?usp=sharing)
* Voir le fichier beamer_dijkstra2.pdf, pour comprendre le fonction de l'algorithme
* pour travailler avec des dictionnaires  https://python.doctor/page-apprendre-dictionnaire-python
* Petit exercice
```Python
# Exemple graphe
#--------------------------------------------

g = {'D': {'B':2, 'C':6},
     'B': {'E':8, 'C':2},
     'C': {'E':5,'G':3},
     'E': {'F':1, 'A': 5,'G':4},
     'F': {'A':4},
     'G': {'A':8},
     'A':{}
     }
# Faire le dessin du graphe à la main
# Appliquer l'alogorithme  pour connaître la plus petite distance entre 'D' et 'A'
# on  veut les voisins d'un sommet donné, les distances des voisins au sommet donné.
# g['A'].get('E',float('inf')) Expliquer cette instruction
# Création d'un dictionnaire avec les distance à partir d'un sommet donné à tous les autres sommets (si l'arête n'existe pas on met float('inf')) 
# fonction qui retourne la plus petite distance avec le sommet correspondant
```
