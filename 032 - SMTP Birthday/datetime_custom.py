# 5/06/2024
# Day - 032

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1991, month=2, day=14, hour=23)
print("Date of birth:", date_of_birth)

print(f'\nNow: {now}')
print(f'Type: {type(now)}')

print(f'\nYear: {year}')
print(f'Type: {type(year)}')

if year == 2024:
    print("\n\n*** Coronaviryus is ovah ***")