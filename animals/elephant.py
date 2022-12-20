from animals.baseAnimal import *

class Elephant(BaseAnimal):

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool = True, Happiness : int = 65):
        super().__init__(Name, Age, AmountOfFood, 20, Gender, "*Звуки слонов*", Happiness, ["трава", "листья", "фрукты"], {"трава":"травы", "листья":"листьев", "фрукты":"фруктов"}, False, "Саванна", "слон")
        