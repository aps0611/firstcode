#This is called as ceasar cipher in cryptography
#for Any string I give shift the index by 1 and give next string for example for india I want

alpha= 'abcdefghijklmnopqrstuvwxyz'
l=len(alpha)
print(l, type(l))

s=str(input('please Enter the Question'))
t=len(s)
print(t, type(t))

#I am taking input lets say abhinav here
#I need to index by 1 and get an output bcijobw

i=0
k=1
ans=' '

print('\n')
#print(alpha[((alpha.index(s[i])+k)%26)])

while(i!=t):
  ans= ans+ (alpha[((alpha.index(s[i])+k)%26)])
  #ans= ans + str(print(alpha[((alpha.index(s[i])+k)%26)]))
  i=i+1
 # print(type(ans))

print('The answer to cipher is',ans)
#shift by 2 units

'''
print(alpha[((alpha.index(s[i])+k)%26)])
t=t+(alpha[((alpha.index(s[i])+k)%26)])
t=t+(alpha[((alpha.index(s[i+1])+k)%26)])
t=t+(alpha[((alpha.index(s[i+2])+k)%26)])
t=t+(alpha[((alpha.index(s[i+3])+k)%26)])
t=t+(alpha[((alpha.index(s[i+4])+k)%26)])

print(t)
'''