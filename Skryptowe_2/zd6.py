import datetime

today = datetime.datetime.today().date()
#today = datetime.datetime(2022, 12, 30).date()
date_end_year = datetime.datetime(today.year, 12, 31).date()
print(today)
print(date_end_year)
delta = date_end_year - today
print(delta.days)

print()

today = datetime.datetime.today()
date_end_year = datetime.datetime(today.year, 12, 31)
delta = date_end_year - today
print(today)
print(date_end_year)
print(delta)