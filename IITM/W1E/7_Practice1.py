#Write a Python code using functions which calculate the number of upper case letters, lower case letters, total number of characters and numbber of words.

#Test Case
#Functions could have no parameters        1 29  34  5


sentence= str(input('Enter the Input: '))
 
def up_case_letter(s):
  upper=0
  for c in s:
    if (c.isupper()):
      upper= upper + 1
  return upper

def lower(s):
  lower=0
  for c in s:
    if (c.islower()):
      lower = lower + 1
  return lower

def total_character(s):
  char=0
  for c in s:
    char=char +1
  return char

def total_word(s):
  words=1#since end word will have no space
  for c in s:
    if(c==' '):
      words=words +1
  return words