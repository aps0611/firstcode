#USing Getter and Setter:

class Celsius:
  def __init__(self, temp = 0):
    self.set_temp(temp)
    #self.temp = value (this is changed to below line format)
    #self.set_temp(value)
  
  def to_F(self):
    return (self.get_temp() * 1.8) + 32
  
  #GETTER Method:
  def get_temp(self):
    return self._temp #_ used to denote the private variables in python
  
  #SETTER Method:
  def set_temp(self, value):
    if value < -273.15:
      raise ValueError('Temp below -273 not allowed')
    self._temp = value

#Implementation

#Create an object called human
human = Celsius(37)

print(human.get_temp())
print(human.to_F())

human.set_temp(-300)