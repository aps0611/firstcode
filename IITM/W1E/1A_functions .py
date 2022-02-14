#Warmup on functions

def list_min(l):
  mini=l[0]
  for i in range(len(l)):
    if (l[i]<mini):
      mini=l[i]
  return mini

l=[5,8,6,8,4,2,-1]
print (list_min(l))

def list_max(l):
  maxi=l[0]
  for i in range(len(l)):
    if(l[i]>maxi):
      maxi=l[i]
  return maxi

print(list_max(l))


def list_appendbefore(l,z):
  newl=[]
  for i in range(len(z)):
    newl.append(z[i])
  for i in range(len(l)):
    newl.append(l[i])
  return newl

def list_append(l,z):
  newl=[]
  for i in range(len(l)):
    newl.append(l[i])
  for i in range(len(z)):
    newl.append(z[i])
  return newl


z=[10,20,30]
print(list_appendbefore(l,z))
print(list_append(l,z))

#Find the average of enteries of list l

def list_avg(l):
  sum=0
  for i in range(len(l)):
    sum = sum + l[i]
  ans= sum/len(l)
  return ans

print(list_avg(l))




