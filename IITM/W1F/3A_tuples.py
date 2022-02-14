#Tuples More on it
#Tuple is immutable


#packing
t=1,2,3
print(t,type(t))

#Unpacking
x,y,z= t
print(x,y,z,type(x))

u=5
v=10
u,v=v,u #unpacking onleft hand side
print(u,v)

l=[10]
print(l,type(l))

t=(11)
print(t,type(t)) #class int? interesting part of tuple. 
#When only one element is inside it is intiger

t=(11,) #put comma
print(t,type(t))

w=([10,20],['a','b'])
print(w,type(w))
#can we change values inside list inside tuple?= Yes
w[0][0]=100
print(w)
#Tuple immutability principle does not stop us from modifying value inside list. Values inside list inside tuple can be modified: It is called hashable. 

t1=(1,2,3) #hashable= values inside are immutable
t2=([1,2,3],)#non-hasable= values inside are mutable


