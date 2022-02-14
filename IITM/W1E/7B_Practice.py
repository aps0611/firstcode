#Write a python code using the function that checks whether the input co-ordinates form a triangle or not.

#acc:ept the variables (x1y1) (x2y2) (x3y3)


#Not verified thus can be wrong
def distance(xi,yi,xj,yj):
  dist= (((xj-xi)**2)+((yj-yi)**2)**0.5)
  return dist

def isTriangle(max,a,b):
  if ((a+b)>max):
    print('Triangle')
  else:
    print('\n not a triangle')

x1= float(input('Enter x1:'))
y1= float(input('Enter y1:'))
x2= float(input('Enter x2:'))
y2= float(input('Enter y2:'))
x3= float(input('Enter x3:'))
y3= float(input('Enter y3:'))

d1=distance(x1,y1,x2,y2)
d2=distance(x2,y2,x3,y3)
d3=distance(x1,y1,x3,y3)
  
print(f'\n Distance between ({x1},{y1}) and ({x2}{y2}) is {d1}')
print(f'\n Distance between ({x2},{y2}) and ({x3}{y3}) is {d2}')
print(f'\n Distance between ({x1},{y1}) and ({x3}{y3}) is {d3}')

if (d1>d2):
  if(d1>d3):
    isTriangle(d1,d2,d3)
  else:
    isTriangle(d3,d1,d2)
elif(d2>d3):
  isTriangle(d2,d1,d3)
else:
  isTriangle(d3,d2,d1)


