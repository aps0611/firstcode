#Concept: how mod can be used in looping

alpha='abcdefghijklmnopqrstuvwxyz'
i=len(alpha)
print(i)
print('\n')

'''print(alpha[i])
print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+3])'''


print(i%26)
print('\n')

print(alpha[i%26])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26])
#so the loop continues after 26 letters again goes to a



