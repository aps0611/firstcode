#NUMERIC DUNDER METHODS

class MY_NEW:
  def __init__(self, first):
    self.first = first
  
  def value(self):
    return self.first

  def __str__(self):
    return f'{self.first}'

  def __add__(self, other):
    return self.first + other.first

obj = MY_NEW(11)
print(obj)
obj2 = MY_NEW(22)
print(obj + obj2)

