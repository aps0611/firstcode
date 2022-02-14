#Behaviour part of the object: Attributes and Methods


class Student: #any function inside the class are reffered as Methods.
   
  def __init__(self, roll_no, name, total):
  
    self.roll_no = roll_no 
    self.name = name
    self.total =total
    
  def display(self): 
    print(self.roll_no, self.name, self.total)
  
  #this below function displays the behaviour
  def result(self):
    if self.total > 100:
      print('pass')
    else:
      print('fail')
  

s0 = Student (0,'Bhuvnesh', 100)
s0.display()
s0.result()

s1= Student(1,'Harish', 150)
s1.display()
s1.result()

