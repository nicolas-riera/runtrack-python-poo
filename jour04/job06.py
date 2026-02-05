class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix}€")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")

    def demarrer(self):
        print("Attention, je roule en voiture")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")

    def demarrer(self):
        print("Attention, je roule en moto")

voiture1 = Voiture("Tesla", "Model Y", "2026", 47500)
voiture1.informationsVehicule()
moto1 = Moto("Yamaha", "jsp", "2022", 7300)
moto1.informationsVehicule()

voiture1.demarrer()
moto1.demarrer()