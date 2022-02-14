#SETTERS are normally used to VALIDATE THE Attributes passed to an object.

class WizCoin:
  def __init__(self, galleon, sickles, knuts):
    self.galleon = galleon
    self.sickles = sickles
    self.knuts = knuts
    #init never has a return statement

    @property
    #Getter
    def galleon(self):
      return self._galleon
    
    @galleon.setter
    def galleon(self, value):
      print('Setting the value .... ')
      if not isinstance(value, int):
        raise ValueError('The value cannot be other than int')
      if value < 0:
        raise ValueError('THe value must be more than 0')
      self._galleon = value

##This is not a complete code this is just for practice purpose