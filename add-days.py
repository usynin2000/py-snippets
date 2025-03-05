from datetime import datetime, timedelta

import calendar


def add_days(n: int, date: datetime) -> datetime:
    return date + timedelta(n)



def format_date_to_str(date: datetime) -> str:
    return date.strftime("%H:%M:%S %d.%m.%Y")
    # can be any format u need
    # %y-%Y depends on what format u need 25 or 2025
    # %h or %m Feb or 02 as a mounth


def format_str_to_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%H:%M:%S %d.%m.%Y")

def get_difference(date1: datetime, date2: datetime) -> timedelta:
    return date2 - date1

def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)

def get_weekday(date: datetime) -> str:
    return date.strftime("%A")

def get_timestamp_from_datetime(dt: datetime) -> int:
    return int(dt.timestamp())


def get_from_timestamp_to_datetime(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp)

def from_string_datetime_to_timestamp(date_str: str) -> int:
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    return int(dt.timestamp())


if __name__ == "__main__":
    date = datetime.now()
    print(add_days(3, date))
    print(add_days(-30, date))


    print(format_date_to_str(date))

    date_str = format_date_to_str(date)

    print(format_str_to_date(date_str))

    date2 = datetime(2025, 3, 5)

    print(get_difference(date, date2))

    print(is_leap_year(2024))
    print(is_leap_year(2025))

    print(get_weekday(datetime.now()))
    print(get_timestamp_from_datetime(date))

    timestamp = get_timestamp_from_datetime(date)
    print(get_from_timestamp_to_datetime(timestamp))

    date_str = "2025-03-05T13:35:39"
    print(from_string_datetime_to_timestamp(date_str))