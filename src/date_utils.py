from datetime import datetime


def check_leap_year(year: int):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False


def check_hired_greater_than_3year(hired: datetime):
    current = datetime.now()
    diff_year = current.year - hired.year
    if diff_year >= 3:
        return True

    days_per_month = 366 / 12 if check_leap_year(hired.year) else 365 / 12
    current_days = (days_per_month * current.month) + current.day
    hired_days = (days_per_month * hired.month) + hired.day
    if current_days - hired_days == 0:
        return True

    return False


if __name__ == "__main__":
    print(check_hired_greater_than_3year(datetime.strptime("2020-10-09", "%Y-%m-%d")))
