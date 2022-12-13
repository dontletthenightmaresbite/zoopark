class BaseAnimal:

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool, Sound : str, Happiness : int, Food : list, Foods : dict, isVegan : bool, Biome : str, Type : str):
        self.__gender = Gender
        self.__name = Name
        self.__age = Age
        self.__amountOfFood = AmountOfFood
        self.__area = 10
        self.__food = Food
        self.__foods = Foods
        self.__isVegan = isVegan
        self.__biome = Biome
        self.__foodAte = 0
        self.__type = Type
        self.__happiness = Happiness
        self.__sound = Sound
        self.__aviary = 0
    
    @property
    def aviary(self):
        return self.__aviary

    @aviary.setter
    def aviary(self, aviary):
        self.__aviary = aviary
    
    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    @property
    def isVegan(self):
        return self.__isVegan

    @property
    def type(self):
        return self.__type

    @property
    def food(self):
        return self.__food

    @property
    def foods(self):
        return self.__foods

    @property
    def biome(self):
        return self.__biome

    @property
    def happiness(self):
        return self.__happiness

    @happiness.setter
    def happiness(self, value):
        if value > 100:
            self.__happiness = 100
        elif value < 0:
            self.happiness = 0
        else:
            self.__happiness = value
    
    @property
    def isFeeded(self):
        return self.__foodAte >= self.__amountOfFood

    @property
    def amountOfFood(self):
        return self.__amountOfFood

    @property
    def foodAte(self):
        return self.__foodAte

    def eatFood(self, food, amount):
        if not amount: pass
        if not self.isFeeded:
            if food in self.__food:
                self.__foodAte += amount
                print(f"{self.__name} съел{(' ' if self.__gender else 'а ')} {round(amount, 2)} кг {self.__foods[food]}")
            else:
                print(self.__type.capitalize(), "это не ест")
        else:
            print(self.__name, "наел" + ("ся" if self.__gender else "ась"))

    def makeSound(self):
        print(self.__sound)

    def play(self):
        print(self.__name + " играет")
