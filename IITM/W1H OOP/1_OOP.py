# Object Oritented Programing: OOP 
# Every living and non-living entity is an object
# Every Individual object have attribute and behaviour.
# Translates the gerneral world into programming
# Attributes are Variables and Behaviour are Functions.
# Every object has its own identity.


class Student: #first letter of class name is Capital: i.e. Standard practice which is normally followed.
  roll_no = None
  name = None

s0 = Student() #object of class Student #special type of function. 
#using the constructor Student() we constructed the object s0
s0.roll_no = 0 
#inside object s0 there are 2 variables called roll_no and name
s0.name = 'Bhuvnesh'
#DOT Operator: whenever we need to access an entity that belongs to object

print(s0.roll_no, s0.name)

s1 = Student()
print(s1.roll_no,s1.name)








