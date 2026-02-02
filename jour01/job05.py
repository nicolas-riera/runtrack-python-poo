class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"x : {self.x}, y : {self.y}")

    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y