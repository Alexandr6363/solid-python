"""
    В данном примере принцп нарушается
    Потому что в классе 'Animal' в методе 'eat' принимается только 'self',
    а в классе 'Cat' появился 'amount'.
    В классе Dog параметр 'amount' отсутсвует
    Отсутствует общий интерфейс, чтобы задавать атрибуты животным ( Имя | Возраст )
    =================================================
    Поэтому мы не можем заменить Класс родтеля на класс потомка

"""


class Animal:
    def __init__(self, attrs):
        self.attributes = attrs

    def eat(self):
        print("Ate some food!")


class Cat(Animal):
    def eat(self, amount=0.1):
        if amount > 0.3:
            print("Can't eat that much!")
        else:
            print("Ate some cat food!")


class Dog(Animal):
    def eat(self):
        print("Ate some dog food!")


# атрибуты задаются неоднородно ( собакам в виде словаря , а для кошки в виде кортежа)
pluto = Dog({'name': 'Pluto', 'age': 3})
goofy = Dog({'name': 'Goofy', 'age': 2})
buttons = Cat(('Mr. Buttons', 4))

animals = (pluto, goofy, buttons)

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])
