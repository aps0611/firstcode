
def test(name,mail_id):
  con= name + mail_id
  return mail_id, name


#lambda Function:

a=10
b=20

def test1(x,y):
  return x+y

#lambda is inbuild python function used to create an anonymous filter

m= lambda x,y : x + y
print(m(a,b))

print(m('sudh','xyz@amb'))
#Not advisable to use lambda generally and lambda is a keyword. 

p1= lambda a,b : print(a,b)
print(p1('as','so'))



