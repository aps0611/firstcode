#find whether given number is divided by 5 or 10 or any other number


num=int(input('Enter the number:'))
if(num%5==0):
  if(num%10==0):
    print ('divisile by 10 and 5')
  else:
    print('Divisible by 5')
else:
  print('other number')











