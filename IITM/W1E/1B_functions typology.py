#Basics of Functions:

def add(a,b,c): # abc are called parameters
#function definition starts with def
  return(a+b+c)#for execution return statement- pass to where the function is called like to below line

print(add(20,30,40))
#function call
#arguments= values passed with function call=20 30 40



#Keywords= these are 2nd type of function arguments
#so in case we need more simplicity
print(add(a=20,b=30,c=40))
#so here the position or the sequence of arguments does not matter and also the parameters. 
#number of parameters and arguments must be same and then we get errors.

  return add(a,b=30,c=40))
print(20)
#in above case it will execute even when we have one argument for 3 parameters since there is only one parameter which has no value


# if return is replaced by print then the output will show none after every execution
#print is a function you call while return is a Keyword
#when return is called the python stops execution of current function and returns the value out to where the function was called. 
#if we dont write return keyword the function implicity returns None! 
