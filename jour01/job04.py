class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return self.nom, self.prenom
    

personne1 = Personne("Doe", "John")
print(f"Je suis {personne1.SePresenter()[1]} {personne1.SePresenter()[0]}")

personne2 = Personne("Dupond", "Jean")
print(f"Je suis {personne2.SePresenter()[1]} {personne2.SePresenter()[0]}")
