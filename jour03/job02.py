class CompteBancaire:
    def __init__(self, nb_compte, nom, prenom, solde, decouvert):
        self.__nb_compte = nb_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__nb_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde}")
        if self.__decouvert:
            decouvert = "Oui"
        else:
            decouvert = "Non"
        print(f"Découvert autorisé : {decouvert}")

    def afficherSolde(self):
        print(f"Solde : {self.__solde}")

    def versement(self, versement):
        self.__solde += versement

    def retrait(self, retrait):
        if self.__solde >= retrait or self.__decouvert:
            self.__solde -= retrait
        else:
            print("Vous n'avez pas le solde nécessaire pour effectuer ce retrait...")

    def agios(self):
        if self.__solde < 0:
            self.__solde -= (self.__solde * -0.1)

    def virement(self, destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            destinataire.__solde += montant
            print(f"Le virement de {montant}€ a été effectué !")
        else:
            print("Vous n'avez pas le solde nécessaire pour effectuer ce virement...")

compte1 = CompteBancaire(1, "Riera", "Nicolas", 500, True)
compte1.afficher()
compte1.versement(30)
compte1.afficherSolde()
compte1.retrait(600)
compte1.afficherSolde()
compte1.agios()
compte1.afficherSolde()
compte1.versement(200)

compte2 = CompteBancaire(1, "Dupond", "Jean", -70, True)
compte1.virement(compte2, 70)
compte2.afficherSolde()
