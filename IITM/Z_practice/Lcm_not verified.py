#failed program to find out the lcm

itr=int(input('How many numbers for LCM?: '))
l=[]
k=0
while(k<itr):
    num=int(input('Enter the number or exit: '))
    
    for i in range(2,num):
        #print('i',i)


        if num%i == 0:
            #print('i2',i)
            l.append(i)

    print(l)
    k=k+1

l.sort()
flag=False

while i<(len(l)-1):
    if l[i]==l[i+1]:
        flag True



