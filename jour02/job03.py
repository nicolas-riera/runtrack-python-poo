class Livre:
    def __init__(self, titre, auteur, nb_pages, disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = disponible

    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_nb_pages(self):
        return self.__nb_pages
    def verification(self):
        return self.__disponible
    
    def set_titre(self, new_value):
        self.__titre = new_value
    def set_auteur(self, new_value):
        self.__auteur = new_value
    def set_nb_pages(self, new_value):
        if new_value > 0:
            self.__nb_pages = new_value
        else:
            print("Le nombre de pages doit être positif...")
    def emprunter(self):
        if self.verification():
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible...")
    def rendre(self):
        if not self.verification():
            self.__disponible = True
        else:
            print("Le libre n'a pas été emprunté")
    