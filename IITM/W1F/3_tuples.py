#Tuples

t=(1,6,5,4,8,2,8)
print(t)
#cannot append or remove

'''

        tuple()               list[]
        Data Never change     Changeable
        i.e.Immutable
        less size             more size
        append yes            append yes

'''
#Application of Tuple: areas where we do not want the variables to be manipulated. For example: Email address or phone number etc.. 


t1=tuple(range(10))
print(t1)

import string
s=string.ascii_letters
print(s)
u=string.ascii_uppercase
print(u)
s=set(s)
print(s)

alpha=tuple(s)
print(alpha)
print(list(s))
x='sudarshanpundjjan#7*fjdkjaslkn%#$'
l=list(x)
print(l)

r=[]
for p in l:
  if p in alpha:#tuple is used for lookup
    r.append(p)
print(r)
#all the special symbols including space are removed

a=list(range(10))
b=tuple(range(10))
print(a)
print(b)
#a.__sizeof__()
#120
# b.__sizeof__()
#104


