# python One.py

def func():
    print("Func() in one.py")

def func1():
    pass

def func2():
    pass

print("Top level in one.py")

if __name__ == "__main__":
    # main()
    func1()
    func2()
    print("One.py is being run directly")
else:
    print("One.py is has been imported!")
