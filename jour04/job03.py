class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, new_value):
        self.__longueur = new_value
    def set_largeur(self, new_value):
        self.__largeur = new_value

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur
    
rectangle1 = Rectangle(14, 5)
print(rectangle1.perimetre())
print(rectangle1.surface())
print(rectangle1.get_largeur())

parallepipede1 = Parallelepipede(28, 13, 12)
print(parallepipede1.volume())