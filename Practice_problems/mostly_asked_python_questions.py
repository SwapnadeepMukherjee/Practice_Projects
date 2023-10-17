# # Problem - 1 - WAP to generate an infinite Fibonacci Series using Generators -
#
# def fibo():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# f1 = fibo()
# # for i in f1:
# #     print(i).
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
#
# # Problem - 2 - WAP to sort a list without using sort keyword -
#
# # Python program to print a list
# # without using the sort() function
# # without an extra variable
#
# l1 = [76, 23, 45, 12, 54, 9]
# print("Original List:", l1)
#
# # sorting list using nested loops
# for i in range(0, len(l1)):
#     for j in range(i + 1, len(l1)):
#         if l1[i] >= l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
#
# # sorted list
# print("Sorted List", l1)
#
#
# # Check the remaining solutions here - https://www.geeksforgeeks.org/sort-a-list-in-python-without-sort-function/
#
#
# # Problem - 3 - WAP to check whether a string palindrome -
#
# # Easiest way using string slicing -
#
# def is_palindrome(string):
#     """
#     Checks if the given string is a palindrome or not.
#
#     Args:
#       string: The string to check.
#
#     Returns:
#       True if the string is a palindrome, False otherwise.
#     """
#
#     # Convert the string to lowercase.
#     string = string.lower()
#
#     # Reverse the string.
#     reversed_string = string[::-1]
#
#     # Check if the string is equal to its reverse.
#     return string == reversed_string
#
#
# # Driver code
# string = "racecar"
# ans = is_palindrome(string)
#
# if ans:
#     print("Yes")
# else:
#     print("No")
#
#
# # Alternative way -
#
# def is_palindrome(string):
#     """Returns True if the given string is a palindrome, False otherwise."""
#
#     # Convert the string to lowercase.
#     string = string.lower()
#
#     # Iterate over the string, comparing each character to its counterpart at the opposite end.
#     for i in range(int(len(string) // 2)):
#         if str[i] != str[len(str) - i - 1]:
#             return False
#     # If we reach this point, the string must be a palindrome.
#     return True
#
#
# # main function
# s = "malayalam"
# ans = is_palindrome(s)
#
# if not ans:
#     print("No")
# else:
#     print("Yes")

# # Problem - 4 - WAP to sort a particular dictionary / by using dictionary comprehension -
#
# # Sort a dictionary -
#
# dict1 = {575: "Apple", 876: "Mango", 132: "Grapes", 782: "Banana"}
#
# d = sorted(dict1.keys())
#
# dict2 = {}
# for i in d:
#     dict2[i] = dict1[i]
# print(dict2)
#
#
# # # Sort A Dictionary (BY VALUE) -
#
# def sort_dictionary_by_value(dict1):
#     """Sorts a dictionary by value.
#
#   Args:
#     dict1: A dictionary to be sorted.
#
#   Returns:
#     A new dictionary sorted by value.
#   """
#
#     sorted_dict = {key: value for key, value in sorted(dict1.items(), key=lambda x: x[1])}
#     return sorted_dict
#
#
# # Example usage:
#
# dict1 = {575: "Apple", 876: "Mango", 132: "Grapes", 782: "Banana"}
#
# sorted_dict = sort_dictionary_by_value(dict1)
#
# print(sorted_dict)
#

# Problem - 5 - WAP to find the pair with given number in a list -

def find_pair_with_given_number(lst, number):
    """Finds the pair in the given list with the given sum.

  Args:
    lst: A list of integers.
    number: The sum to find a pair for.

  Returns:
    A tuple of two integers, or None if there is no pair in the list with the
    given sum.
  """

    lst.sort()
    i = 0
    j = len(lst) - 1

    while i < j:
        sum = lst[i] + lst[j]
        if sum == number:
            return lst[i], lst[j]
        # elif sum < number:
        #     i += 1
        # else:
        #     j -= 1
        #     return None


# Driver code -
pair = find_pair_with_given_number([2, 4, 6, 8], 10)


# Problem - 6 - WAP to create a fibonacci series using recursion -

def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Driver Program
print(Fibonacci(0))

# 0 1 1 2 3 5 8 13 21 34
# 0 1 2 3 4 5 6 7 8 9
