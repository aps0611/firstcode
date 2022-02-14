#iterator and next

number = [1,4,5,6,7]

n1= iter(number)
'''
print(next(n1))
print(next(n1))
print(next(n1))
'''
while True :
  try:
    element =next(n1)
    print(element)
  except StopIteration:
    break




