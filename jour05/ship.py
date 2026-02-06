class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"{self.name} est constitué de {self.material}"
    
class Ship:
    def __init__(self, name, parts):
        self.name = name
        self.__parts = parts

    def display_state(self):
        for part in self.__parts.values():
            print(part.name)

    def replace_part(self, part_name, new_part):
        self.__parts[part_name] = new_part

    def change_part(self, part_name, new_material):
        self.__parts[part_name].change_material(new_material)

class RacingShip(Ship):
    def __init__(self, name, parts, max_speed):
        super().__init__(name, parts)
        self.max_speed = max_speed
    
    def display_speed(self):
        print(f"La vitesse maximun est de {self.max_speed}")

# Example test

part1 = Part("devant", "Bois")
part2 = Part("deriere", "Fer")
part3 = Part("bas", "plastique")
part4 = Part("DdD", "Metal")
part5 = Part("DxD", "Bois")

dict = {
    part1.name: part1,
    part2.name: part2,
    part3.name: part3,
    part4.name: part4,
    part5.name: part5,
}

s=Ship("Navire", dict)

s.change_part("devant", "TestBois")
s.replace_part("DdD", part2)

s.display_state()

s2 = RacingShip("Narive de course", dict, 180)
s2.display_speed()