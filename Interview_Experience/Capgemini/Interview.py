import copy
from collections import Counter

# Combine and convert list to dictionary -
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

convert_dict = zip(list1, list2)
dict1 = dict(convert_dict)
print(dict1)

# Reference - https://www.w3schools.com/python/ref_func_zip.asp

# ----------------------------------------|

# Delete second element in list1 -
list1.pop(1)
print(list1)

# Reverse a list -
print(list2[::-1])

# ----------------------------------------|

# Print the output (Needs to be completed) -
# input = "My name is Swapnadeep"
# output = {m:2, y:1, n:1, a:3, ..}

# Approach - 1:

# using naive method to get count
# of each element in string
test_str = "My name is Swapnadeep"

all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print("Count of all characters in " + test_str + " is :\n "
      + str(all_freq))

# Approach - 2:

# Python3 code to demonstrate
# each occurrence frequency using
# collections.Counter()
# initializing string
test_str = "GeeksforGeeks"

# using collections.Counter() to get
# count of each element in string
res = Counter(test_str)

# printing result
print("Count of all characters in " + test_str + " is :\n "
      + str(res))


# Reference - https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/

# ----------------------------------------|

# Explain Decorators with example -
def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("thanks for listening")

    return mfx()


@greet
def hello():
    print("I am in greet fucntion")


# ----------------------------------------|

# DeepCopy vs ShallowCopy
ds_list = [1, 2, 3, 4]

# shallowCopy -
print(copy.copy(ds_list))

# DeepCopy -
print(copy.deepcopy(ds_list))

# Reference - https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

# ----------------------------------------|

# Demonstrate Constructor with example -
class Swapnadeep:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return "{}.{}".format(self.first, self.last)


nme = Swapnadeep("Swapnadeep", "Mukherjee")
print(nme.fullname())

# Keyword to inherit attribute of a parent class -
# __super__
