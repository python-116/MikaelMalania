# super() function usage

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello I am {self.name}!"


class Child(Parent):
    def __init__(self, name: str, hobby: str):
        super().__init__(name)
        self.hobby = hobby

    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting} I like {self.hobby}!"


class GrandChild(Child):
    def __init__(self, name: str, hobby: str, age: int):
        super().__init__(name, hobby)
        self.age = age

    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting} I am {self.age} years old!"


child1 = Child("John", "playing football")
child2 = Child("Mary", "playing piano")

grandchild1 = GrandChild("John", "playing football", 10)
grandchild2 = GrandChild("Mary", "playing piano", 12)

print(child1.greet())
print(child2.greet())

print(grandchild1.greet())
print(grandchild2.greet())
