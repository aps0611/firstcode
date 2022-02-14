#practice  #STRING METHODS

x='ABHINAV SONONE IS A GOOD PERSON'
z= 'this IS a CIPHER'
w= '123456787'
v='123ac'
u='abc'
y='----rajaseth----'


print(x.lower())
print(z.lower())
print(z.upper())
print('\n')

#Capitalize only capitalizes the first letter and keeps small the remaining part. 
print(x.capitalize())
print('\n')

#title converts the first letter of every word in Sentence:
print(x.title())
print('\n')

#Swapcase
print(v.swapcase())
print(z.swapcase())
print('\n')

#islower and isupper or is title
print(x.islower())
print(x.isupper())
print(x.istitle())
print('\n')

#is digit alpha and is alnum
print('Digit alpha and alnum')
print(w.isdigit())
print(u.isalpha())
print(v.isalnum())
#remember in isalpha() there has to be no space to return space while if there is space it returns false. 
print('\n')

#Strip case l and r strips
print(y.strip('-'))
print(y.lstrip('-'))
print(y.rstrip('-'))
print('\n')

print(x.startswith('A'))
print(x.startswith('a'))
#remember here that the string is case sensitive
print(x.endswith('e'))
print('\n')

#measuring the length = the revision
print(len(x))
print(x[0])
print('\n')

#counting the digits
print(x.count('A'))
print(x.index('A'))
#it indexes only the first come first serve basis
print(x.replace('A','a'))
#replace all and not only the first come first serve
print(x.replace('x[0]','a'))
#check this with someone why is it not possible?






