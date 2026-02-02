class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (self.TVA / 100) + self.prixHT
    
    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Prix HT : {self.prixHT}")
        print(f"TVA : {self.TVA}")
        print(f"Prix TTC : {self.CalculerPrixTTC()}")

produit1 = Produit("Produit 1", 100, 20)
produit1.afficher()