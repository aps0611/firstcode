#lists and sets:

'''
l=list(range(100000))
print(l)
s=set(range(10))
print(s)
x=list(range(10))
print(x)
t=set(range(100000))
print(t)
'''
#Speed at which set says True or False is fast compared to the Speed of list.
'''

                  List               Set
Search            Not easy           easy
size              Small              Large
subscriptable     yes[]              No  
functionality     in(lookup)         in   
Data              Ordered            Unordered Unique
Nested list       yes                Not possible

'''

import random
import math
import sys
import numpy

l=[]
l1=[0]
l2=[0,2]

x=list(range(100))
y=set(range(100))
#use command sys.getsizeof() to calculate the size

#s[0] we cannot call this as list does. all are the elements of a set and you cannot arrange them on specific number.

#Data Structures: Need to study to understand this better.