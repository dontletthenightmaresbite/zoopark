from random import randint

class Tiger:

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool = True, Happiness : int = 65):
        self.__gender = Gender
        self.__name = Name
        self.__age = Age
        self.__amountOfFood = AmountOfFood
        self.__area = 10
        self.__food = ["рыба", "мясо"]
        self.__foods = {"рыба":"рыбу", "мясо":"мясо"}
        self.__isVegan = False
        self.__biome = "Саванна"
        self.__foodAte = 0
        self.__type = "тигр"
        self.__happiness = Happiness

    @property
    def Age(self):
        return self.__age

    @property
    def Name(self):
        return self.__name

    @property
    def Type(self):
        return self.__type

    @property
    def Food(self):
        return self.__food

    @property
    def Biome(self):
        return self.__biome

    @property
    def Happiness(self):
        return self.__happiness

    @Happiness.setter
    def Happiness(self, value):
        if value > 100:
            self.__happiness = 100
        elif value < 0:
            self.happiness = 0
        else:
            self.__happiness = value

    @property
    def isFeeded(self):
        return self.__foodAte >= self.__amountOfFood

    def eatFood(self, food, amount):
        if not self.isFeeded:
            if food in self.__food:
                self.__foodAte += amount
                print(self.__name + " съел" + (" " if self.__gender else "а ") + self.__foods[food])
            else:
                print(self.__type.capitalize(), "это не ест")
        else:
            print(self.__name, "наел" + ("ся" if self.__gender else "ась"))

    def makeSound(self):
        print("Ррррррррррр")

    def play(self):
        print(self.name + " играет")