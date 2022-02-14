#Dictionary Data Structure

d={}
#PCM Marks
d['abhinav']=[99,96,98]
d['ramya']=[81,87,85]
d['ravi']=[75,65,52]
print(d)

print(d['abhinav'][0])#Marks secured by abhinav in P
#to make it more complicated
d['abhinav']=[98,85,45,'abhinav@gmail.com']
d['ramya']=[81,87,85,'ramya@123']
d['ravi']=[75,65,52,'ravi@245']
print(d)

print(d['abhinav'][3]) #It will give me my email address