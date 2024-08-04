#Inheritance 
'''Inheritance helps us in defining a class that inherits
all the methods and properties from another class. 
PARENT CLASS from which the properties are inherited 
CHILD CLASS which inherits the properties from parent'''

#Create a class named Person, with firstname and lastname properties, and a printname method: which is the parent class 
class Person:
    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def printName(self):
        print(self.firstName + self.lastName)
# child class 
class Student(Person):
    pass # when we dont want to add any other property or method
