class Operation:

    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

test = Operation(2, 6)

print(f"Le nombre 1 est {test.nombre1}")
print(f"Le nombre 2 est {test.nombre2}")