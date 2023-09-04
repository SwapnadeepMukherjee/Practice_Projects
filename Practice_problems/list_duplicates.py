# Problem - Given a list as follows -

# list1 = [1,1,2,2,3,4,5,5,5,5,6]

# `WAP to make a list of all duplicate elements.

# Approach - 1: # Using count keyword

# list1 = [1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6]
# # list2 = list(dict.fromkeys(list1))
# list2 = list(set(list1))
# print('List-2', list2)
#
# count1 = 0
# list3 = []
# for i in list2:
#     count1 = list1.count(i)
#     if count1 > 1:
#         list3.append(i)
# print(list3)

# Approach - 2: # Using standard approach -

list1 = [1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6]
# list2 = list(dict.fromkeys(list1))
list2 = list(set(list1))

list4 = []
for i in range(len(list1)):
    count1 = 0
    for j in range(i, len(list1)):
        if list1[i] == list1[j]:
            count1 += 1
    if count1 > 1:
        if list1[i] not in list4:
            list4.append(list1[i])

print("Final list", list4)