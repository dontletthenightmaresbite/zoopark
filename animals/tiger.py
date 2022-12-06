from animals.baseAnimal import *

class Tiger(BaseAnimal):

    def __init__(self, Name : str, Age : int, AmountOfFood, Gender : bool = True, Happiness : int = 65):
        super().__init__(Name, Age, AmountOfFood, Gender, "Ррррррррррр", Happiness, ["рыба", "мясо"], {"рыба":"рыбу", "мясо":"мясо"}, False, "Саванна", "тигр")
        