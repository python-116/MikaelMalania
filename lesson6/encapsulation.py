# Python program to
# demonstrate private members
# "__" double underscore represents private attribute.
# Private attributes start with "__".

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks123"

    def abc(self):
        self.a = "Private member of Base class"
        self.__c = "Private member of Base class"
# Creating a derived class


class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.a)
        print(self.__c)

    def pqr(self):
        self.__c = "Private member of Derived class"


# Driver code
obj1 = Base()
obj1.__c

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
