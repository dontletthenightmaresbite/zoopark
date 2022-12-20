class Aviary:
    def __init__(self, Name : str, Biome : str, Area : int):
        self.__name = Name
        self.__biome = Biome
        self.__area = Area
        self.__animals = []
        self.__areaFree = Area
        self.__food = {"рыба":0, "трава":0, "листья":0, "фрукты":0, "мясо":0}
        self.__foods = {"трава":"травы", "листья":"листьев", "фрукты":"фруктов", "рыба":"рыбы", "мясо":"мяса"}

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
        return self.__animals

    @property
    def areaClaimed(self):
        return self.__area - self.__areaFree

    @property
    def areaFree(self):
        return self.__areaFree

    @property
    def food(self):
        return self.__food

    def __eq__(self, other):
        return self.__name == other.name and self.__biome == other.biome and self.__area == other.area

    def addAnimal(self, Animal):
        if Animal.aviary:
            print(f'{Animal.name} уже в вольере "{Animal.aviary.name}"');return

        if len(self.__animals)>0:
            if not ((not Animal.isVegan) and (not self.__animals[0].isVegan) and self.__animals[0].type == Animal.type) or (Animal.isVegan and self.__animals[0].isVegan):
                print(f'{Animal.name} не сочетается с другими животными в вольере {self.__name}');return 
        
        if not Animal.biome == self.__biome:
            print(f"Этот вольер не подходит для данного животного: {Animal.type}");return


        if not self.__areaFree >= Animal.area:
            print(f'Животному не хватает места =(');return

        self.__animals.append(Animal)
        self.__areaFree -= Animal.area
        Animal.aviary = self
        print(f'{Animal.name} теперь в вольере "{self.__name}"!')
        return True

    def removeAnimal(self, Animal):
        if not Animal.aviary == self:
            print(f'{Animal.name} не находится в вольере "{self.__name}"');return

        self.__animals.remove(Animal)
        Animal.aviary = 0
        self.__areaFree += Animal.area
        print(f'{Animal.name} больше не в вольере "{self.__name}"')

    def makeSound(self):
        if len(self.__animals)==0: print(f'В вольере "{self.__name}" нет животных');return

        for animal in self.__animals:
            print(f"{animal.name} говорит: ", end = "")
            animal.makeSound()

    def feedAnimals(self, food, amount):
        if not food in self.__food: return
        amount += self.__food[food]
        k = 0
        for animal in self.__animals:
            if amount <= 0: break

            if food in animal.food and (not animal.isFeeded):
                if animal.amountOfFood - animal.foodAte < amount:
                    value = animal.amountOfFood - animal.foodAte
                    amount -= value
                else:
                    value = amount; amount = 0
                
                animal.eatFood(food, value)
                k += 1
        self.__food[food] = amount

        if k: print(f'{k} животн{"ых" if k>1 else "ое"} в вольере "{self.__name}" покормлен{"ы" if k>1 else "о"}!' + 
        (f" Осталось {round(amount, 1)} кг {self.__foods[food]}" if amount > 0 else f" {self.__foods[food].capitalize()} не осталось"));return

        print(f'Ни одно животное в вольере "{self.__name}" это не ест ({food})')
        self.__food[food] = amount

    def listAnimals(self):
        return ", ".join([f"{x.name}({x.type})" for x in self.__animals])

    def BeautyneedFood(self):
        if len(self.__animals) == 0: print(f'В вольере "{self.__name}" нет ни одного животного');return

        for animal in self.__animals:
            if not animal.isFeeded:
                amount = animal.amountOfFood - animal.foodAte
                print(f"{animal.name} хочет ещё {round(amount, 2)} кг {', '.join(self.__foods[x] for x in animal.food[:-1]) + (' или ' if len(animal.food)-1 else '') + self.__foods[animal.food[-1]] }")

    def needFood(self):
        food = dict.fromkeys(self.__food.keys(), 0)
        for i in self.__animals:
            food[i.food[0]] += i.needFood
        return food

    def foodRemain(self):
        if sum(self.__food.values()) == 0: print("Еды не осталось!");return
        print(f'В вольере "{self.__name}" осталось ' + ", ".join( [f"{round(self.__food[x])} кг {self.__foods[x]}" for x in self.__foods if self.__food[x] != 0] ))
