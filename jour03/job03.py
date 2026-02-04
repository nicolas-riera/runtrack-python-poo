class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.liste = []

    def ajouterTache(self, tache):
        self.liste.append(tache)

    def supprimerTache(self, tache):
        self.liste.pop(self.liste.index(tache))

    def marquerCommeFinie(self, tache):
        self.liste[self.liste.index(tache)].statut = "terminer"

    def afficherListe(self):
        print("Liste des tâches :\n")
        for tache in self.liste:
            print(f"- {tache.titre} : {tache.description} - {tache.statut}")

    def filterListe(self, statut):
        liste = []
        for tache in self.liste:
            if tache.statut == statut:
                liste.append(tache)
        return liste
    

liste = ListeDeTaches()
        
tache1 = Tache("Charger 3DS", "Mettre la 3DS sur son dock de charge")
tache2 = Tache("Récupérer Jeu Gratuit Epic", "Récupérer le jeu gratuit de la semaine sur Epic Games Store")
tache3 = Tache("Prendre Switch 2", "Prendre la Switch 2 et la mettre dans le sac")

liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

liste.supprimerTache(tache3)
liste.marquerCommeFinie(tache2)
liste.afficherListe()
liste.filterListe("à faire")
