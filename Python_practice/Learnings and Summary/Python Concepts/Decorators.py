# Example: 1

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# ----------------------------------------------------------------|

# Exmaple: 2

import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f"Took {t2} seconds")

    return wrapper


@tictoc
def do_this():
    # simulating running code..
    time.sleep(1.3)


@tictoc
def do_that():
    # simulating running code..
    time.sleep(1.3)


do_this()
do_that()
print("done")

# Output:

# swapnadeepmukherjee@Swapnadeeps-MacBook-Pro Personal_data % python3 decorator.py
# Took 1.3050940036773682 seconds
# Took 1.3010389804840088 seconds
# done
