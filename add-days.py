from datetime import datetime, timedelta


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




if __name__ == "__main__":
    date = datetime.now()
    print(add_days(3, date))
    print(add_days(-30, date))


    print(format_date_to_str(date))

    date_str = format_date_to_str(date)

    print(format_str_to_date(date_str))

    date2 = datetime(2025, 3, 5)

    print(get_difference(date, date2))