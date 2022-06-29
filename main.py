from tkinter import *
# tkinder interface
fenetre = Tk()
label = Label(fenetre)
label.pack()
fenetre.mainloop()

print("Jouons au pierre feuille ciseau ensemble:")
print("Tapez 1 pour choisir la pierre")
print("Tapez 2 pour choisir la feuille")
print("Tapez 3 pour choisir le ciseau")

mychoice = input()
int_nbr = int(mychoice)

if (int_nbr>=1 and int_nbr<=3):
    import random
    compchoice = ['pierre', 'feuille', 'ciseau']
    def selectRandom(compchoice):
        return random.choice(compchoice)
    toto = selectRandom(compchoice)
    print("Le choix de l'ordinateur est: ", toto)
    # condition pour int = 1 soit: choix du joueur = pierre
    if (int_nbr == 1 and toto == "pierre"):
        print("Match nul")
    elif (int_nbr == 1 and  toto == "feuille"):
        print("l'ordinateur a gagné")
    elif (int_nbr == 1 and toto == "ciseau"):
        print("vous avez gagné")

    # condition pour int = 1 soit: choix du joueur = pierre
    elif (int_nbr == 2 and toto == "pierre"):
        print("vous avez gagné")
    elif (int_nbr == 2 and toto == "feuille"):
        print("Match nul")
    elif (int_nbr == 2 and toto == "ciseau"):
        print("l'ordinateur a gagné")

    # condition pour int = 1 soit: choix du joueur = pierre
    elif (int_nbr == 3 and toto == "pierre"):
        print("l'ordinateur a gagné")
    elif (int_nbr == 3 and toto == "feuille"):
        print("vous avez gagné")
    elif (int_nbr == 3 and toto == "ciseau"):
        print("Match nul")

    else:
        print("probleme")