from random import randint

class Wolf:
    area = 10
    food = ["мяса"]
    isVegan = False
    biome = "Пустыня"

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool = True):
        self.gender = Gender
        self.name = Name
        self.age = Age
        self.amountOfFood = AmountOfFood
    
    def makeSound(self):
        print("Ауф")

    def eatFood(self):
        print(self.name + " съел" + (" " if self.gender else "а ") + str(self.amountOfFood) + " кг " + self.food[randint(0,len(self.food))-1])

    def play(self):
        print(self.name + " играет")