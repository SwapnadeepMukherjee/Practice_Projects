# 1. Question - https://www.geeksforgeeks.org/python-extract-numbers-from-list-of-strings/

# Solution Approach -

# # 1. First -
#
# import re
#
# input_string = "I was 27 years 4 years ago"
# # output = [27, 4]
#
# output = re.findall('\d+', input_string)
# print(output)

# 2. Second -

import re


def extract_numbers(string):
    numbers = re.findall(r'\d+', string)
    return list(numbers)


string = "I was 27 years 4 years ago"
numbers_list = extract_numbers(string)
print(numbers_list)


# 2. Question - Given an array find the middlemost-element.

import math

in_array = []
len_array = int(input("Please enter your array length"))

for i in range(len_array):
    inp_array = input("Please enter element of the array")
    in_array.append(inp_array)

sort_in_array = sorted(in_array, reverse=False)
print(sort_in_array)

if len_array % 2 == 0:
    print(sort_in_array[int(len_array / 2) - 1], sort_in_array[int(len_array / 2)])
else:
    print(sort_in_array[math.floor(len_array / 2)])

