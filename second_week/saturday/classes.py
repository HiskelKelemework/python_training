class Animal:
    name = "Lion"
    age = 12
    height = 1.3


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def walk(self):
        print(self.name, "is walking")

    def talk(self):
        print(self.name, "is talking")

    def eat(self):
        print(self.name, "is eating")


abebe = Person("Abebe", 35, 1.85)
kebede = Person("Kebede", 24, 1.77)

abebe.walk()
kebede.walk()

# model a television.
