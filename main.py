print("Jouons au pierre feuille ciseau ensemble:"/n)
print("Tapez 1 pour choisir la pierre")
print("Tapez 2 pour choisir la feuille")
print("Tapez 3 pour choisir le ciseau")

mychoice = input()

if (mychoice>=1 && mychoice<=3):
    compchoice = ['pierre', 'feuille', 'ciseau']
    def selectRandom(compchoice):
        return random.choice(compchoice)