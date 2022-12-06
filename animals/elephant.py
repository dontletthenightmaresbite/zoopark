from animals.baseAnimal import *

class Elephant(BaseAnimal):

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool = True, Happiness : int = 65):
        super().__init__(Name, Age, AmountOfFood, Gender, "*Звуки слонов*", Happiness, ["трава", "листья", "фрукты"], {"трава":"траву", "листья":"листья", "фрукты":"фрукты"}, False, "Саванна", "слон")
        