class car :
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
    def display(self):
        print(f"Name : {self.name}\nModel : {self.model}\nYear : {self.year}")

name1 = str(input('Enter the name of the car :'))
model1 = str(input('Enter the model of the car :'))
year1 = int(input('Enter the year of the car :'))

car1 = car(name1,model1,year1)


car1.display()

# Multiple inheritance

class Human:
    def __init__(self,age):
        self.age = age
    def display(self):
        print(f"Age : {self.age}")
class Student(Human):
    def display2(self,age):
        if age < 18:
            print('You are student')
class Amal(Student):
    def display3(self,age):
        if age == 17:
            print('You are Amal')

age1 = int(input('Enter the age :'))

hey1 = Amal(age1)

hey1.display3(age1)

class Animal:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f"Name : {self.name}")

class Dog(Animal):
    def __init__(self,name,age):
        self.age = age
        super().__init__(name)
    def display(self):
        super().display()
        print(f"Age : {self.age}")

name1 = str(input('Enter the name of the dog :'))
age1 = int(input('Enter the age of the dog :'))

dog1 = Dog(name1,age1)

print(dog1.display())
