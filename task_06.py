import calendar
import random


def random_month():
    return random.randrange(1, 12)


def random_day(month: int):
    _, days = calendar.monthrange(2024, month)
    return random.randrange(1, days)


simbols = [
    "Capricorn",  # 0
    "Aquarius",
    "Pisces",
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius"
]

compare = {
    calendar.JANUARY:
        lambda date: simbols[calendar.JANUARY - 1] if date < 20 else simbols[calendar.JANUARY],
    calendar.FEBRUARY:
        lambda date: simbols[calendar.FEBRUARY - 1] if date < 19 else simbols[calendar.FEBRUARY],
    calendar.MARCH:
        lambda date: simbols[calendar.MARCH - 1] if date < 21 else simbols[calendar.MARCH],
    calendar.APRIL:
        lambda date: simbols[calendar.APRIL - 1] if date < 20 else simbols[calendar.APRIL],
    calendar.MAY:
        lambda date: simbols[calendar.MAY - 1] if date < 21 else simbols[calendar.MAY],
    calendar.JUNE:
        lambda date: simbols[calendar.JUNE - 1] if date < 21 else simbols[calendar.JUNE],
    calendar.JULY:
        lambda date: simbols[calendar.JULY - 1] if date < 23 else simbols[calendar.JULY],
    calendar.AUGUST:
        lambda date: simbols[calendar.AUGUST - 1] if date < 23 else simbols[calendar.AUGUST],
    calendar.SEPTEMBER:
        lambda date: simbols[calendar.SEPTEMBER - 1] if date < 23 else simbols[calendar.SEPTEMBER],
    calendar.OCTOBER:
        lambda date: simbols[calendar.OCTOBER - 1] if date < 23 else simbols[calendar.OCTOBER],
    calendar.NOVEMBER:
        lambda date: simbols[calendar.NOVEMBER - 1] if date < 22 else simbols[calendar.NOVEMBER],
    calendar.DECEMBER:
        lambda date: simbols[calendar.DECEMBER - 1] if date < 20 else simbols[calendar.DECEMBER],
}

month_no = random_month()
month_name = calendar.month_name[month_no]
day_no = random_day(month_no)
sign = compare[month_no](day_no)
print(f"month : {calendar.month_name[month_no]}\n"
      f"day : {day_no}\n"
      f"zodiac sign : {sign}")
