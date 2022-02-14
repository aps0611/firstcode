#import calendar library
'''
import calendar

#print(calendar.month(2021,11))
print(calendar.calendar(2021))

'''

#bring everything inside calendar library into python program so that we dont need to write everytime the calndar.calendar or calendar.month

'''
from calendar import *
#print(calendar(2021))
print(month(2021,11))

'''

#DOnt give computer unecessary trouble by bringing everything thus,

'''
from calendar import month, calendar
#print(month(2021,11)) 
print(calendar(2021))
'''

from calendar import month as m

print(m(2021,11))




