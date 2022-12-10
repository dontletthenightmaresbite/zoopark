from alllibs import *

p = Penguin("PenPen", 7, 0.3)
e = Elephant("Матильда", 15, 5, 0)
t = Tiger("Симба", 4, 5)
w = Wolf("Вован", 2, 5)
p1 = Penguin("SecPen", 1, 10)
p2 = Penguin("ThPen", 2, 15)

v = Aviary("aaa", "Пустыня", 100)
b = Aviary("aaal", "Саванна", 100)

v.addAnimal(p)
v.addAnimal(p1)

b.addAnimal(e)
print()

v.feedAnimals("рыба", 5000)
v.feedAnimals("мясо", 5000)
print()

v.needFood()

v.foodRemain()
