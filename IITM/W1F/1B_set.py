#Set
#In set and dict both have curly brackets. But set do not allow duplicate value
s={1,2,3,4,5,6,1,1,1}
print(s,type(s))
#Set objets are not subscriptile s[0] and has no order
#set is peculiar. Set itself is mutable but every value inside is immutable and hashable. Can add values inside set but whatever we add has to be immutable. Hence we cannot add a list or a dictionary or a tuple containing list in a set. 

#iterate over a set yes.

#Set Methods:
#support all the operations that we usually perform using Mathematical sets. 

A={1,2,3,4,5,6,7,8,9}
B={1,2,3,}
C={9,10,11}
print(A.issubset(B))
print(A.issuperset(B))

C1= A.union(B)
print('C1',C1)
C2=A|B #See Operator
print('C2',C2)

C3= A.intersection(B)
print('C3',C3)
C4=A&B
print('C4',C4)

C5= A.difference(B)
C6=A-B
print(C5,C6)

# A+B not allowed in set
# A*5 Not allowed in set
