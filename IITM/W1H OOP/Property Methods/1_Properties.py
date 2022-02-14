#Properties and Dunder Methods

class Celsius : #Class that stores temp in degree
  def __init__(self, temp = 0):
    self.temp = temp

  def to_F(self): #Method to convert to Farhenite
    return (self.temp * 1.8) + 32

#Create a new object
human = Celsius()

#set temperature attribute
human.temp = 37

#Get the temp attribute
print(human.temp)

#Get the to_F Method
print(human.to_F())

#WHenever we retrieve any object attribute like temperature then it search for objects built in __dict__ attribute
print(human.__dict__)