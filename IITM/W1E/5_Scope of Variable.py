

def myFunction1(x): #(Local Variable 1)
  x=x*2
  print('the value of x in function 1 is', x)

def myFunction2(x): #(Local Variable 2)
  x=x*3
  print('the value of x in function 2 is',x)

def myFunction3():
  global x #looks for global variable
  x=x*3 #changes values of global variable
  print('Value of x in myFunction3 is',x)

x=5 #GLOBAL VARIABLE x
print('Value of x before the function call is',x)
myFunction1(x)#value of x is passed from x=5 to myFunction1
#so the variable x in myfunction(x) is different than the x=5
myFunction2(x)
print('Value of x after the function call is',x)

myFunction3() #here we changed the global variable so hereafter x value will change to 15
#there are 2 types of variables:
#Global Variable and Local Variables. 

