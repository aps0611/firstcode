#For loop examples
for i in range(1,11):
  print(i)

print('\n')
#ODD examples
for i in range(1,11):
  if (i%2!=0):
    print(i)
#here the default value for step is one for example see below
print('\n')

for i in range(1,11,1):
  if (i%2!=0):
    print(i)

print('\n')
#step (starting, end, step)
for i in range(1,11,2):
  print(i)

print('\n')
for i in range(0,12,2):
  print(i)

print('\n')
#To print the numbers in reverse order:
for i in range(10,-1,-1):
  print(i)

print('\n')
#for loop without using the range:
country= 'india'
for letter in country:
  print(letter)

'''
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])
'''


print('\n')
for i in range(10):
  print(i,end=' ')
#default value here is \n thus it prints in vertical fashion.
#here we explicitly tell the computer to overwrite the default value and consider this space '' as new value.

print('\n')

d=11
m=6
y=2021
print('todays date is',d,m,y)
print('todays date is:',end='')
print(d,m,y,sep='/')





