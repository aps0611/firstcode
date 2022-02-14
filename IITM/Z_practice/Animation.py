import time, sys
indent = 0 #How many spaces to indent
indentIncreasing=True #whether indentation is increasing or not?

try:
    while True:
        print(' '* indent, end='')
        print('********')
        time.sleep(0.1) #pause for 1/10th of second. 
        if indentIncreasing:
            #increase the number of spaces
            indent= indent +1
            if indent == 20: 
                indentIncreasing = False
        else:
            #decrease the number of space
            indent = indent -1
            if indent ==0:
                indentIncreasing= True #Change directione
except KeyoardInterrupt:
    sys.exit()

