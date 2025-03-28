import json
from typing import List, Union

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

class dateCollection:
    """Класс-контейнер для хранения набора объектов Date"""
    
    def __init__(self, dates: List['Date'] = None):
        """Инициализация контейнера"""
        self._data = dates if dates is not None else []
    
    def __str__(self) -> str:
        """Представление объекта в удобном для человека виде"""
        return f"Collection of {len(self._data)} dates: " + ", ".join(str(date) for date in self._data)
    
    def __getitem__(self, index: Union[int, slice]) -> Union['Date', 'dateCollection']:
        """Индексация и срез для класса-контейнера"""
        if isinstance(index, slice):
            return dateCollection(self._data[index])
        return self._data[index]
    
    def add(self, value: 'Date') -> None:
        """Добавляет элемент value в контейнер"""
        if not isinstance(value, Date):
            raise TypeError("Можно добавлять только объекты класса Date")
        self._data.append(value)
    
    def remove(self, index: int) -> None:
        """Удаляет элемент из контейнера по индексу index"""
        if not 0 <= index < len(self._data):
            raise IndexError("Индекс вне диапазона")
        del self._data[index]
    
    def save(self, filename: str) -> None:
        """Сохраняет объект в JSON-файл filename"""
        datesData = [{'day': date.day, 'month': date.month, 'year': date.year} for date in self._data]
        with open(filename, 'w') as f:
            json.dump(datesData, f)
    
    @classmethod
    def load(cls, filename: str) -> 'dateCollection':
        """Загружает объект из JSON-файла filename"""
        with open(filename, 'r') as f:
            datesData = json.load(f)
        dates = [Date(data['day'], data['month'], data['year']) for data in datesData]
        return cls(dates)
    
if __name__ == "__main__":
    # Создаем несколько объектов Date
    date1 = Date(1, 1, 2023)
    date2 = Date(15, 5, 2023)
    date3 = Date(31, 12, 2023)

    # Создание коллекции и добавление элементов
    collection = dateCollection()
    collection.add(date1)
    collection.add(date2)
    collection.add(date3)

    print("Коллекция после добавления:")
    print(collection)  # Используем __str__

    # Доступ по индексу и срезу
    print("\nПервая дата в коллекции:", collection[0])
    print("Последние две даты:", collection[1:3])  # Возвращает новую dateCollection

    # Удаление элемента
    collection.remove(1)  # Удаляем вторую дату
    print("\nКоллекция после удаления:")
    print(collection)

    # Сохранение в файл
    collection.save("dates.json")
    print("\nКоллекция сохранена в файл dates.json")

    # Загрузка из файла
    loadedСollection = dateCollection.load("dates.json")
    print("\nЗагруженная коллекция из файла:")
    print(loadedСollection)

    # Проверка работы __getitem__ с новыми датами
    print("\nПервый элемент загруженной коллекции:", loadedСollection[0])