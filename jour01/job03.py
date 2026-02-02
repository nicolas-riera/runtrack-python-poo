class Operation:

    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        print(f"L'addition de nombre 1 et de nombre 2 est de {self.nombre1 + self.nombre2}")

test = Operation(2, 6)

print(f"Le nombre 1 est {test.nombre1}")
print(f"Le nombre 2 est {test.nombre2}")

test.addition()