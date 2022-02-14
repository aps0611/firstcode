#to find factorial of a number


n=int(input('enter the number'))

#n=5
#n!= 5*4*3*2*1

#answer=1
#answer=answer*2
#answer=answer*3
#answer=answer*4
#answer=answer*5


i=1
ans=1

#while(i!=(n+1)) can use this also

while(i<=n): #less than or equal to
  ans=ans*i
  i=i+1
  

print(ans)
