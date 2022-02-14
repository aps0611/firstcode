#Dictionary Data Structure

d={}

d['abhinav']=9765574852
d['ramya']=5689451256
d['ravi']=8945562345
print(d)
print(d['abhinav'])

#What use is dictionary then?

malgudi=['It','was','a','good', 'day','Yesterday','it','will','be','a','good','day','tommorow','And','day','after','tommorow']
print (malgudi)

s=set(malgudi)
print(s)

for x in malgudi:
  print (x)


#Initialixe dictionary
d={}
for x in s:
  d[x]=0
#So, it give 'string':0 for all the strings in d
print(d)
max=0
answer_word=''
for x in malgudi:
  d[x]=d[x]+1
  if(d[x]>max):
    max=d[x]
    answer_word=x
print(d)
print (max)
print(answer_word)


