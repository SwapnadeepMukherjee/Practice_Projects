# What is lambda function in Python?

# Using lambda with map to double numbers in a list
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers) # Output: [2, 4, 6, 8]

# Using lambda with sorted to sort a list of dictionaries by age
employees = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
sorted_employees = sorted(employees, key=lambda emp: emp['age'])
print(sorted_employees) # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
