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


class Television:
    def __init__(self, model, size, price, weight, type, volume=20, channel=1):
        self.model = model
        self.size = size
        self.price = price
        self.weight = weight
        self.type = type

        self.volume = volume
        self.channel = channel

    def __str__(self):
        return self.model + " " + self.size + " " + self.type

    def volumeUp(self, upBy=1):
        if self.volume + upBy > 100:
            return

        self.volume += upBy
        print("volume is", self.volume)

    def volumeDown(self, downBy=1):
        if self.volume - downBy < 0:
            return

        self.volume -= downBy
        print("volume is", self.volume)

    def channelUp(self):
        self.channel += 1
        print("channel is", self.channel)

    def channelDown(self):
        self.channel -= 1
        print("channel is", self.channel)


class RemoteControl:
    def __init__(self, tv):
        self.tv = tv

    def volumeUp(self, upBy=1):
        self.tv.volumeUp(upBy)


class Tire:
    def __init__(self, radius, brand):
        self.radius = radius
        self.brand = brand


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Vehicle:
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def drive(self, type="vehicle"):
        print(type, "driving with ", len(self.tires), "wheels")


class Car(Vehicle):
    def __init__(self, engine, tires):
        super().__init__(engine, tires)

    def drive(self):
        super().drive("car")


class MotorCycle(Vehicle):
    def __init__(self, engine, tires):
        super().__init__(engine, tires)

    def drive(self):
        super().drive("motorcycle")


# car_engine = Engine(500)
# car_tires = [
#     Tire(22, "Bridgestone"),
#     Tire(22, "Bridgestone"),
#     Tire(22, "Bridgestone"),
#     Tire(22, "Bridgestone"),
# ]

# car = Car(car_engine, car_tires)
# car.drive()

# motorcycle_engine = Engine(100)
# motorcycle_tires = [
#     Tire(18, "Bridgestone"),
#     Tire(18, "Bridgestone"),
# ]

# bugati = MotorCycle(motorcycle_engine, motorcycle_tires)
# bugati.drive()

# Person
#    def __init__(self):
#         self.numberOfLegs

#     def walk(self):
#         pass

#     def talk(self):
#         pass

# Dog
# walk
# bark

# birds have numberOfWings, numberOfLegs
# Eagle
# walk
# fly

# Parrot
# talk
# fly

class Animal:
    def __init__(self, numberOfLegs, name):
        self.numberOfLegs = numberOfLegs
        self.name = name

    def walk(self):
        print(self.name, "walking...")


class Person(Animal):
    def __init__(self):
        super().__init__(2, "Person")

    def talk(self):
        print("person talking..")


class Dog(Animal):
    def __init__(self):
        super().__init__(4, "Dog")

    def bark(self):
        print("wooof woof")


class Bird(Animal):
    def __init__(self, numberOfWings, numberOfLegs, name):
        super().__init__(numberOfLegs, name)
        self.numberOfWings = numberOfWings

    def fly(self):
        print(self.name, "is flying with", self.numberOfWings, "wings")


class Eagle(Bird):
    def __init__(self):
        super().__init__(2, 2, "Eagle")


class Parrot(Bird):
    def __init__(self):
        super().__init__(2, 2, "Parrot")

    def talk(self):
        print(self.name, "talking")


eagle = Eagle()
eagle.walk()

parrot = Parrot()
parrot.walk()
parrot.talk()

person = Person()
person.walk()
person.talk()
