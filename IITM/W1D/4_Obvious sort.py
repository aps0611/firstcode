l=[12,56,84,65,79,52,8]
#say no to l.sort

#Pick the least element then put it in x and then remove from l. Revisiting the sort traditional way. 

x=[]


while(len(l)>0):
  min=l[0]
  for i in range(len(l)):
    if l[i]<min:
      min=l[i]
  x.append(min)
  l.remove(min)

print(l)
print(x)


