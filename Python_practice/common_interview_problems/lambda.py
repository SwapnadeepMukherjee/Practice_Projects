# What is a lambda function, and where would you use it?

# Basic Syntax:

# lambda arguments: expression

# Example 1 — Simple Addition

add = lambda a, b: a+b

print(add(3,5))

# Example 2 — Using Lambda with map():

numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, numbers))

print(squared)

# Output

# [1, 4, 9, 16]

# Example 3 — Using Lambda with filter():

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

# Output

# [2, 4, 6]

# Example 4 — Using Lambda for Sorting:

students = [
    ("Alice", 85),
    ("Bob", 70),
    ("Charlie", 95)
]

students.sort(key=lambda x: x[1])

print(students)