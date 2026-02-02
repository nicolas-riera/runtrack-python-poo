class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom


chat = Animal(prenom="Diego")
print(f"L'age de l'animal est de {chat.age} ans")
chat.vieillir()
print(f"L'age de l'animal est de {chat.age} ans")
chat.nommer("Luna")
print(f"L'animal se nomme {chat.prenom}")
