from animals.baseAnimal import *

class Tiger(BaseAnimal):

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool = True, Happiness : int = 65):
        super().__init__(Name, Age, AmountOfFood, 15, Gender, "Ррррррррррр", Happiness, ["рыба", "мясо"], {"рыба":"рыбы", "мясо":"мяса"}, False, "Саванна", "тигр")
        