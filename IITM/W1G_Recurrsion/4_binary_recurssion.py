#Code for binary search using the recursive:
#remember this list we will use in this function is already sorted.

def rbinarysearch(l,k,begin,end):
  
  if (begin==end): #only one element
    if(l[begin]==k):
      return 1
    else:
      return 0

  if (end-begin==1): #2 elements
    if(l[begin]==k) or (l[end]==k):
      return 1
    else:
      return 0
    
  if (end-begin>1): 
    mid=(begin+end)//2
    if(l[mid]>k):
      #discard the right and retain the left
      end=mid-1
    if(l[mid]<k):
      #discrad the left and retain the right
      begin=mid+1
    if(l[mid]==k):
      return 1

  if (end-begin<1):
    return 0

  return rbinarysearch(l,k,begin,end)




#Recurrsion cannot go on and on it has some limits called recurrsion depth. 
#~999 in python
