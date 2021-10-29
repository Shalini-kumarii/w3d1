from pet import Pet
class Ninja:
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name =last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print(self.first_name+" "+self.last_name+" playing with"+self.pet.name +" and his health is "+str(self.pet.health))
        return self

    def feed(self):
        self.pet.eat()
        print(self.first_name+" "+self.last_name+" feeding "+self.pet.name+" with "+self.pet_food)
        return self
    def bathe(self):
        self.pet.noise()
        print(self.pet.name+" you are cleaned!")
        return self
    
petobj =Pet("Rockey","Golden_retriver","Roll_over",89,100)
ninjaobj= Ninja("Shalini","Kumari",petobj,"lunch","meat")
ninjaobj.walk().feed().bathe()