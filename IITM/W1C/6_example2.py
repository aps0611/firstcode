#Nested loops

#find all prime numbers less than entered number
'''
input                     output
5 days                    

10 15 19 5 -1             49
12 13 31 -1               56
57 32 85 47 82 -1         303
2 5 8 2 4 8 8 2 -1        39
-1                        0
'''

#a= 10+15+19+5= 49

days=int(input('Enter the number of days:'))
for i in range(1,days+1):
  total=0
  rainfall=int(input('Enter the rainfall:'))
  while(rainfall!=-1):
    total= total+rainfall
    rainfall=int(input('Enter the rainfall:'))
  print('Total rainfall for day{0}is {1}'.format(i,total))


