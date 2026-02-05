class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        super().__init__()
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

rectangle1 = Rectangle(14, 8)
print(rectangle1.aire())