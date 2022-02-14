#Matrix Multiplication using the functions:
#Functions help you stay Organised

#initialize C to zero
#Consider two matrices A and B
#Need to find dot product of 2 lists
#take ith row of A and jth column of B and then find our C[i][j]

#I want my C to become like [[000][000][000]]
def initialize_mat(dim):
#Code verified and works perfectly fine in test cases
  C=[]
  for i in range(dim):
    C.append([])
  for i in range(dim):
      for j in range(dim):
        C[i].append(0)
  return C

def dot_product(u,v):
  dim=len(u)
  ans=0
  for i in range(dim):
    ans=ans+(u[i]*v[i])
  return ans


def row(M,i):
  l=[]
  dim=len(M)
  for k in range(dim):
    l.append(M[i][k])
  return l

def col(M,j):
  dim=len(M)
  l=[]
  for k in range(dim):
    l.append(M[k][j])
  return l

def mat_mul(A,B):
  dim=len(A)
  C=initialize_mat(dim)
  for i in range(dim):
    for j in range(dim):
      #C[i][j]=ith row of A * jth column of B
      C[i][j]=dot_product(row(A,i),col(B,j))
  return C


#below is the Mentos jindagi
import numpy
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[10,11,12],[13,14,15],[16,17,18]]
A=numpy.mat(A)
B=numpy.mat(B)
C=A*B
print(C)


