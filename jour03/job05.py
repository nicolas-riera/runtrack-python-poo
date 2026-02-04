import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.vie -= 1

class Jeu:
    def __init__(self):
        pass

    def choisirNiveau(self):
        self.niveau = input("Choissiez un niveau :\n\n1. Facile\n2. Normale\n3. Difficile\n")

    def lancerJeu(self):
        match self.niveau:
            case "2":
                self.joueur = Personnage("Joueur", 6)
                self.ennemi = Personnage("Ennemi", 6)
            case "3":
                self.joueur = Personnage("Joueur", 5)
                self.ennemi = Personnage("Ennemi", 8)
            case _:
                self.joueur = Personnage("Joueur", 8)
                self.ennemi = Personnage("Ennemi", 5)

    def verifierVie(self):
        if self.joueur.vie == 0:
            print("Perdu")
            return False
        elif self.ennemi.vie ==0:
            print("Gagné")
            return False
        return True
    
    def afficherVie(self):
        print(f"Joueur : {self.joueur.vie} - Ennemi : {self.ennemi.vie}")

    def joueur_jouer(self):
        choix = input("Que voulez-vous faire :\n\n1. Attaquer\n2. Rien faire\n")
        match choix:
            case "1":
                self.joueur.attaquer(self.ennemi)
            case _:
                pass

    def ennemi_jouer(self):
        match random.randint(1,2):
            case 1:
                self.ennemi.attaquer(self.joueur)
                print("L'ennemi attaque")
            case _:
                print("L'ennemi ne fait rien")



jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()

while jeu.verifierVie():

    jeu.afficherVie()
    jeu.joueur_jouer()
    jeu.ennemi_jouer()
        