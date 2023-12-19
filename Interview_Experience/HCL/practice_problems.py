# fibonacci using generator:

def fib_gen():
    a = 0
    b = 1

    while True:
        c = a
        a = b
        b = c + a
        yield c


f = fib_gen()
for i in range(20):
    print(next(f))

# Reverse a list using Python:

lst = [4, 7, 9, 2]

# reverse()
lst.reverse()
print(lst)

# reversed
list3 = reversed()

# slicing:
list2=lst[::-1]

# without using 