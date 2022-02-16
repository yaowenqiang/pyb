import datetime

d = datetime.date(2015, 7, 20)



print(d)

today = datetime.date.today()

print(today)



print(today.day)

print(today.weekday())
print(today.isoweekday())

timedelta = datetime.timedelta(days=7)

print(today + timedelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2



bday = datetime.date(1987, 7,7)

till_bday = bday - today
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())



t = datetime.time(9, 30, 45, 100000)

print(t)

print(t.hour)



dt = datetime.datetime(1978, 7, 7, 0,0,0)
print(dt)


print(dt.date())
print(dt.time())


datetimedelta = datetime.timedelta(days=7, hours=4)
print(dt + datetimedelta)