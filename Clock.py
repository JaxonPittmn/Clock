import os
import time

month = int(input("What month is it (Use Number): "))
day = int(input("What day of the month is it (Use Number): "))
year = int(input("What year is it: "))
if(year % 4 == 0 and year % 100!= 0 or year % 400 == 0):
  leapyear = True
hour = int(input("What hour is it: "))
am_or_pm = int(input("Is it am[0] or pm[1]: "))
minutes = int(input("What minute is it: "))
seconds = int(input("What second is it: "))

os.system('clear')

if hour == 12:
  twelve_exact = True
else:
  twelve_exact = False

while True:
  if month % 2 == 1 and month != 2 and month != 8:
    days_in_month = 30
  elif month % 2 == 0 and month != 2 or month == 8:
    days_in_month = 31
  elif leapyear == False and month == 2:
    days_in_month = 28
  elif leapyear and month == 2:
    days_in_month = 29

  if am_or_pm == 0:
    timeframe = "AM"
  else:
    timeframe = "PM"
  seconds += 1
  if seconds == 60:
    minutes += 1
    seconds = 0
  if minutes == 60:
    hour += 1
    minutes = 0
  if hour == 12:
    if twelve_exact == False:
      check_timeframe = am_or_pm % 2
      if check_timeframe == 0:
        am_or_pm = 1
      else:
        am_or_pm = 0
        day += 1
    twelve_exact = True
  else:
    twelve_exact = False
  if day > days_in_month:
    month += 1
    day = 1
  if month > 12:
    month = 1
    year += 1

  print(f"{month}/{day}/{year} | {timeframe} | {hour}:{minutes}:{seconds}")
  time.sleep(1)
  os.system('clear')