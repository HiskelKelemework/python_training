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


sony = Television("Sony", "24 In.", 12000, 8, "Flat screen")
