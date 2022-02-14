#Nested loops

#Find the length of longest word from the set of Words entered by the user
'''
input                              output
                    
IITM online degree  -1              6
Bachelors of Science -1             9
Computational Thinking -1           13 
Introduction to the Python -1       12
'''

word=input('Enter the word:')
maxlen=0
while(word != '-1'):
  count=0
  for c in word:
    count=count+1
  if(count > maxlen):
    maxlen = count
  word = input('Enter the word:')
print('the length of longest word is:',maxlen)





