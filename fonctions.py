#fonction to check name
def name():
    name=input("entré votre nom ")
    while len(name)==0:
        name=input("entré votre nom ")
    return name
#choice radom word
def mots():
    import random
    liste_mot=["bruno","thomas","kamel","farid","sofiane","fally","emira","nour"]
    return random.choice(liste_mot)
#fonction to check enter must be letter a to z
def check_enter(lettre):
    import re
    return  bool(re.match(r"^[a-z]$",lettre))

#fonction of play
def part():
    #genrate random word to ze liste
    mot=mots()
    nbr_coup=0
    lettre=""
    affichage=["*" for i in range(len(mot))]
    index=0
    while nbr_coup < 8 and index<len(mot):
        lettre=input("entrez une lettre ")
        #i check his enter if its letter
        if check_enter(lettre):
            if(lettre==mot[index]):
                affichage[index]=lettre
                index+=1
                if(index!=len(mot)):
                    print("".join(affichage)," bravo il vous reste ",8-nbr_coup,"coups")
            else:
                nbr_coup+=1
                if 8-nbr_coup>0:
                    print("".join(affichage),"attention il vous reste",8-nbr_coup,"coups")
    if(nbr_coup==8):
        print("vous avez perdu !")
    else:
        print("bravo vous avez gagnez ",8-nbr_coup,"points")
    return 8-nbr_coup
# i call fonction to part in play
def play():
    nom=name()
    print("bienvenu",nom)
    score=0
    while input("taper oui si vous voulez jouer ").lower()=="oui":
        score+=part()
        print("votre score est ",score)




	   
	