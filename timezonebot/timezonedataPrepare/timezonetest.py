from dateutil.tz import gettz
import datetime as dt
from pytz import timezone

print(gettz("Europe/Madrid"))
print("This is your local time")
print(dt.datetime.now().isoformat())

print("This is time zone of Europe/Marid")
print(dt.datetime.now(gettz("Europe/Madrid")).isoformat())

print("This is time zone of SIngapore")
print(dt.datetime.now(gettz("Singapore")).isoformat())

timeZone_Singapore = dt.datetime.now(gettz("Singapore")).isoformat()
print(type(timeZone_Singapore))

print("The date is: ")
print(timeZone_Singapore[0: 11])

print("The time is: ")
print(timeZone_Singapore[11: 19])

print("The Time zone is: ")
print(timeZone_Singapore[-6:])

city = ['America/Cayman']


tz = timezone('Australia/Sydney')
print(tz)