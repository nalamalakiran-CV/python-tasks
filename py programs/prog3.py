""" Creating a class in python"""
""" Class: A class is a model or a blueprint for creating objects. The class 
    does not exist physically but an object does. we use a keyword called class
    to create class.
    Inside the class we will have constructor which takes self as a default 
    parameter, we will have instance method to access the variables inside the
    constructor """

#employee class

class Employee:
    def __init__(self, name='', age = 0): #constructor
        self.name = name
        self.age = age

    def details(self): #instance method
        print(self.name)
        print(self.age)
"""Here we have two objects they are 'emp1' and 'emp2' 
   we could create as many object as we want from a single class"""
emp1 = Employee('raju', 32)
emp1.details()

emp2 = Employee('ravi', 29)
emp2.details()

