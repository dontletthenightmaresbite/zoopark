from alllibs import *

def createAviary(zoo):
    clear()
    printBright(" Создание вольера ".center(30, "#"))
    aviaries = zoo.aviaries
    b = biomes()

    while True:
        name = input("Название: ")
        if name == "0": return

        if name in aviaries:
            print("\033[1A\033[J", end="")
        else:
            break

    ok = 0
    while True:
        enumBiomes()
        biome = input("Биом: ")
        if biome == "0": return

        try:
            biome = int(biome) - 1
            biome = b[biome]
            # print(f"Биом: {biome}")
            ok = True
        except:
            pass
        print("\033[3A\033[J", end="")
        if ok: 
            print(f"Биом: {biome}")
            break

    while True:
        area = input("Площадь: ")
        if area == "0": return

        try:
            area = int(area)
            if area > 0:
                break
        except:
            print("\033[1A\033[J", end="")
            pass

    zoo.createAviary(name, biome, area)
    printGreen(f'Вольер "{name}" создан!')
    input()

def deleteAviary(zoo):
    clear()
    print(" Снос вольера ".center(30, "#"))

    input()
    pass

def listAviaries(zoo):
    clear()
    printBright(" Список вольеров ".center(30, "#"))
    zoo.listAviaries()
    input()

def main(zoo):
    while True:
    #commands = {'1':createAviary(zoo), '2':listAviaries(zoo), '':''}
        printBright(name.center(30, " "))
        print("1. Создать вольер", "2. Список всех вольеров", "3. Снести вольер", sep = "\n")
        com = input()
        if com == "0": break
        elif com == "1": createAviary(zoo)
        elif com == "2": listAviaries(zoo)
        elif com == "3": deleteAviary(zoo)
        clear()

commands = {False:main}

clear()
name = input("Введите название зоопарка: ")
clear()

z = Zoo(name)
printGreen(f'Добро пожаловать в "{z.name}"!')
input('("Enter" для продолжения)')
clear()

main(z)
