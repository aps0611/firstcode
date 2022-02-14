#Dot Product

import random 
'''
l=random.sample(list(range(10000)),1000)
print(l)
sum=0
for i in range(len(l)):
  sum= sum + l[i]

print(sum)
'''

x=[1,2,3,4,3,5,6]
y=[8,5,6,7,8,9,4]

sum=0
for i in range(len(x)):
  sum=sum + x[i]*y[i]

print(sum)


