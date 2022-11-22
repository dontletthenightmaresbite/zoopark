from random import randint

class Penguin:
    area = 10
    food = ["рыбы"]
    isVegan = False
    biome = "Пустыня"

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool = True):
        self.gender = Gender
        self.name = Name
        self.age = Age
        self.amountOfFood = AmountOfFood
    
    def makeSound(self):
        print("Pen Pen")

    def eatFood(self):
        print(self.name + " съел" + (" " if self.gender else "а ") + str(self.amountOfFood) + " кг " + self.food[randint(0,len(self.food))-1])

    def play(self):
        print(self.name + " играет")
    """
    @property
    def isFeeded(self):
        return self.__foodAte >= self.__amountOfFood

    def eatFood(self, food, amount):
        if not self.isFeeded:
            if food in self.__food:
                self.__foodAte += amount
                print(self.__name + " съел" + (" " if self.__gender else "а ") + self.__foods[food])
            else:
                print(self.__vid, "это не ест")
        else:
            print(self.__name, "наел" + ("ся" if self.__gender else "ась"))
        #print(self.__name + " съел" + (" " if self.gender else "а ") + str(self.amountOfFood) + " кг " + self.food[randint(0,len(self.food))-1])"""
