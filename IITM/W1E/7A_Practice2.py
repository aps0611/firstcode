#Write a python code using the functions to calculate the area and perimeter of circle and rectangle. 
#Here the speciality about the code is that it is menu driven. 
#area
#perimeter

import math
PI=math.pi


def circle_area(r):
  area= PI*(r**2)
  return area

def circle_perimeter(r):
  perimeter= 2*PI*r
  return perimeter

def rectangle_area(l,b):
  area= l*b
  return area

def rectangle_perimeter(l,b):
  perimeter=(2*l)+(2*b)
  return perimeter

#We need to write the menu driven code:

polygon=''
while(polygon!='exit'):
  print('\nPolygons: \nCircle\nRectangle\nExit:')
  polygon=input('Choose the polygon type or exit:')

  property=''
  if polygon=='Circle':
    r=float(input('Enter the radius of circle'))
    while(property==''):  
      print('\nProperty\nArea or \nPerimeter')
      property=input('Please Enter property or go back:')
      if property=='Area':
        print('The area of circle is',circle_area(r))
      elif property=='Perimeter':
        print('The perimeter of circle is',circle_perimeter(r))
      elif property=='back':
        break
      else:
        print('Please select the correct property or exit')
        property=''

  elif polygon=='Rectangle':
    l=float(input('Enter the length of rectangle: '))
    b=float(input('Enter the breadth of rectangle: '))
    property=''
    while (property==''):
      print('\nPlease select the property either as Area or Perimeter')
      property=input('Please Enter the property:')
      if property=='Area':
        print('The area of rectangle is :',rectangle_area(l,b))
      elif property=='Perimeter':
        print('The perimeter of rectangle is:', rectangle_perimeter(l,b))
      elif property=='back':
        break
      else:
        Print('Enter the property or go back')
        property =''
        
  elif polygon=='exit':
    break
  else:
    print('Please select a correct polygon type or exit')



