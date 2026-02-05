class Forme:
    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def aire(self):
        return 3.14 * (self.radius**2)

cercle1 = Cercle(6)
print(cercle1.aire())