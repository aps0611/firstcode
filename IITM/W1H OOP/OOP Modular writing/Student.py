from Person import Person

class Student(Person): #Child class
  def __init__(self, name, age, marks):
    super().__init__(name,age)
    self.marks = marks
  
  def display(self):
    print(self.name, self.age, self.marks) #Method overriding 