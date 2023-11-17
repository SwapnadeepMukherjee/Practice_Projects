# 1. Introduction

# 2. Past Projects and their explanation.

# 3. What are the different memory management techniques in Python?

# Solution - Please refer the following -

# 1. https://www.educative.io/answers/how-is-memory-managed-in-python
# 2. https://docs.python.org/3/c-api/memory.html

# 4. What are the different concepts of OOPs paradigm you are aware of?

# Inheritance -

# class a:
#
#     body
#     car
#
# class b(a):
#
#     body
#
#     b1.car()

# Polymorphism -

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


def main():
    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        animal.speak()


if __name__ == "__main__":
    main()


# Example - 2 ->

class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"


class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__init__()
        # print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)


# 5. What is the difference between hosting a microservice on an Amazon-ECR vs on Kubernetes?

# Solution - https://stackshare.io/stackups/amazon-ecr-vs-kubernetes


# Skills required to succeed in the role =

# web-app
# automations
# git / Devops
