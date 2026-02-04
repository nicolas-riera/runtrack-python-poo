class Ville:
    def __init__(self, nom, nb_hab):
        self.__nom = nom
        self.__nb_hab = nb_hab

    def get_nb_hab(self):
        return self.__nb_hab
    
    def set_nb_hab(self, nb_hab):
        self.__nb_hab = nb_hab

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.set_nb_hab(self.__ville.get_nb_hab() + 1)

ville1 = Ville("Paris", 1000000)
print(ville1.get_nb_hab())

ville2 = Ville("Marseille", 861635)
print(ville2.get_nb_hab())

personne1 = Personne("John", 45, ville1)
personne1.ajouterPopulation()
personne2 = Personne("Myrtille", 4, ville1)
personne2.ajouterPopulation()
personne3 = Personne("Chloé", 18, ville2)
personne3.ajouterPopulation()

print(ville1.get_nb_hab())
print(ville2.get_nb_hab())