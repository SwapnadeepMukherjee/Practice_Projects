# What are generators in Python and why are they useful?

# Generators is a special type of functions that returns an iterator which produces values one at a time and instead of returning all values at once.

# Example using yeild:

def count_up_to(n):
	i = 1
	while i <= n:
		yield i
		i += 1
 
# Using the generator: 
 
for num in count_up_to(5):
     print(num)

# output:

#1
#2
#3
#4
#5