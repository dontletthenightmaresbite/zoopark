from alllibs import *

p = Penguin("PenPen", 7, 0.3)
e = Elephant("Матильда", 15, 5, 0)
t = Tiger("Симба", 4, 5)
w = Wolf("Вован", 2, 5)

for i in range(10):
    e.eatFood("листья", 10)
    print(e.isFeeded)
    # print(p.happiness)
    # p.happiness += 15