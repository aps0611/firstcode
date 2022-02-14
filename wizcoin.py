class Wizcoin:
  def __init__(self, galleons, sickles, knuts): #initialiser
    self.galleons = galleons
    self.sickles = sickles 
    self.knuts = knuts
    #__ini__() never has a return statement
  
  def value(self):
    return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)
  
  def weightInGrams(self):
    return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

  def __repr__(self):
    '''returns the string of an expression that recreates this object'''
    return f'{self.__class__.__qualname__}({self.galleons},{self.sickles},{self.knuts})'
  def __str__(self):
    return f'{self.galleons}g,{self.sickles}s,{self.knuts}k'

  def __add__(self, other): #other is the convention
    if not isinstance(other, Wizcoin):
      return NotImplemented
    
    return Wizcoin(other.galleons + self.galleons, other.sickles + self.sickles, other.knuts + self.knuts)



