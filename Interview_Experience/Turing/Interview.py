# Initially scheduled for Thursday(July 17th): 7pm -8pm IST
# Then moved to Monday(July 21st): 7pm to 8pm IST and finally happened on 7.30pm - 8.30pm IST

# First 15-minutes started with a  brief introduction about each other, then started the formal interview process:

# Interviewer Name: Shivam Chabbra

# 	1. Tell me recently about 1/2 projects of yours and explain in details.
# 	2. Follow-up question: how did you configure your secrets in your Jenkins server?
# 	3. Imagine you have huge dataset and we havse setup a Python code that is giving out correct output that is designed with nested loops only. How do you optimize the code? : Pandas, Numpy, List Comprehension, …
# 	4. How will you design a Python application using Docker and write a docker file such that you don't have to manage pipeline manually and the dockerfile itself manages the sync between Production and non-production code? What are the parameters that you will use?
# 	5. Design a custom exception that will define something and show the output by using it in a function in python.

#   Answer to question 5:

#   Custom execptions in Python allow us to create our specific error types to handle situations unique to out application domain. 
#   This can improve code quality, make error handling much more granular and enchacnce reusability.

#   Designing a custom exception:

#   To create a custom exception, we create a new class that inherits from built-in Exception class or one of it's sub-classes
#   (like valueError or TypeError). It's a good practice to suffix the custom execption class name with "Error" for clartiy. 
#   We can also customise it's behaviour by overriding the constructor (__init__) and other methods like it __str__

#   Syntax:
#   class CustomError(Exception):
#   ...
#   pass

#   try:
#   ...

#   except CustomError:
#   ...

#   Sample Exception:
class InvalidInputError(ValueError): # inhertiing from VAlueError for clarity.
    """Customer exception raised for invalid input values"""

    def __init__(self, message, input_value=None):
            super().__init__(message) #Call the parent classes constructor
            self.input_value = input_value #Store the invalid input value
    
    def __str__(self): #Customise string representation of the exception
          if self.input_value is not None:
                return f"{self.args[0]} Provided input: {self.input_value}"
          return self.args[0]
    
# Using the custom exception in a file:

# We can use the raise keyword to explicitly raise your custom exception within a function when a specific error condition is met.

def process_data(data):
    if not isinstance(data, (int, float)):
        raise InvalidInputError("Data must be a number.", data)  # Raising the custom exception
    if data <= 0:
        raise InvalidInputError("Data must be positive.", data)

    return data * 2

# Simple example to understand this custom exception using eligible voter example:
class AgeError(Exception):
    "Raised when persons age is less than 18"
    pass

try:
    age = int(input("Enter age:"))
    if age < 18:
        raise AgeError
except AgeError:
    print("person is ineligible to caste their vote")     
else:
    print("person is eligable to caste their vote")