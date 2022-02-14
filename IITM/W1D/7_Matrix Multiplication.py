#Matrix Multiplication-1

dim=3
r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

B=[]
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

C=[[0,0,0],[0,0,0],[0,0,0]]


#I need to multiply the Matrixes 
#C[i][j] is the dot product of ith row of A and jth column of B
#C[2][1] is the dot prouct of 2nd row of A and 1st columnB

for i in range(dim):
  for j in range(dim):
      for k in range(dim):

    #C[i][j]=dot product of A[i][...] and B[...][j]
        C[i][j]=C[i][j]+A[i][k]*B[k][j]

print(C)


#And then there is Lionel messi doing things differently:

'''
import numpy
X=numpy.mat(A)
Y=numpy.mat(B)
print(X*Y)
'''









