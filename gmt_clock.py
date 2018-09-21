#Eric Wright
#9/18

import calendar
import time

def gmtnow():
    seconds = calendar.timegm(time.gmtime())
    current_second = seconds % 60
    minutes = seconds // 60
    current_minute = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24
    return current_hour, current_minute, current_second

x = True
while x == True:
    h, m, s = gmtnow()
    print(h, ":", m, ":", s)
    time.sleep(1)