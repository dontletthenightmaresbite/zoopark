class Aviary:
    def __init__(self, Name : str, Biome : str, Area : int):
        self.__name = Name
        self.__biome = Biome
        self.__area = Area
        self.__animals = []
        self.__areaFree = Area

    @property
    def name(self):
        return self.__name

    @property
    def biome(self):
        return self.__biome

    @property
    def area(self):
        return self.__area

    @property
    def animals(self):
        return ", ".join(self.__animals)

    @property
    def areaClaimed(self):
        return self.__area - self.__areaFree

    def AddAnimal(self, Animal):

        if not Animal.aviary:
            if Animal.biome == self.__biome:
                if self.__areaFree >= Animal.area:
                    self.__animals.append(Animal)
                    Animal.aviary = self.__name
                    print(f'{Animal.name} теперь в вольере "{self.__name}"!')
                else:
                    print(f'Животному не хватает места =(')
            else:
                print(f"Этот вольер не подходит для данного животного: {Animal.type}")
        else:
            print(f'{Animal.name} уже в вольере "{Animal.aviary}"')

    def RemoveAnimal(self):
        pass
