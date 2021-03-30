


liste_animaux= ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]


liste_animaux.sort()
print(liste_animaux)
liste_animaux.reverse()
print(liste_animaux)

liste_animaux.append("troll")
print(liste_animaux)

animaux_dom=["lapin", "chat", "chien", "chiot"]

for i in animaux_dom:
    liste_animaux.remove(i)
    print(liste_animaux)

# !/usr/bin/python3
#  -*- coding : UTF-8 -*-
from random import *
from random import randint


tableau_jeu=[]
for i in range (0,10):
    tableau_jeu.append(randint(1,10))
print(tableau_jeu)


nombre=int(input("choisissez un nombre entre 1 et 10"))
for i in tableau_jeu:
    if (i==nombre):
        print("c'est gagné")
        break
    else:
        print("c'est perdu")
        break
tableau_jeu.sort()
print(tableau_jeu)

for i in tableau_jeu:
    if i != nombre
        break
