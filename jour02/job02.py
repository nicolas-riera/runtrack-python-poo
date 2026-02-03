class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_titre(self, new_value):
        self.__titre = new_value
    def set_auteur(self, new_value):
        self.__auteur = new_value
    def set_nb_pages(self, new_value):
        if new_value > 0:
            self.__nb_pages = new_value
        else:
            print("Le nombre de pages doit être positif...")

