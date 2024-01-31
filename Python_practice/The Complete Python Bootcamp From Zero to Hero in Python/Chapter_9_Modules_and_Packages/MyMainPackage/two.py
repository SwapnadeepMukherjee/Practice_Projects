import one

print("Top level in two.py")

one.func()

if __name__ == "__main__":
    # main()
    print("Two.py is being run directly")
else:
    print("Two.py is has been imported!")
