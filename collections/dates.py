#dates in pythons is tomort as datetime to work with dates as date objects
import datetime as dt
x=dt.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.strftime('%A'))
print(x.strftime('%a'))
print(x.strftime('%d'))
print(x.strftime('%B'))
print(x.strftime('%b'))
print(x.strftime('%C'))  #yaer divided by 100 and covert into int
print(x.strftime('%c'))
'''
import datetime
y=datetime.datetime.now()
print(y)
x=datetime.datetime(2025,10,10,9,45,36)
print(x)
print(x.strftime('%B'))
print(x.strftime('%C'))
print(x.strftime('%w'))
print(x.strftime('%d'))
print(x.strftime('%m'))
print(x.strftime('%y'))
print(x.strftime('%Y'))
print(x.strftime('%p'))
print(x.strftime('%I'))#12 hour clock
print(x.strftime('%H'))#24 hour clock
print(x.strftime('%f'))#micro seconds
print(x.strftime('%u'))# weekday(1-7)
print(x.strftime('%v'))#weeknumber(01-53)
'''
from datetime import date,datetime,timedelta
today=date(2024,1,15)
print(today,today.strftime('%A'))
now=datetime(2024,1,15,9,30)
print(now.strftime('%d %b %Y, %I:%M %p'))
