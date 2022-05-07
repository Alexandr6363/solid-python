# Все классы едино образны и можно испольтзовать класс-Потомок,
# вместо класса-Родителя
class Animal:
    def __init__(self, name, age):
        """
        В базовый класс Animal теперь передаются 2 атрибута,
        которые записываются в словарь
        :param name: Имя
        :param age: Возраст
        """
        self.attributes = {'name': name, 'age': age}

    def eat(self, _amount=0):
        """
        Есть возможность указывать количество сьеденного корма,
        но это является не обязательным параметром
        :param _amount: = 0 ,но не фигурирует
        :return:
        """
        print("Ate some food!")


class Cat(Animal):
    def __init__(self, name, age):
        """
        Делегирует работу родительскому методу
        """
        super().__init__(name, age)

    def eat(self, amount=0.1):
        """
        Используется возможность указывать количество съеденного корма,
        :param amount: = 0.1
        :return: Возвращается ответ в зависимости от количества съеденного корма
        """
        if amount > 0.3:
            print("Can't eat that much!")
        else:
            print("Ate some cat food!")


class Dog(Animal):
    """
        Делегирует работу родительскому методу
    """
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, _amount=0):
        print("Ate some dog food!")


# Все атрбуты передаются в одном формате
pluto = Dog('Pluto', 3)
goofy = Dog('Goofy', 2)
buttons = Cat('Mr. Buttons', 4)

animals = (pluto, goofy, buttons)

for animal in animals:
    if animal.attributes['age'] > 2:
        print(animal.attributes['name'])
