import time
import calendar

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)
print(time.localtime())
localtime = time.localtime(time.time())
print("Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

month = calendar.month(2018, 6)
print(month)