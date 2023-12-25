from collections import Counter

# Problem-1: Count the number of 1's from a given list without any conditional opertions:

# Solution:

# Hint: using Arithmetic operations:

input = [0,0,0,0,1,1,0,1,1]
# output = 4

count = 0

for i in input:   
    # i += i    
    count += i
print(count)

# --------------------------------------------

# Problem-2 - Frequency of each character in  in dictionary format:

input = [0,2,3,4,4,5,6,8,8,9]
# output = element with count in dict format.


all_freq = {}

for i in input:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print(all_freq)
