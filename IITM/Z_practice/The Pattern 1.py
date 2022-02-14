n=int(input('Enter the number of rows'))
k1=0
#n represents the number of rows
for i in range(n,0,-1):
  for j in range(i,0,-1):
    print('X',end=' ')
  print('\n')
  k1=k1+1
  for k in range(k1):
    print(' ',end='')
