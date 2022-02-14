#while loop
# I would like to write a code that lets user to attempt as many times as he wants. 
#the code will end only when it gets the right answer
'''
year= int(input('when did India get its Independence?:'))

if(year==1947):
  print('yeta re tula')
else:
  print('shalela paise wapas mag ja')
  print('chal tula ekda wapas chance deto')
  print('bol bhava wapas')
  year= int(input('when did India get its Independence?:'))
  if(year==1947):
    print('yeta re tula')
  else:
    print('gandlaes bhava tu')


'''

#while loop:

year= int(input('when did India get its Independence?:'))

while(year!=1947):
  print('aee wapas tak')
  year= int(input('when did India get its Independence?:'))

print('lai hushar ahes re tu')

#while(condition)
  #write anything
  #take inputs again
  #write again
  #will work untill it goes to take correct answer