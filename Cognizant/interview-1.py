# Problem statement - https://www.geeksforgeeks.org/python-extract-numbers-from-list-of-strings/

# Solution Approach -

# 1. First -

import re

input = "I was 27 years 4 years ago"
# output = [27, 4]

output = []

output = re.findall('\d+', input)
print(output)

# 2. Second -

import re


def extract_numbers(string):
    numbers = re.findall(r'\d+', string)
    return list(numbers)


input_string = "I was 27 years 4 years ago"
numbers_list = extract_numbers(input_string)
print(numbers_list)

# 3. Third -

in_array = []
inp = int(input("Please enter your array length"))

for i in range(inp):
    in_arr = int(input("Please enter element of the array"))
    in_array.append(in_arr)

sort_in_arr = sorted(in_array)

if inp % 2 == 0:
    print(sort_in_arr[int(inp / 2)], sort_in_arr[int(inp / 2 + 1)])
else:
    print(inp / 2)
