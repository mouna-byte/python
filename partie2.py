def searchC(mot, chaine):
    trouve=chaine.find(mot)
    print(trouve)

    #faux= False

    if (trouve == -1):
        print (False)
    else :
        print (True)
        print (trouve)


#####exo 1 version 2

def chercheC (mot, chaine):
    trouve= chaine.count(mot)
    print(trouve)

    if trouve>0:
        print (True)
    else:
        print (False)


#####exo 2
phrase= "la v13 3st un myst3r3 qu'1l faut r3soudr3, 3t non un probl3m3 a r3soudr3. Ghand1  "

new=(phrase.replace("3", "e"))
print (new)
new2=new.replace("1", "i")
print (new2)
