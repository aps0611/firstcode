#Sort using the recurrsion: 


def min(l):
  min=l[0]
  for x in l:
    if (x<min):
      min=x
  return min

def sort(l):
  ''' Recursively sort the list'''
  if (l==[]) or len(l)==1:
    return l
  
  m=min(l)
  l.remove(m)
  return [m] + sort(l)


