# How to find all occurrences and their count in a given string?

# solution - 

# Approach -1: Using a for loop:

string = 'banana'
count = 0
for char in string:
  if char == 'a':
    count += 1
print(count)

# Approach - 2: Using the count() method:

string = 'banana'
count = string.count('n')
print(count)

# Approach - 3: Using regular expressions:

import re
string = 'banana'
count = len(re.findall('[n]', string))
print(count)