class Student:
    def __init__(self, lastname, firstname, num_student):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__num_student = num_student
        self.__num_credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__num_credits += credits
            self.__level = self.__studentEval()
        else:
            print("The value given isn't a positive value.")
        
    def get_credits(self):
        return self.__num_credits
    
    def get_name(self):
        return self.__lastname, self.__firstname
    
    def get_id(self):
        return self.__num_student
    
    def get_level(self):
        return self.__level
    
    def __studentEval(self):
        match self.get_credits():
            case credit if credit >= 90:
                return "Excellent"
            case credit if credit >= 80:
                return "Très bien"
            case credit if credit >= 70:
                return "Bien"
            case credit if credit >= 60:
                return "Passable"
            case _:
                return "Insuffisant"
            
    def studentinfo(self):
        print(f"Nom = {self.get_name()[0]}")
        print(f"Prénom = {self.get_name()[1]}")
        print(f"id = {self.get_id()}")
        print(f"Niveau = {self.get_level()}")

student145 = Student("Doe", "John", 145)
student145.add_credits(5)
student145.add_credits(38)
student145.add_credits(53)
print(f"Le nombre de crédits de {student145.get_name()[1]} {student145.get_name()[0]} est de {student145.get_credits()} points")

student145.studentinfo()