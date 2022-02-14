#Using PROPERTY 

class Celsius:
  
  def __init__(self, temp):
    self.temp = temp 
  
  def to_F(self):
    return (self.temp * 1.8) + 32

  #GETTER
  def get_temp(self):
    print('Getting Value .... ')
    return self._temp

  #SETTER
  def set_temp(self, value):
    print('setting value .... ')
    if value < -273.15:
      raise ValueError('Temp below -273 is not allowed')
    self._temp = value

  
  #Create the PROPERTY OBJECT:
  temp = property(get_temp, set_temp)

#Create object
human = Celsius(37)

print(human.temp)
print(human.to_F())

'''Whenever an object is created the init method is called. it has line self.temp = temp which automaticaly calls set_temp()
also any method call like human.temp will automatically call getter. like object creation calls setter'''


human2 = Celsius(-400)
#human2.temp = -400

