# Practice_Problem - 2 -
#
# To be completed in 10 min
#
# Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping.
#
# If there are no ingredients or toppings, the method should return an empty list.
#
# For example: IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops() should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

# Start-up code

class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        pass


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
# print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

# 1. Solution Approach - Less Efficient/Nasty Approach(To be not taken just for clarification purpose) -

class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        if self.ingredients == [] or self.toppings == []:
            return []

        else:
            b = []
            for intgr_temp in self.ingredients:
                a = []
                for top_temp in self.toppings:
                    a.append([intgr_temp, top_temp])
                b.append(a)
            return b


# TestCase - 1 - Testing for list not empty - 1
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
# should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
print("I am in print", machine.scoops())

# Testing for one list  empty
machine = IceCreamMachine(["vanilla", "chocolate"], [])
print(machine.scoops())

# Testing for both lists  empty
machine = IceCreamMachine([], [])
print(machine.scoops())

# 2. Solution Approach - Elegant solution -
#
# itertools is a module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
#
# The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an “iterator algebra” making it possible to construct specialized tools succinctly and efficiently in pure Python.

from itertools import product


class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        return [list(p) for p in product(self.ingredients, self.toppings)]


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
