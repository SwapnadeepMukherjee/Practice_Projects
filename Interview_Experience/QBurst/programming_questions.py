# # Problem -1 - WAP use a decorator function to demonstrate output of division by two numbers:
#
# # Solution Approaches:
#
# # 1. Simple example to explain decorator:
#
# # Python program to illustrate functions can be treated as objects
#
# def shout(text):
#     return text.upper()
#
#
# print(shout('Hello'))
# yell = shout
# print(yell('Hello'))
#
#
# 2. https://replit.com/@SwapnadeepMukherjee/59-Day-59-Decorators-in-Python -

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx


@greet
def hello():
    print("Hello World")


@greet
def add(a, b):
    print(a + b)


hello()
add(1, 2)
# greet(hello)()


# Problem - 2 - WAP to find the given sub-string inside a string:

# import re
#
input = "121324swapnadeep 5454 121121324swapnadeep324swapnadeep   swapnadeep"


#
# # Approach - 1:
# count = len(re.findall("swapnadeep", input))
# print(count)

# Approach - 2:

def find_substring(input_string, substring):
    """Returns a list of indices where the substring is found in the input string.

  Args:
    input_string: The string to search.
    substring: The substring to find.

  Returns:
    A list of indices where the substring is found in the input string, or an empty
    list if the substring is not found.
  """

    result = []
    len_res = 0
    for i in range(len(input_string)):
        if input_string[i:].startswith(substring):
            result.append(i)
            len_res = len(result)
    return len_res


# Example usage:

input = "121324swapnadeep 5454 121121324swapnadeep324swapnadeep   swapnadeep"
substring = "swapnadeep"

result = find_substring(input, substring)

if result:
    # print("The substring is present at index", result)
    print("The occurrences of substring present", result)
else:
    print("The substring is not present in the string")
