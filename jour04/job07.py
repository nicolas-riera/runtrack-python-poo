import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def points(self):
        if self.valeur in ["Valet", "Dame", "Roi"]:
            return 10
        elif self.valeur == "As":
            return 11  
        else:
            return int(self.valeur)

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = []
        self.main_joueur = []
        self.main_croupier = []
        self.creer_paquet()
        self.melanger()

    def creer_paquet(self):
        couleurs = ["Cœur", "Carreau", "Trèfle", "Pique"]
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "Valet", "Dame", "Roi", "As"]

        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

    def calculer_score(self, main):
        score = 0
        nb_as = 0

        for carte in main:
            score += carte.points()
            if carte.valeur == "As":
                nb_as += 1

        while score > 21 and nb_as > 0:
            score -= 10
            nb_as -= 1

        return score

    def distribuer(self):
        for i in range(2):
            self.main_joueur.append(self.tirer_carte())
            self.main_croupier.append(self.tirer_carte())

    def afficher_main(self, main, nom):
        print(f"\nMain de {nom} :")
        for carte in main:
            print(" -", carte)
        print("Score :", self.calculer_score(main))

    def tour_joueur(self):
        while True:
            self.afficher_main(self.main_joueur, "Joueur")
            if self.calculer_score(self.main_joueur) > 21:
                print("Vous dépassez 21, vous avez perdu !")
                return False

            choix = input("Prendre une carte (p) ou passer (s) ? ").lower()
            if choix == "p":
                self.main_joueur.append(self.tirer_carte())
            elif choix == "s":
                return True

    def tour_croupier(self):
        while self.calculer_score(self.main_croupier) < 17:
            self.main_croupier.append(self.tirer_carte())

    def determiner_gagnant(self):
        score_joueur = self.calculer_score(self.main_joueur)
        score_croupier = self.calculer_score(self.main_croupier)

        self.afficher_main(self.main_croupier, "Croupier")

        if score_croupier > 21 or score_joueur > score_croupier:
            print("Le joueur a gagné !")
        else:
            print("Le croupier a gagné...")

    def jouer(self):
        print("=== BLACKJACK ===")
        self.distribuer()

        if self.tour_joueur():
            self.tour_croupier()
            self.determiner_gagnant()

jeu = Jeu()
jeu.jouer()
