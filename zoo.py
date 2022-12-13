from alllibs import *

class Zoo:
    def __init__(self, Name):
        self.__name = Name
        self.__aviaries = {}
        self.__animals = []
        print(f'Добро пожаловать в "{self.__name}"')

    @property
    def name(self):
        return self.__name

    @property
    def aviaries(self):
        print(", ".join([x for x in self.__aviaries]))

    def createAviary(self, Name : str, Biome : str, Area : int):
        aviary = Aviary(Name, Biome, Area)
        if Name in self.__aviaries:
            print("Вольер с таким именем уже существует!")
            del(aviary)
        else:
            self.__aviaries[Name] = aviary

    def deleteAviary(self, Name):
        pass

    def createAnimal(self, Type, Name, Age, AmountOfFood, ):

    def animalMove(self):
        pass
