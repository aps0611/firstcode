#Naive Search

import random

l=[]

for i in range(10000):
  l.append(random.randint(1,1000000))
print(l)
a=0

while(a>-1):
  a=int(input('Enter the number, type -1 to exit:'))
  flag=0
  for i in range(len(l)):
    if(a==l[i]):
      print('Yo the number is present',a)
      flag=1
      break
      
  if (flag==0):
    print('Element not found')


