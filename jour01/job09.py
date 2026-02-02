class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (self.TVA / 100) + self.prixHT
    
    def afficher(self):
        return [self.nom, self.prixHT, self.TVA, self.CalculerPrixTTC()]
    
    def changerNom(self, nom):
        self.nom = nom

    def changerPrixHT(self, prixHT):
        self.prixHT = prixHT
    
    def afficherNom(self):
        return self.nom
    
    def afficherPrixHT(self):
        return self.prixHT
    
    def afficherTVA(self):
        return self.TVA

produit1 = Produit("Produit 1", 100, 20)
print(produit1.CalculerPrixTTC())
print(f"Nom : {produit1.afficher()[0]}, Prix HT : {produit1.afficher()[1]}, TVA : {produit1.afficher()[2]}, Prix TTC {produit1.afficher()[3]}")
produit1.changerNom("Produit 11")
produit1.changerPrixHT(250)
print(f"Nom : {produit1.afficher()[0]}, Prix HT : {produit1.afficher()[1]}, TVA : {produit1.afficher()[2]}, Prix TTC {produit1.afficher()[3]}")

produit2 = Produit("Produit 2", 38, 15)
print(produit2.CalculerPrixTTC())
print(f"Nom : {produit2.afficher()[0]}, Prix HT : {produit2.afficher()[1]}, TVA : {produit2.afficher()[2]}, Prix TTC {produit2.afficher()[3]}")
produit2.changerNom("Produit 22")
produit2.changerPrixHT(12)
print(f"Nom : {produit2.afficher()[0]}, Prix HT : {produit2.afficher()[1]}, TVA : {produit2.afficher()[2]}, Prix TTC {produit2.afficher()[3]}")
