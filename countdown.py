import datetime

def getNextYear(now: datetime.datetime, date: datetime.datetime) -> int:
    '''Returns the next year if this year's date has passed'''
    if now.month >= date.month and now.day >= date.day:
        return now.year + 1
    else:
        return now.year

#If the day is the specified date, return the next year
assert(getNextYear(datetime.datetime(2020, 12, 25, 12, 0, 0), datetime.datetime(2020, 12, 25, 12, 0, 0)) == 2021)
#Specified date year does not matter, only month and day
assert(getNextYear(datetime.datetime(2020, 12, 26, 12, 0, 0), datetime.datetime(2000, 12, 25, 12, 0, 0)) == 2021)
#If the day is before the specified date, return same year 
assert(getNextYear(datetime.datetime(2020, 1, 1, 12, 0, 0), datetime.datetime(2021, 12, 25, 12, 0, 0)) == 2020)
#If the day is after the specified date, return next year
assert(getNextYear(datetime.datetime(2020, 12, 30, 12, 0, 0), datetime.datetime(2020, 12, 25, 12, 0, 0)) == 2021)

def getDaysUntil(date: datetime.datetime) -> int:
    '''Calculates the days until the given date'''
    now = datetime.datetime.now()
    year = getNextYear(now, date)
    date = datetime.datetime(year, date.month, date.day)
    delta = date - now
    return delta.days
    