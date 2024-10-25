# name mangling in python


class Parent:
    def __init__(self) -> None:
        self.__private_attribute = "I am private!"


class Child(Parent):
    def print_private_attribute(self):
        print(self._Parent__private_attribute)


child = Child()

child.print_private_attribute()
