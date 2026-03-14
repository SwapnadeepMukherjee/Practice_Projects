# What is list comprehension, and how is it different from loops?

# List comprehension is a concise and Pythonic way to create a new list by applying an expression to each element in an iterable, optionally with a condition.

# Instead of writing multiple lines using a loop, list comprehension allows us to perform the same operation in a single readable line.

# Syntax:

# [expression for item in iterable if condition]

# Example using a loop:

numbers = [1, 2, 3, 4, 5]

squares = []
for num in numbers:
    squares.append(num ** 2)

print(squares)  # Output: [1, 4, 9, 16, 25]

# Example using list comprehension:

numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)  # Output: [1, 4, 9, 16, 25]