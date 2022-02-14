#Obvious sort with functions:

#find out the minimum element in the list l
#append that to new list l
#remove the minimum from the original list l

def min_list(l):
  min=l[0]
  for i in range(len(l)):
    if l[i]< min:
      min=l[i]
  return min

def obvious_sort1(l):
  x=[]
  while (len(l)>0):
    min=min_list(l)
    x.append(min)
    l.remove(min)
  return x

def obvious_sort2(l):
  x=[]
  while(len(l)>0):
    min=l[0]
    for i in range(len(l)):
      if l[i]<min:
        min=l[i]
    x.append(min)
    l.remove(min)
  return x

l=[90,23,45,74,65]
print(obvious_sort1(l))
print(obvious_sort2(l))



