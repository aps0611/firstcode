#String Slicing

s='My Name is Abhinav'

print(s[1:5])
#by default the step is one and it goes from one to n-1

#This will print it reverse no matter what!
print(s[::-1])

print(s[0:-3])
#for ease: python says dont count from start you can even count from the last i.e. -1 -2 -3

print(s[3:10:2])
#here we gave the step of 2

print(s[1:50])
#This will not show any Indexing Error. Slicing is only iteration operation and not directly retrieving any particular index. 


print(s[-1:5:-1])
#this will print from -1th element to 5th element in reverse order with decrement of 1