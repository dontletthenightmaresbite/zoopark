from animals.baseAnimal import *

class Penguin(BaseAnimal):

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool = True, Happiness : int = 65):
        super().__init__(Name, Age, AmountOfFood, 5, Gender, "Pen Pen", Happiness, ["рыба"], {"рыба":"рыбы"}, False, "Пустыня", "пингвин")
        
    