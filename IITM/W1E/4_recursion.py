#Introduction to Recurrsion
#theme:
#sum(n)= sum(n-1)+n
#fact(n)=fact(n-1)*n

#Code to find our sum of n numbers:

n=10
ans=0
for i in range(n):
  ans=ans+(i+1)
print(ans)

#lets create a function for above program
def sum(n):
  ans=0
  for i in range(n):
    ans= ans+(i+1)
  return ans

#Recurssion in python:

def sum(n):
  if(n==1):
    return 1
  else:
    return n+sum(n-1)

#Python lets you call same function within same function
#assume interet rate is 10%
def compound_interest(p,t):
  #Verified
  if(t==1):
    return p*(1.1)
  else:
    return (compound_interest(p,t-1))*1.1

def fact(n):
  if(n==1):
    return 1
  else:
    return n*fact(n-1)

