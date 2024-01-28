# Problem statement: Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

# Remember, don't run the function, simply provide the definition.

# To give an idea what the function would look like when tested:

# myfunc('Anthropomorphism')
Output: 'aNtHrOpOmOrPhIsM'

# myfunc('Swapnadeep')
# Output: 'SwApNaDeEp'

# Added note: this exercise requires that the function return a string. Print statements will not work here.

# Solution Approach: 

def myfunc(a):
    myfinallist = []    
    mylist = list(a)
    for l in range(len(mylist)):
        if l % 2 == 0:
            upper = mylist[l].upper()
            myfinallist.append(upper)
        elif l % 2 != 0:
            lower = mylist[l].lower()
            myfinallist.append(lower)
    
    
    return "".join(myfinallist)

print(myfunc('Swapnadeep'))