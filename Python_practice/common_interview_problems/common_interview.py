# What is the difference between list, tuple, set, and dictionary in Python?

# List - Ordered, Mutable
# Tuple - Ordered, Immutable
# Set - Unordered, Unique
# Dictionary - Unordered(Python 3.7), Ordered(After 3.7), Key-Value Pair

# Examples:

# L = [2,4,6,8]
# T = (3,5,7,9)
# S = {1,3,5,7}
# D = {a:1, b:2, c:3, d:4}

# What is the difference between mutable and immutable objects?

# The basic difference is in the way the objects are accessed and modified.
# In Mutable, they are accessed easily via apend, add operations while in immutable setup they are not.

# What are args and kwargs in Python?

# The basic is difference between args and kwargs are the way we define variables. Let's check it via an example as follows:

# *args:

def person(name, *data):

	print(name)
	print(data)
	
person('Swapnadeep', 32, 'Bengaluru', 9865432)

# **kwargs:

def person(name, **data):

	print(name)
	print(data)
	
person('Swapnadeep', age=32, city='Bengaluru', mob=9865432)

# Which Python libraries do you use for automation?

# Common answers:

# requests
# subprocess
# os
# paramiko
# boto3