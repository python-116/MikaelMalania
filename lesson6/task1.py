# Classes in python

class Car:
    # ესე კოდს არ ვწერთ
    wheels = 4

    def __init__(self, make, color, name: str, surname: str):
        # Instance attributes
        self.make = make
        self.color = color
        self.name = name
        self.surname = surname

    def start_engine(self):
        # check if name and surname equal to a specific value if so then do something
        if self.name == "abc" and self.surname == "def":
            print("Special condition triggered")
        return f"{self.make} with the color of {self.color} is starting the engine"


# Creating instances of the class
car1 = Car("BMW", "Black", "John", "Doe")

car2 = Car("Mercedes", "White")

print(car1.wheels)
print(car1.start_engine("abc", 'def'))
# print(car2.start_enginex)
print(car2)
