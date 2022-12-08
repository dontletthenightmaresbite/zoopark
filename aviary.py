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

    def __eq__(self, other):
        return self.__name == other.name and self.__biome == other.biome and self.__area == other.area

    def addAnimal(self, Animal):
        if Animal.aviary:
            print(f'{Animal.name} уже в вольере "{Animal.aviary}"'); return

        if len(self.__animals)>0:
            if not (not Animal.isVegan and not self.__animals[0].isVegan and self.__animals[0].type == Animal.type) or (Animal.isVegan and self.__animals[0].isVegan):
                print(f'{Animal.name} не сочетается с другими животными в вольере {self.__name}');return 
        
        if not Animal.biome == self.__biome:
            print(f"Этот вольер не подходит для данного животного: {Animal.type}");return


        if not self.__areaFree >= Animal.area:
            print(f'Животному не хватает места =(');return

        self.__animals.append(Animal)
        Animal.aviary = self
        print(f'{Animal.name} теперь в вольере "{self.__name}"!')

    def removeAnimal(self, Animal):
        if not Animal.aviary == self:
            print(f'{Animal.name} не находится в вольере "{self.__name}"');return

        self.__animals.remove(Animal)
        Animal.aviary = 0
        print(f'{Animal.name} больше не в вольере "{self.__name}"')

    def makeSound(self):
        if len(self.__animals)==0: print(f'В вольере "{self.__name}" нет животных');return

        for animal in self.__animals:
            print(f"{animal.name} говорит: ", end = "")
            animal.makeSound()

    def feedAnimals(self, food, amount):
        foods = {}
        k = 0
        for animal in self.__animals:
            if amount<=0: break

            if food in animal.food:
                foods[food] = animal.foods[food]
                if animal.amountOfFood - animal.foodAte < amount:
                    value = animal.amountOfFood - animal.foodAte
                    amount -= value
                else:
                    value = amount; amount = 0
                animal.eatFood(food, value)
                k += 1

        if k: print(f'{k} животн{"ых" if k>1 else "ое"} в вольере "{self.__name}" покормлен{"ы" if k>1 else "о"}!' + 
        (f" Осталось {round(amount, 1)} кг {foods[food]}" if amount > 0 else f" {foods[food].capitalize()} не осталось"));return
        print(f'Ни одно животное в вольере "{self.__name}" это не ест({food})')