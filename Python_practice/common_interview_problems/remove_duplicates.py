# Write a Python script to remove duplicates from a list:

# Approach:

lst = [1,2,3,3,5,5,7,6,8]

lst1 = list(set(lst))

print(lst1)

# Approach - 2:

lst = [1,2,3,3,5,5,7,6,8]

lst1 = []

for i in lst:
   if i not in lst1:
       lst1.append()

print(lst1)

# Approach - 3:

lst = [1,2,3,3,5,5,7,6,8]

lst1 = list(dict.fromkeys(lst))

print(lst1)