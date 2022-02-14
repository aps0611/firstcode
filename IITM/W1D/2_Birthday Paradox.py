#The Birthday Paradox

import random

l=[]
#create an empty list.

for i in range(100):
  l.append(random.randint(1,365))
  #append random numbers between 1 to 365
  #append 30 of these

l.sort()
print(l)
#console:
#[12, 20, 39, 53, 85, 87, 95, 107, 111, 111, 113, 114, 117, 143, 147, 173, 189, 189, 216, 217, 224, 246, 275, 284, 291, 303, 306, 312, 316, 331]
#repetation
i=0
flag=0 #denotes that there is no repetation
while(i<len(l)-1):
  if(l[i]==l[i+1]):
    print('repeats',l[i],l[i+1])
    flag=1
  i=i+1

if (flag==0):
  print('there is no repetation')



