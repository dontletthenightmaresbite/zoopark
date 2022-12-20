from animals.baseAnimal import *

class Wolf(BaseAnimal):

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool = True, Happiness : int = 65):
        super().__init__(Name, Age, AmountOfFood, 10, Gender, "Ауф", Happiness, ["мясо"], {"мясо":"мяса"}, False, "Пустыня", "волк")
        