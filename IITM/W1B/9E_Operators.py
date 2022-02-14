#we cannot use special characters like and or if in as variable name. 


#we cannot start variable name with float or integer however we can start it with string.
#example:
al_5 = 5
print(al_5)

#here 5_al will give error

roll=5
Roll=6
ROLL=7
print(roll, Roll, ROLL)


#Multiple assignment
x,y= 1,2
print(x,y)

xy= yz = zx = 10
print(xy,yz,zx)

#interchanging the variable
x,y = y,x
print(x,y)


#short hand operators
count=0
count= count+1
count= count+1
count= count+1
print(count)

#solution to above problem (short hand operators)

count=0
count+=1
count+=1
count+=1
print(count)

#also we can use -= or /= or *= for short hand operators


#special operators called in-operators
#application search engine. 

print('alpha'in'A variable name can only contain alpha-numeric characters and underscores')
#it search for alpha if yes then true
print('alpha'in'A variable can contain only letters')


#relational operators
m= 5
print(m)
print(1<m<10)
print(10<m<50)
print(m<10<m*10<100)
print(10>=m<=9)
print(5==m>4)






#deleting the variable
print(x)
del (x)
print (x)








