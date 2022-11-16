from animals.penguin import *
from animals.elephant import *
from animals.tiger import *
from animals.wolf import *

penguin = Penguin("PenPen", 7, 0.3)
elephant = Elephant("Матильда", 15, 5, 0)
tiger = Tiger("Симба", 4, 5)
wolf = Wolf("Вован", 2, 5)

for i in range(10):
    elephant.eatFood()