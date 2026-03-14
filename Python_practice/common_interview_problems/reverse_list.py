# WAP reverse a string without using built-in functions:

# Approach - 1(using built-ins):

s = "hello"
reversed_string = s[::-1]

print(reversed_string)

# Approach - 2:

s = "hello"
rev = ""

for char in s:
	rev = c + rev

print(rev)

# Approach - 3:

s = "hello"

reversed_string = ""

for i in range(len(s)-1, -1, -1):
    reversed_string += s[i]

print(reversed_string)