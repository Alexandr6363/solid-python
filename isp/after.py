"""
    В данном примере методы разделяются по назначению
    => Что можно подключать только нужные интерфейсы ( метод - классы ).
    --------------------------------
    Отсутсвует доступ к ненужным интерфейсам ( talk у класса Cat )
"""


class Creature:
    """Класс отвечающий за имя создания"""
    def __init__(self, name):
        self.name = name


class SwimmerInterface:
    """Класс отвечающий за умение плавать"""
    def swim(self):
        pass


class WalkerInterface:
    """Класс отвечающий за умение ходить"""
    def walk(self):
        pass


class TalkerInterface:
    """Класс отвечающий за умение говорить"""
    def talk(self):
        pass


# Подключаются только нужные нтерфейсы ( класс )
class Human(Creature, SwimmerInterface, WalkerInterface, TalkerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")

    def talk(self):
        print(f"I'm {self.name} and I can talk")


class Fish(Creature, SwimmerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")


class Cat(Creature, SwimmerInterface, WalkerInterface):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")


human = Human("John Doe")
human.swim()
human.walk()
human.talk()

fish = Fish("Nemo")
fish.swim()

cat = Cat("Mr. Buttons")
cat.walk()
cat.swim()
