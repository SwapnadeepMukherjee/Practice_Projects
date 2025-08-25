Notes from the following links:

https://www.datacamp.com/blog/top-python-interview-questions-and-answers
https://www.geeksforgeeks.org/python/decorators-in-python/ - Needs further read.

What are Decorators in Python?

Decorators in Python are a design pattern that allows you to add new fucntionallity to an exisiting object without modifying it's strucuture. They are commonly used to extend the behaviour of functions / methods. 

## Example code:

```
def my_decorator(fucntion):
	def wrapper():
	print("Something is happening before this function is called.")
	func()
	print("Something is happening after the function is called.")
return wrapper

@my_decorator
def say_hello():
	def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

