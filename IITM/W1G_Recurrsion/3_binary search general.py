def obvious_search(l,k):
  #Check if the given element k is present in the list or not? and this function by authored my Mr A and is most simplest function in the world
  for x in l:
    if x==k:
      return 1
  return 0

#Can we write a code which can find the same results above but in short duration of time?

def binary_search(l,k):
  #I want to shrink my list.
  #lets do that using a while loop.

  begin=0 #index of first element in l l[0]
  end=len(l)-1 #last element index l[len(l)-1]

  #use while loop to look at the list and keep having it. 
  while((end-begin) > 1):
    #list has atleast 2 elements
    #we will handle the case when the number of elements is less than or equal to 1
    mid=(begin-end)//2

    
    if (l[mid]==k): #if mid is k then end
      return 1
    
    if(l[mid]>k): #if middle element is greater than k, then cut the right side and retian the left side
      end=mid-1
    
    if (l[mid]<k): #discrd left and retain the right side
      begin=mid+1

#this is outside the while loop that means while is either violated or we havent found the element. 
#this means end-begin is -1 or 0 or something different

#if it is equal to one then there are two element in the region of interest. 

  
  if (l[begin]==k) or (l[end]==k):
    return 1
  else:
    return 0

#Technique you use is the technology!!