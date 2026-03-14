# WAP Sort a list without using the sort() or sorted() function:

# Approach - 1:

lst = [5, 2, 9, 1, 5, 6]

n = len(lst)

for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
        #swap:
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
        
print(lst)

# Approach - 2:

for i in range(len(lst)):
    min_index = i
    for j in range(i + 1, len(lst))):
        if lst[j] < lst[min_index]:
            min_index = j
            
    lst[i], lst[min_index] = lst{min_index}, lt[i]

print(lst)