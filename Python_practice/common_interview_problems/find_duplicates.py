# WAP Find duplicate elements in a list using Python:

# Approach - 1:

lst = [1,2,3,3,5,5,7,6,8]

duplicate = set()

seen = set()

for i in lst:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
    
print(list(duplicates))

# Approach - 2:

duplicates = set([x for x in lst if.count(x) > 1])

print(list(duplicates))