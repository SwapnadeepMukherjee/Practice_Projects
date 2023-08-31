# What is self? Explain with an example -

# When working with classes in Python, the term “self” refers to the instance of the class that is currently being
# used. It is customary to use “self” as the first parameter in instance methods of a class. Whenever you call a
# method of an object created from a class, the object is automatically passed as the first argument using the “self”
# parameter. This enables you to modify the object’s properties and execute tasks unique to that particular instance.

class mynumber:

    # Constructor -
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

obj1 = mynumber(17)
obj1.print_value()