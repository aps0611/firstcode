#DUNDER METHODS / SPECIAL METHODS / MAGIC METHODS
import wizcoin

obj = wizcoin.Wizcoin(50,20,10)
print(str(obj))
#<wizcoin.Wizcoin object at 0x7f837ace1b80> this will be my output
print(repr(obj))
#<wizcoin.Wizcoin object at 0x7f48c4f3db80>

#so now lets tell python what to return instead of this not so readanble o/p 
#i have made changes in the wizcoin.py
print(obj) #this will call the __str__ dunder method