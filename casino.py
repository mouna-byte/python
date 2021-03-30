aleatoire=randrange(50)
print(aleatoire)

nombre= int(input("choisissez un chiffre entre 0 et 49"))

mise= int(input("combien misez vous?"))

while nombre != aleatoire:
    nombre = int(input("choisissez un chiffre entre 0 et 49"))
    if (nombre %2== 0 and aleatoire %2 == 0):
        print("c'est bien un nombre pair!, mais vous avez perdu la moitié de votre mise")
        mise= mise/2
        print("il vous reste", mise, "€")
    elif (nombre%2 !=0 and aleatoire%2!=0):
        print("c'est bien un nombre impair!, mais vous avez perdu la moitié de votre mise")
        mise = mise / 2
        print("il vous reste", mise, "€")
    else:
        print("vous avez perdu votre mise!")
        mise=0
