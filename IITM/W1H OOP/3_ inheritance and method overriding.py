#Inheritance and Method Overriding:

class Person: #Parent class
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def display(self):
    print(self.name, self.age)


class Student(Person): #Child class
  def __init__(self, name, age, marks):
    super().__init__(name,age) #inheritance
    self.marks = marks
  
  def display(self):
    print(self.name, self.age, self.marks) #Method overriding 

class Employee(Person): #Child class or subclass
  def __init__(self, name, age, salary):
    super().__init__(name,age)
    self.salary = salary
  
  def display(self):
    super().display()
    print(self.salary)

s= Student('Akash', 20, 250)
s.display()

e = Employee('Amit', 30, 300)
e.display()


