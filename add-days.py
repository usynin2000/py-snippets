from datetime import datetime, timedelta


def add_days(n: int, date: datetime) -> datetime:
    return date + timedelta(n)


print(add_days(3, datetime.now()))
print(add_days(-30, datetime.now()))

# Calculates the date of n days from the given date.
#
# Use datetime.timedelta and the + operator to calculate the new datetime.datetime value after adding n days to d.
# Omit the second argument, d, to use a default value of datetime.today().