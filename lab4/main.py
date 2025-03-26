from task2_class import Date
from datetime import datetime

def testDateClass():
    # Создание объектов
    d1 = Date(15, 5, 2023)
    d2 = Date.fromString("20.05.2023")
    d3 = Date.fromDatetime(datetime.now())
    
    # Тестирование методов
    print(d1)
    print(d2)
    
    # Операции
    print(d2 - d1)
    d4 = d1 + 10
    print(d4)
    
    # Сравнение
    print(d1 < d2)  # True
    print(d1 == d2)  # False
    
    # Сохранение/загрузка
    d1.save("date.json")
    loaded = Date.load("date.json")
    print(loaded == d1)  # True
    
    # Дополнительные методы
    print(f"День недели: {d1.weekday()}")  # 0 (понедельник)
    print(f"Високосный год: {d1.leapYear()}")  # False
    print(f"Дней между датами: {d1.daysUntil(d2)}")  # 5

if __name__ == "__main__":
    testDateClass()