#Functions Introduction
'''
def add(a,b):
  ans=a+b
  print (ans)
#Here we have created our own functions. We have defined what should do what. 

def sub(a,b):
  ans=a-b
  print(ans)

def discount(cost,d):
  ans=cost-(cost*(d/100))
  print(ans)

'''

def add(a,b):
  ans=a+b
  return ans

a=5
b=6
print(add(a,b))
#comes to print >> Cals function add and goes to see what have you defined >> what is and b puts and then returns ans

def discount(cost,d):
  ans= cost-(cost*(d/100))
  return ans

x=int(input('Enter the cost'))
y=int(input('ENter the discount'))

print('The final price is',discount(x,y))