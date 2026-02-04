class Joueur:
    def __init__(self, nom, numero, position, nb_buts=0, passes_decisives=0, carton_jaune=0, carton_rouge=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_buts = nb_buts
        self.passes_decisives = passes_decisives
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge

    def marquerUnBut(self):
        self.nb_buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.carton_jaune += 1

    def recevoirUnCartonRouge(self):
        self.carton_rouge += 1

    def afficherStatistiques(self):
        print(f"Nom : {self.nom}")
        print(f"Numéro : {self.numero}")
        print(f"Position : {self.position}")
        print(f"Nombre de buts marqués, : {self.nb_buts}")
        print(f"Passes décisives effectuées : {self.passes_decisives}")
        print(f"Cartons jaunes reçus : {self.carton_jaune}")
        print(f"Cartons rouges reçus : {self.carton_rouge}")

class Equipe:
    def __init__(self, nom, liste_joueurs=[]):
        self.nom = nom
        self.liste_joueurs = liste_joueurs

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()
            print("")
    
    def mettreAJourStatistiquesJoueur(self, joueur, marquerbut=False, passe_decisive=False, carton_jaune=False, carton_rouge=False):
        if marquerbut:
            joueur.marquerUnBut()
        if passe_decisive:
            joueur.effectuerUnePasseDecisive()
        if carton_jaune:
            joueur.recevoirUnCartonJaune()
        if carton_rouge:
            joueur.recevoirUnCartonRouge()


joueur1 = Joueur("Nicolas", 69, "Avant")
joueur2 = Joueur("Jean", 8, "Millieu")
joueur3 = Joueur("Paul", 33, "Arrière")
joueur4 = Joueur("Guillaume", 12, "Arrière")

joueur5 = Joueur("Pascal", 53, "Avant")
joueur6 = Joueur("Laurent", 14, "Millieu")
joueur7 = Joueur("Gérard", 25, "Arrière")
joueur8 = Joueur("John", 96, "Arrière")

equipe1 = Equipe("Bleu")
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)

equipe2 = Equipe("Rouge") 
equipe2.ajouterJoueur(joueur5)
equipe2.ajouterJoueur(joueur6)
equipe2.ajouterJoueur(joueur7)
equipe2.ajouterJoueur(joueur8)

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur(joueur2, marquerbut=True)
equipe1.mettreAJourStatistiquesJoueur(joueur4, passe_decisive=True)
equipe2.mettreAJourStatistiquesJoueur(joueur7, carton_jaune=True)

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()