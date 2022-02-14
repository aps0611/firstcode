#Nested loops

#find all prime numbers less than entered number
'''
input               output
9                   2 3 5 7
15                  2 3 5 7 11 13
3                   2 
1                   no output
2                   no output
'''

n=int(input('Enter the number you wish: '))

if(n>2):
  print(2,end='')
for i in range(3,n+1):
  flag=False
  for j in range(2,i):
    if(i%j==0):
      flag=False
      break
    else:
      flag=True
  if(flag):
    print(i,end='')



