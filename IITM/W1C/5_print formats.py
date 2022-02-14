#trivial way of wriiting print function: or call it as formated way of writing print function
'''
num=int(input('Enter the number'))
for i in range(1,11):
  #print(num,'X',i,'=',num*i)
  #print(f'{num} x {i} = {num*i}')
  #everything in parantheses will count as varibale and outside it as comment. 
  print('{0}x{1}={2}'.format(num,i,i*num))
  print('%d x %d = %d' % (num,i,num*i))
'''

#lets say value of pi=22/7 

pi=22/7
print(pi)
print(f'The value of pi is {pi}')
print('The value of pi is {0}'.format(pi))
print('the value of pi is %f'%(pi))

#remeber .2f will give the value of pi to two decimal places only
print(f'The value of pi is {pi:.2f}')
print('The value of pi is {0:.2f}'.format(pi))
print('the value of pi is %.2f'%(pi))

print('\n')

print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))
#this :5d ensures that the minimum digit length is 5
