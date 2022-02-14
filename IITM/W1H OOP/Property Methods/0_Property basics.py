#PROPERTY BASICS:

class ClassWithProperty:
  
  def __init__(self):
    self.someAttribute = 'some initial value'

  @property #There is no colon
  def someAttribute(self):
    #GETTER METHOD
    return self._someAttribute
    #_is called backing variable and it is important to use the same.
  
  @someAttribute.setter
  def someAttribute(self, value):
    #SETTER METHOD
    self._someAttribute = value
  
  @someAttribute.deleter
  def someAttribute(self):
    #DELETER
    del self._someAttribute

#Implementation:

obj = ClassWithProperty()
print(obj.someAttribute)
obj.someAttribute = 'changed value'
print(obj.someAttribute)
del obj.someAttribute
print(obj.someAttribute)

