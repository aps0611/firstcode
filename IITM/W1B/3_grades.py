#find the grades of students based on given marks from 0 to 100


mrk=int(input('Enter the percentage: '))
if(mrk>=0 and mrk<=100):
  if(mrk>=90):
    print('A')
  if(80<=mrk<90):
    print('B')
  if(70<=mrk<80):
    print('C')
  if(60<=mrk<70):
    print('D')
  if(mrk<60):
    print('E')
else:
  print('invalid')











