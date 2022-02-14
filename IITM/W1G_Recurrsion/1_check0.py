#Introduction to Recurssion: 

#Find 0 in the list: 
l=[11,21,56,4,8,21,45,23,0,21,54]

#Check if the given list has zero in it or not. If it has zero in it we return true or else we return False


def check0(l): 
  if len(l)==0:
    return False
  if (l[0]==0): #base condition
    return True
  else:#outsource the rest of the list
    return check0(l[1:len(l)])

ans=check0(l)
print(ans)

#Please not this is not a good code lets see it later. 


