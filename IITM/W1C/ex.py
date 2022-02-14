#Break Continue and Pass

'''
#xyz123@iitm.in
email=input('Enter the email ID:')
for c in email:
  if(c=='@'):
    break
  print(c,end='')
'''

'''
#xyz123@iitm.in
email=input('Enter the email ID:')
for c in email:
  if(c=='@'):
    print('')
    continue
  print(c,end='')
'''


#PASS:
#categorise numbers from 1-10 into divisible by 3 and not divisible by three

for i in range(11):
  if(i%3 == 0):
    print(i)
  else:
    pass
    #just a place holder and it performs no operation: its a null statement in coding. 
  