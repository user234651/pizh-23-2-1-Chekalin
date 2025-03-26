import json
from datetime import datetime, timedelta

class Date:
    def __init__(x, day: int, month: int, year: int):
        x.validateDate(day, month, year)
        x._day = day
        x._month = month
        x._year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(x, value):
        x.validateDate(value, x._month, x._year)
        x._day = value

    @property
    def month(x):
        return x._month

    @month.setter
    def month(x, value):
        x.validateDate(x._day, value, x._year)
        x._month = value

    @property
    def year(x):
        return x._year

    @year.setter
    def year(x, value):
        x.validateDate(x._day, x._month, value)
        x._year = value

    def validateDate(x, day, month, year):
        if not (1 <= month <= 12):
            raise ValueError("Месяц должен быть от 1 до 12")
        
        maxDays = 31
        if month in [4, 6, 9, 11]:
            max_days = 30
        elif month == 2:
            maxDays = 29 if x.isLeapYear(year) else 28
        
        if not (1 <= day <= maxDays):
            raise ValueError(f"День должен быть от 1 до {maxDays} для месяца {month}")

    def isLeapYear(x, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __str__(x):
        return f"{x._day:02d}.{x._month:02d}.{x._year}"

    def __repr__(x):
        return f"Date({x._day}, {x._month}, {x._year})"

    def __add__(x, y):
        if isinstance(y, int):
            newDate = x.toDatetime() + timedelta(days=y)
            return Date.fromDatetime(newDate)
        raise TypeError("Можно добавлять только целое число дней")

    def __sub__(x, y):
        if isinstance(y, Date):
            delta = x.toDatetime() - y.toDatetime()
            return delta.days
        elif isinstance(y, int):
            newDate = x.toDatetime() - timedelta(days=y)
            return Date.fromDatetime(newDate)
        raise TypeError("Можно вычитать только Date или целое число дней")

    def __eq__(x, y):
        if not isinstance(y, Date):
            return False
        return x._day == y.day and x._month == y.month and x._year == y.year

    def __lt__(x, y):
        if not isinstance(y, Date):
            raise TypeError("Можно сравнивать только с объектом Date")
        return (x._year, x._month, x._day) < (y.year, y.month, y.day)

    def __gt__(x, y):
        if not isinstance(y, Date):
            raise TypeError("Можно сравнивать только с объектом Date")
        return (x._year, x._month, x._day) > (y.year, y.month, y.day)

    def toDatetime(x):
        return datetime(x._year, x._month, x._day)

    @classmethod
    def fromDatetime(cls, dt):
        return cls(dt.day, dt.month, dt.year)

    @classmethod
    def fromString(cls, strValue):
        try:
            day, month, year = map(int, strValue.split('.'))
            return cls(day, month, year)
        except (ValueError, AttributeError):
            raise ValueError("Строка должна быть в формате 'dd.mm.yyyy'")

    def save(x, filename):
        data = {
            'day': x._day,
            'month': x._month,
            'year': x._year
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls(data['day'], data['month'], data['year'])

    def weekday(x):
        return x.toDatetime().weekday()

    def leapYear(x):
        return x.isLeapYear(x._year)

    def addDays(x, days):
        newDate = x.toDatetime() + timedelta(days=days)
        return Date.fromDatetime(newDate)

    def daysUntil(x, otherDate):
        if not isinstance(otherDate, Date):
            raise TypeError("Параметр должен быть объектом Date")
        return (otherDate.toDatetime() - x.toDatetime()).days