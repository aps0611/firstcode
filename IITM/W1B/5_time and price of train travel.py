#Converting the flowchart


#Travel from City A to City B

print('Travel from City A to City B')
time=int(input('Enter the time you are willing to travel:'))
long_time=int(input('Define long time: '))
if(time>= long_time):
  price=int(input('What price are you willing to pay?:'))
  high_p=int(input('Above what price will it be costly?:'))
  if(price>=high_p):
    print('Travel by Rajdhani')
  else:
    print('Travel by garib rath')
else:
  price=int(input('What price are you willing to pay?:'))
  high_p=int(input('Define high price base value:'))
  if(price>=high_p):
    print('Travel by UAE Royal flight')
  else:
    print('Travel by Air India with subsidy')

print('Enjoy the journey')












