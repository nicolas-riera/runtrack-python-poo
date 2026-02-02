from math import *

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon

    def afficherInfos(self):
        print(f"Rayon = {self.rayon}")
        print(f"Circonférence = {self.circonference()}")
        print(f"Aire = {self.aire()}")
        print(f"Diamètre = {self.diametre()}")

    def circonference(self):
        return round(self.rayon*2*pi, 3)

    def aire(self):
        return round(self.rayon**2*pi, 3)
    
    def diametre(self):
        return self.rayon * 2
    
cercle1 = Cercle(4)
cercle1.afficherInfos()
print(cercle1.circonference())
print(cercle1.aire())
print(cercle1.diametre())

cercle2 = Cercle(7)
cercle2.afficherInfos()
print(cercle2.circonference())
print(cercle2.aire())
print(cercle2.diametre())