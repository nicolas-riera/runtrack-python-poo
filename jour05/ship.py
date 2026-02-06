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

class Menu:
    def main_menu(self, ship):
        print("1. Remplacer Pièce")
        print("2. Modifier Matériau")
        print("3. Afficher état bâteau")
        print("4. Quitter")
        print(f"Bâteau choisi : {ship.name}")

        match input():
            case "1":
                return self.replace_part_menu(ship)
            case "2":
                return self.change_part_menu(ship)
            case "3":
                return self.display_state_menu(ship)
            case "4":
                return
            case _:
                return self.main_menu(ship)
            
    def replace_part_menu(self, ship):
        part_name = input("Entrez le nom de la pièce que vous voulez remplacer : ")
        new_part = Part(input("Entrez le nom de la nouvelle pièce : "), input("Entrez le matériau de la nouvelle pièce : "))
        ship.replace_part(part_name, new_part)
        return self.main_menu(ship)
    
    def change_part_menu(self, ship):
        part_name = input("Entrez le nom de la pièce : ")
        new_material = input("Entrez le nom du nouveau matériau : ")
        ship.change_part(part_name, new_material)
        return self.main_menu(ship)

    def display_state_menu(self, ship):
        ship.display_state()
        input("Appuyez sur Entrer pour continuer")
        return self.main_menu(ship)

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

s = Ship("Navire", dict)

# s.change_part("devant", "TestBois")
# s.replace_part("DdD", part2)

# s.display_state()

# s2 = RacingShip("Narive de course", dict, 180)
# s2.display_speed()

menu = Menu()
menu.main_menu(s)