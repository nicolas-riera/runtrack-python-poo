class Commande:
    def __init__(self, nb_commande, liste_plats_commandes, status_commande):
        self.__nb_commande = nb_commande
        self.__liste_plats_commandes = liste_plats_commandes
        self.__status_commande = status_commande

    def ajouter_plat(self, plat, prix):
        self.__liste_plats_commandes[plat] = (prix, "en cours")

    def annuler_commande(self):
        self.__status_commande = 'annulée'

    def __calculer_total_commande(self):
        total = 0
        for values in self.__liste_plats_commandes.values():
            total += values[0]
        return total
    
    def calculer_TVA(self, TVA=20):
        return self.__calculer_total_commande() * (TVA/100)
    
    def total(self):
        print(self.__calculer_total_commande() + self.calculer_TVA())

commande1 = Commande(1, {"Steak" : (13, "en cours"), "Frites" : (6, "en cours")}, "en_cours")
commande1.ajouter_plat("Salade", 3)
commande1.total()
commande1.annuler_commande()