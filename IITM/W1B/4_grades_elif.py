#find the grades of students based on given marks from 0 to 100


mrk=int(input('Enter the percentage: '))
if(mrk>=0 and mrk<=100):
  if(mrk>=90):
    print('A')
  elif(mrk>=80):
    print('B')
  elif(mrk>=70):
    print('C')
  elif(mrk>=60):
    print('D')
  elif(mrk<60):
    print('E')
else:
  print('invalid')











