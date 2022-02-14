#This is called as ceasar cipher in cryptography

alpha= 'abcdefghijklmnopqrstuvwxyz'

s= 'india'
#i want to print 

t=''

i=0

k=2
#shift by 2 units


print(alpha[((alpha.index(s[i])+k)%26)])
t=t+(alpha[((alpha.index(s[i])+k)%26)])
t=t+(alpha[((alpha.index(s[i+1])+k)%26)])
t=t+(alpha[((alpha.index(s[i+2])+k)%26)])
t=t+(alpha[((alpha.index(s[i+3])+k)%26)])
t=t+(alpha[((alpha.index(s[i+4])+k)%26)])

print(t)
