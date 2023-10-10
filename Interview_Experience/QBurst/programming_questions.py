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

# Approach - 2 (Not complete/accurate yet):
output = input.split(" ")
count = 0
print(output)
sstring = 'swapnadeep'
for i in range(len(output)):
    if sstring in output[i]:
        count += 1
# count = len(output)
print(count)
