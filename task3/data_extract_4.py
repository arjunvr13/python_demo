# Write a Python program to extract year, month, date and time using Lambda.
import datetime
x = datetime.datetime.now()
now = lambda x : x
year = lambda x : x.year
month = lambda x : x.month
day = lambda x : x.day
time = lambda x : x.time()
print(now(x))
print(year(x))
print(month(x))
print(day(x))
print(time(x))
