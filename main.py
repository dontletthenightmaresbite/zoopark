from zoo import *

z : Zoo = Zoo("aaa")

z.createAviary("asd", "Пустыня", 100)
z.createAviary("Sec", "Пустыня", 100)

z.listAviaries()

z.animalCreate("asd", 0, "Pen", 4, 10)

z.listAviaries()
z.animalsInAviaries()
z.foodNeed()
