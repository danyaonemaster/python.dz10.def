import calendar
import random


def random_month():
    return random.randrange(1, 12)


def random_day(month):
    _, days = calendar.monthrange(2024, month)
    return random.randrange(1, days)


compare = {
    calendar.JANUARY:
        "Winter",
    calendar.FEBRUARY:
        "Winter",
    calendar.MARCH:
        "Spring",
    calendar.APRIL:
        "Spring",
    calendar.MAY:
        "Spring",
    calendar.JUNE:
        "Summer",
    calendar.JULY:
        "Summer",
    calendar.AUGUST:
        "Summer",
    calendar.SEPTEMBER:
        "Autumn",
    calendar.OCTOBER:
        "Autumn",
    calendar.NOVEMBER:
        "Autumn",
    calendar.DECEMBER:
        "Winter",
}
month_no = random_month()
month_name = calendar.month_name[month_no]
day_no = random_day(month_no)
season = compare[month_no]
print(f"month : {calendar.month_name[month_no]}\n"
      f"day : {day_no}\n"
      f"year season : {season}")
