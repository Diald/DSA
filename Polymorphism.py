#Polymorphism 
'''Polymorphism is often used in classes it means a method
having the same name, polymorphism generally means some
operators/functions/methods having the same names used in different
places with different meanings'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive")
