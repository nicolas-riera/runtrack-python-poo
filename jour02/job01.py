class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    def set_longeur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur

rectangle1 = Rectangle(10, 5)
print(rectangle1.get_longueur())
print(rectangle1.get_largeur())

rectangle1.set_longeur(8)
rectangle1.set_largeur(4)
print(rectangle1.get_longueur())
print(rectangle1.get_largeur())