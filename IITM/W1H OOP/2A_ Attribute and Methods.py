#Behaviour part of the object: Attributes and Methods


class Student: #class and class name
  count = 0 #this is owned by class and not its object i.e. S0 or S1 and hence shared by all the objects 
  
  def __init__(self, roll_no, name, total): #Method called init and __ called dunder
  #this is special function that exists inside every single class inside python programming language.
    self.roll_no = roll_no #on right hand side are parameters which takes values from function paranthesis
    self.name = name
    self.total = total
    #variable inside init belong to specific objects
#self.name and self.roll no are attributes or object variables.
  def display(self): #regular function
    print(self.roll_no, self.name, self.total)
  

s0 = Student (0,'Bhuvnesh', 100)
Student.count += 1
s0.display()
#value of slef is now s0

s1= Student(1,'Harish', 150)
Student.count += 1
s1.display()
#value of self is now s1

print(Student.count)

