from collections import Counter

# list of 0's and 1's

input = [0,0,0,0,1,1,0,1,1]
# output = 4

count = 0

for i in input:   
    # i += i    
    count += i
print(count)

# --------------------------------------------

# Problem - Frequency of each character in list:

input = [0,2,3,4,4,5,6,8,8,9]
# output = element with count

all_freq = {}

for i in input:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print(all_freq)
