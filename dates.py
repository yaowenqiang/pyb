import datetime
import pytz

# pip install pytz
# pip install arrow

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
print(dt.year)


datetimedelta = datetime.timedelta(days=7, hours=4)
print(dt + datetimedelta)


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)




dt_2 = datetime.datetime(2022,2,27, 11,10, 0, tzinfo=pytz.UTC)

print(dt_2)
dt_now_2 = datetime.datetime.now(tz=pytz.UTC)
print(dt_now_2)
dt_utcnow_2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow_2)


dt_mtn = dt_utcnow_2.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)



# for tz in pytz.all_timezones:
# 	print(tz)




dt_mtn_2 = datetime.datetime.now()


print(dt_mtn_2)




mtn_tz = pytz.timezone('US/Mountain')

dt_mtn_2 = mtn_tz.localize(dt_mtn_2)
print(dt_mtn_2)

dt_east = dt_mtn_2.astimezone(pytz.timezone('US/Eastern'))

print(dt_east)




print(dt_mtn_2.isoformat())
print(dt_mtn_2.strftime('%B %d, %Y'))

dt_str = 'February 17, 2022'

dt_from_str = datetime.datetime.strptime(dt_str, '%B %d, %Y')

print(dt_from_str)