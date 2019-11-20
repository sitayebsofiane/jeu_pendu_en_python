#choice radom word
def mots():
    import random
    liste_mot=["bruno","thomas","kamel","farid","sofiane","fally","emira","nour"]
    return random.choice(liste_mot)
#fonction of play
def jouer():
    mot=mots()
    nbr_coup=0
    lettre=""
    affichage=["*" for i in range(len(mot))]
    i=0
    while nbr_coup < 8 and i<len(mot):
        lettre=input("entrez une lettre ")
        if(lettre==mot[i]):
            affichage[i]=lettre
            i+=1
            if(i!=len(mot)):
                print("".join(affichage)," bravo il vous reste ",8-nbr_coup,"coups")
        else:
            nbr_coup+=1
            print("".join(affichage),"attention il vous reste",8-nbr_coup,"coups")
    if(nbr_coup==8):
        print("vous avez perdu !")
    else:
        print("bravo vous avez gagnez ",8-nbr_coup,"points")


	   
	