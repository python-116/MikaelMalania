class Car:
    # კლასის შიგნით არსებულ ფუნქციას ეწოდება მეთოდი
    def __init__(self, model, passengers, color, speed):
        self.model = model
        self.passengers = passengers
        self.color = color
        self.speed = speed

    def accelerate(self):
        self.speed = self.speed + 2
        print(self.speed)


# აქ ვიძახებთ კლასსს და ვაწვდით ფრჩხილებში იმ პარამეტრებს რაც გავწერეთ __init__ - ში

bmw = Car("BMW", 4, "red", 5)
# ყოველ ჯერზე როდესაც ცვლადს ვანიჭებთ კლასს მნიშვნელობის სახით ამით ვქმნით ახალ ობიექტს~
# მაგ. bmw რასაც ახლა ზევით ვუყურებთ არის ახალი ობიექტი.
ferrari = Car("Ferrari", 2, "black", 10)
ford = Car("Ford", 6, "blue", 6)

bmw.accelerate()
print(bmw.color)

# ferrari.accelerate()
# print(ferrari.color)
# # note that the speed has been updated from the previous accelerate call
# ferrari.accelerate()

# print(ford.passengers)
# ford.accelerate()
