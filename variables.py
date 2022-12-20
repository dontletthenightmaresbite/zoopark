from os import system
from colorama import *

biom = ["Саванна", "Пустыня"]

def clear():
    system('cls')

def printRed(s):
    print(Fore.RED + s + Style.RESET_ALL)

def printGreen(s):
    print(Fore.GREEN + s + Style.RESET_ALL)

def printBright(s):
    print(Style.BRIGHT + s + Style.RESET_ALL)

def biomes():
    return biom

def enumBiomes():
    for i, b in enumerate(biom, 1):
        print(f"{i}. {b}")
# init()
