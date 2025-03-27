import json
from datetime import datetime, timedelta

class Date:
    """Класс Дата"""
    def __init__(x, day: int, month: int, year: int):
        x.validateDate(day, month, year)
        x._day = day
        x._month = month
        x._year = year

    @property
    def day(self):
        """Метод, возвращающий день"""
        return self._day

    @day.setter
    def day(x, value):
        """Метод, присваивающий объекту day значение"""
        x.validateDate(value, x._month, x._year)
        x._day = value

    @property
    def month(x):
        """Метод, возвращающий месяц"""
        return x._month

    @month.setter
    def month(x, value):
        """Метод, присваивающий объекту month значение"""
        x.validateDate(x._day, value, x._year)
        x._month = value

    @property
    def year(x):
        """Метод, возвращающий год"""
        return x._year

    @year.setter
    def year(x, value):
        """Метод, присваивающий объекту year значение"""
        x.validateDate(x._day, x._month, value)
        x._year = value

    def validateDate(x, day, month, year):
        """Метод проверки того, подходит ли число"""
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
        """Метод проверки, является ли год високосным"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __str__(x):
        return f"{x._day:02d}.{x._month:02d}.{x._year}"

    def __repr__(x):
        return f"Date({x._day}, {x._month}, {x._year})"

    def __add__(x, y):
        """Метод сложения дат"""
        if isinstance(y, int):
            newDate = x.toDatetime() + timedelta(days=y)
            return Date.fromDatetime(newDate)
        raise TypeError("Можно добавлять только целое число дней")

    def __sub__(x, y):
        """Метод вычитания дат"""
        if isinstance(y, Date):
            delta = x.toDatetime() - y.toDatetime()
            return delta.days
        elif isinstance(y, int):
            newDate = x.toDatetime() - timedelta(days=y)
            return Date.fromDatetime(newDate)
        raise TypeError("Можно вычитать только Date или целое число дней")

    def __eq__(x, y):
        """Метод сравнения дат"""
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
        """Метод возвращения даты в формате datetime"""
        return datetime(x._year, x._month, x._day)

    @classmethod
    def fromDatetime(cls, dt):
        """Метод извлечения даты из переменной в формате datetime"""
        return cls(dt.day, dt.month, dt.year)

    @classmethod
    def fromString(cls, strValue):
        """Метод извлечения даты из строки"""
        try:
            day, month, year = map(int, strValue.split('.'))
            return cls(day, month, year)
        except (ValueError, AttributeError):
            raise ValueError("Строка должна быть в формате 'dd.mm.yyyy'")

    def save(x, filename):
        """Метод, помещающий дату в файл json"""
        data = {
            'day': x._day,
            'month': x._month,
            'year': x._year
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load(cls, filename):
        """Метод загрузки даты из файла json"""
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls(data['day'], data['month'], data['year'])

    def weekday(x):
        """Метод, определяющий день недели"""
        return x.toDatetime().weekday()

    def leapYear(x):
        """Метод проверки года на високосность"""
        return x.isLeapYear(x._year)

    def addDays(x, days):
        """Метод прибавления дней к дате"""
        newDate = x.toDatetime() + timedelta(days=days)
        return Date.fromDatetime(newDate)

    def daysUntil(x, otherDate):
        """Метод, определяющий количество дней до даты"""
        if not isinstance(otherDate, Date):
            raise TypeError("Параметр должен быть объектом Date")
        return (otherDate.toDatetime() - x.toDatetime()).days