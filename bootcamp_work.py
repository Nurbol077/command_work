print("Start Project")

class Animal :
    def __init__(self,name,color):
        self.name = name
        self.color = color

a = Animal("Dog" , "red")
print(a.name)
print(a.color)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Student("John", 25)
print(a.name)
print(a.age)



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

mashina = Car("Tayota","Camry")
print(mashina.brand)
print(mashina.model)

