# Question 1:

# Input = a=[1,2,3,4], b=[3,4,5,6]
# Output = c=[4,6,8,10]

# Approach 1: Using 1 for loop and list iteration:

# two input lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
# empty resultant list
c = []

for i in range(len(a)):
    c.append(a[i] + b[i])

print("The merged output with approach 1 is:", c)

# Approach 2: Using List comprehension:

# two input lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
# empty resultant list
c = []

c = [a[i] + b[i] for i in range(len(a))]
print("The merged output with approach 2 is:", c)

# Approach 3: Using Numpy:

import numpy as np

# two input lists
a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])
# empty resultant list
c = []

c = a + b
print("The merged output with approach 3 is:", c)
