# Example - 1 - GFG - https://www.geeksforgeeks.org/method-overriding-in-python/

# Python program to demonstrate the concept of: `method overriding`

# Defining parent class -
class Parent:

    # Constructor -
    def __init__(self) -> object:
        self.value = "Inside Parent"

    # Parent's show method:
    def show(self):
        print(self.value)


# Defining child class -
class Child(Parent):

    # Constructor -
    def __init__(self):
        super().__init__()
        self.value = "Inside Child"

    # Child's show method:
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


# Example - 2 - CWH - https://replit.com/@codewithharry/74-Day-74-Method-Overriding#main.py

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()


# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())
