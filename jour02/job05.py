class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__reservoir = 50
        self.en_marche = False

    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_annee(self):
        return self.__annee
    def get_kilometrage(self):
        return self.__kilometrage
    def __verifier_plein(self):
        return self.__reservoir
    
    def set_marque(self, new_value):
        self.__marque = new_value
    def set_modele(self, new_value):
        self.__modele = new_value
    def set_annee(self, new_value):
        self.__annee = new_value
    def set_kilometrage(self, new_value):
        self.__kilometrage = new_value

    def demarrer(self):
        if not self.en_marche:
            if self.__verifier_plein() > 5:
                self.en_marche = True
            else:
                print("Le réservoir est vide...")
        else:
            print("La voiture est déjà en marche...")
    def arreter(self):
        if self.en_marche:
            self.en_marche = False
        else:
            print("La voiture est déjà à l'arrêt...")    

    