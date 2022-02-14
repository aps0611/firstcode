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



