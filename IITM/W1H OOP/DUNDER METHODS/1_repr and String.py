#DUNDER METHODS / SPECIAL METHODS / MAGIC METHODS

#reper __repr__() creates copy of object when run
#__str__() human readable string that provides useful information about the string

import datetime
newyears = datetime.date(2021, 1, 1)
print(repr(newyears)) #it displays the object method in string format
print(str(newyears)) 
print(newyears)

#object repr string is often used in technical context