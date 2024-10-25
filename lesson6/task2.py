# Inheritance in classes

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow meow!"


dog = Dog("Rex")
cat = Cat("Tom")

print(dog.speak())
print(cat.speak())
