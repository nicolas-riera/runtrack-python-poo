class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans.")

class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        Personne.__init__(self, age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

personne1 = Personne()
eleve1 = Eleve()
eleve1.allerEnCours()
eleve1.modifierAge(15)
professeur1 = Professeur(40, "Maths")
professeur1.afficherAge()
professeur1.enseigner()