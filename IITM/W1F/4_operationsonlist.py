#Operation on lists:

l1=[1,2,3]
l2=[10,20,30]
l12=l1+l2
l21=l2+l1
print(l12,l21)


m1=[0,0,0,0,0,0,0,0,0,0]
print(m1)
#Way to avoid everytime putting 0 in list
m2=[0]*10
print(m2)
m3=[1,2,3]*5
print(m3)

n1=[1,2,3]
n2=[1,2,3]
n3=[3,2,1]
print(n1==n2)
print(n2==n3)#false since sequence is wrong
#copares values as well as sequence

print(n1<n2)
print(n1<n3)
#element at n[0]compared with m[0]
print('\n')
print([1,2]<[2,1])
print([1]<[1,2,3])
print([2,3]<[3])
print([]<[1])

#update list in place= Mutability
p=[1,2,4]
print(p)
p[2]=3
print(p)

q='abcd'
print(q[0])#output=a
#however if we do q[0]=e it wont be changed since string are not mutable

u1= [1,2,3]
u2= u1
u1[0]=100
print(u1,u2) #here both show 100 Why?
#O/p: [100, 2, 3] [100, 2, 3]
#In list computer behaves in different manner: does not create new memory location but just adds one more name to u1 as u2. So if any single value changed in u1[i] will have changed value in u2[i]

#need different memory locations see three different ways below:

l1=[1,2,3]
#1
l2=list(l1)
#2
l3=l1[:]
#3
l4=l1.copy()

l2[0]=100
l3[1]=200
l4[2]=300
print(l1,l2,l3,l4)
l5=l1

#How to figure out whether 2 different variables are pointing at same memory location or at 2 different memory locations

print(l1 is l2)
print(l1 is l3)
print(l1 is l4)
print(l1 is l5)#True as it has same memory location

def add(x):
  x=x+1#local value 6
  return x

x=5#Global
print(add(x))
print(x)

#now list
def addd(x):
  x.append(1)
  return x

x=[5]
print(addd(x))
print(x)
#here we are not passing the value of but we pass the variable x itself. It is called call by reference.
#If function argument is mutable type it is called by reference wherease in case of integer it was called by value

#list Methods

z=[1,2,3]
print(z)
z.append(400)#at last
z.insert(2,100)#inserts 100 at 2nd index
print(z)
z.remove(2)#deletes particular element 2
print(z)
z.pop(0)#deletes element at index 0
print(z)

z1=z.copy()
print(z1)

z.sort()
print(z)
z.reverse()
print(z)



