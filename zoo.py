from alllibs import *

class Zoo:
    def __init__(self, Name):
        self.__name = Name
        self.__aviaries = {}
        self.__animals = {}
        self.__foods = {"трава":"травы", "листья":"листьев", "фрукты":"фруктов", "рыба":"рыбы", "мясо":"мяса"}
        # print(Fore.GREEN + f'Добро пожаловать в "{self.__name}"!' + Style.RESET_ALL + '\n("Enter" для продолжения)')

    @property
    def name(self):
        return self.__name

    @property
    def aviaries(self):
        return [x for x in self.__aviaries]

    def createAviary(self, Name : str, Biome : str, Area : int):
        aviary = Aviary(Name, Biome, Area)
        if Name in self.__aviaries:
            print("Вольер с таким именем уже существует!")
            del aviary
        else:
            self.__aviaries[Name] = aviary

    def deleteAviary(self, Name):
        if self.__aviaries.get(Name, 0):
            av : Aviary = self.__aviaries[Name]
            if av.area - av.areaFree == 0:
                del self.__aviaries[Name]
            else:
                print("Нельзя снести вольер!\nВ вольере находятся животные!")
        else:
            print("Такого вольера не существует!")
        pass

    def listAviaries(self):
        print(" Список вольеров ".center(30, "#"))
        if len(self.__aviaries) == 0:
            print("В зоопарке нет ни одного вольера");return

        for i, name in enumerate(self.__aviaries, 1):
            aviary = self.__aviaries[name]
            print(f'{i}. "{aviary.name}": {aviary.biome}, {aviary.areaClaimed}/{aviary.area}')

    def animalCreate(self, Av, Type, Name : str, Age : int, AmountOfFood : float|int, Gender : bool = 1, Happiness : int = 65):
        """Types:\n0: Penguin\n1: Elephant\n2: Tiger\n3: Wolf"""
        if not Av in self.__aviaries: print("Такого вольера не существует");return

        if not Name in self.__animals:
            if Type == 0: animal = Penguin(Name, Age, AmountOfFood, Gender, Happiness)
            elif Type == 1: animal = Elephant(Name, Age, AmountOfFood, Gender, Happiness)
            elif Type == 2: animal = Tiger(Name, Age, AmountOfFood, Gender, Happiness)
            elif Type == 3: animal = Wolf(Name, Age, AmountOfFood, Gender, Happiness)
            else: print("Такого животного не существует");return

            create = self.__aviaries[Av].addAnimal(animal)
            if create: self.__animals[Name] = animal
        else:
            print("Животное с таким именем уже существует")

    def animalDel(self, Av, Animal):
        pass

    def animalMove(self, Animal, From, To):
        if not From in self.__aviaries and To in self.__aviaries: print("Такого вольера не существует");return

        if not Animal in [x.name for x in From.animals]:
            print("Этого животного нет в вольере");return

        move = self.__aviaries[To].addAnimal(self.__animals[Animal])
        if move:
            self.__aviaries[From].removeAnimal(self.__animals[Animal])

    def foodNeed(self):
        print(" Нужно еды ".center(30, "#"))
        allFood = {"рыба":0, "трава":0, "листья":0, "фрукты":0, "мясо":0}
        for i in self.__aviaries:
            av = self.__aviaries[i]
            food = av.needFood()
            if sum(food.values()):
                print(f'"{i}": {", ".join([f"{food[x]} кг {self.__foods[x]}" for x in food if food[x] != 0])}.')
                for x in food:
                    allFood[x] += food[x]
        if sum([allFood[x] for x in allFood]):
            print("Чтобы покормить всех животных нужно: " + ", ".join([f"{allFood[x]} кг {self.__foods[x]}" for x in allFood if allFood[x] != 0]))
        else:
            print("Ни одно животное не голодно")
        

    def feedAnimal(self):
        pass

    def animalsInAviaries(self, aviary = False):
        print(" Животные в вольерах ".center(30, "#"))
        for i in self.__aviaries:
            av = self.__aviaries[i].listAnimals()
            if av:
                print(f'"{i}": {av}.')
