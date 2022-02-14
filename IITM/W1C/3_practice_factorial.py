#While loop Exercise
#problem1

n=int(input('enter the number:'))

#5=5*4*3*2*1
#a=a*1
#a=a*2

#a=a*i

i=1
a=1

if(n>=0):
  while(i<=n):
    a=a*i
    i=i+1
  print('factorial of',n,'is',a)
else:
  print('Not defined')
