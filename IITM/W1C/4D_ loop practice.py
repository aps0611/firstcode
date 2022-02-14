num=(abs(int(input('Enter the number you wish: ')))

'''
#tutorial on for loop and difference between for and while loop

#factorial example:

#num=5 then 5*4*3*2*1


fact=1

for i in range(1,num+1,1):
  if(num==0):
   print(fact)
  else:
    fact=fact*i 

print(fact)


#if we are certain about the range then go for loop
#if we are not certain about the range we need to go with while loop
#for example when calculatin the number of digits. Since here we are not sure about the range or number of iterations.

digit=1
if(num>9):
  while(num>9):
    num=num//10
    digit = digit+1
  print('digit',digit)
else:
  print(digit,'1')

#there is some problem in this check with someone:
#other way to solve this
strNum=str(num)
d=0
for c in strNum:
  d=d+1
  #means for every c i.e character in strnum c will have 1 value

print('\n') 
print(d)

'''
#reverse the digits in given number

'''
num=abs(int(input('Enter the number you wish: ')))

rev=num%10
num=num//10
while(num>0):
  r=num%10
  num=num//10
  rev=rev*10+r
print(rev)
'''


'''
string=str(num)
rev=''
for c in string:
  rev=c+rev
print(rev)

#calculating the number of digits
strNum=str(num)
d=0
for c in strNum:
  d=d+1
  #means for every c i.e character in strnum c will have 1 value

print('\n') 
print(d)

'''


#find whether the given number is pallindrome or not?
#12321

strNum=str(num)
rev=''
for c in strNum:
  rev=c+rev

if(num==rev):
  print('its palindrome')
else:
  print('its not')






