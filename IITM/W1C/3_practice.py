#While loop Exercise: count th digits

n=abs(int(input('Enter the number:')))
#absolute function will convert the negative to positive sign

i=1

while(n>9):
  n=n//10
  i=i+1

print(i)
  
#1234

