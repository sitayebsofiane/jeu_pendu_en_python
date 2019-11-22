class Player:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def add_score(self,new_score):
        self.score+=new_score;
        return self.score
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
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
    choix=random.choice(liste_mot)
    return choix
#fonction to check enter must be letter a to z
def letrre_choise():
    import re
    lettre=input("entrez une lettre ").lower()
    while not bool(re.match(r"^[a-z]$",lettre)):
         lettre=input("entrez une lettre ").lower()
    return lettre

#fonction of play
def part():
    #genrate random word to ze liste word and transform it in liste of lettre
    mot=[x for x in mots()[0:]]
    affichage=["*" for i in range(len(mot))]
    tours=0
    find=False
    while tours<8 and affichage !=mot:
        lettre=letrre_choise()
        for i in range(len(mot)):
            if lettre==mot[i] and affichage[i]=="*":
                affichage[i]=lettre
                print("".join(affichage)," bravo il vous reste ",8-tours,"coups")
                find=True
                break
        if not find:
            tours+=1
            print("".join(affichage),"attention il vous reste",8-tours,"coups")
        find=False
    if tours==8 and affichage !=mot:
        print("vous avez perdu !")
    else:
        print("bravo vous avez gagnez ",8-tours,"points")
    return 8-tours
# i call fonction to part in play
def play():
    import pickle
    nom=name()
    print("bienvenu",nom)
    add=True
    with open("data","rb") as fic:
        record=pickle.Unpickler(fic)
        player=record.load()
        if player.getName()==nom:
            score=player.getScore()
            add=False           
    if add:
        score=0
    else:
        score+=player.getScore()
    while input("taper oui si vous voulez jouer ").lower()=="oui":
        score+=part()
        print("votre score est ",score)
    if add:
        player=Player(nom,score)
        with open("data","wb") as fic:
            record=pickle.Pickler(fic)
            record.dump(player)




	   
	