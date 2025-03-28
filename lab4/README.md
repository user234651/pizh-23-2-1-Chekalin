```markdown
# Банковские вклады и работа с датами

Два независимых Python-проекта: система банковских вкладов и класс для работы с датами.

## 1. Банковские вклады 🏦

### Классы вкладов

#### Базовый класс `bankDeposit`
```python
class bankDeposit:
    def __init__(self, name, minAmount, currency, periodMonths, rate):
        self.name = name
        self.minAmount = minAmount
        self.currency = currency
        self.periodMonths = periodMonths
        self.rate = rate
```

#### `termDeposit` - срочный вклад
**Методы:**
- `calculateProfit(amount)` - расчет прибыли по простым процентам
- `__str__()` - строковое представление условий

**Формула:**

Прибыль = (сумма × ставка × срок в месяцах) / 12


#### `BonusDeposit` - бонусный вклад
**Дополнительные параметры:**
- `bonusThreshold` - порог для бонуса
- `bonusRate` - процент бонуса от прибыли

**Особенности:**
- Начисляет базовую прибыль как termDeposit
- Добавляет бонус если сумма ≥ bonusThreshold

#### `capDeposit` - вклад с капитализацией
**Формула:**

Прибыль = сумма × (1 + ставка/1200)^срок - сумма


### Класс `depositAdvisor`
**Функционал:**
- Содержит список доступных вкладов
- `find_best_deposit(amount, currency, period)` - поиск оптимального вклада
- `showAllDeposits()` - отображение всех вкладов

### Пример использования
```python
advisor = depositAdvisor()
result = advisor.find_best_deposit(100000, "RUB", 12)
if result:
    deposit, profit = result
    print(f"Рекомендуем: {deposit.name}, прибыль: {profit} RUB")
```

## 2. Класс для работы с датами 📅

### Основной функционал класса `Date`

#### Инициализация
```python
d = Date(15, 5, 2023)  # 15.05.2023
d = Date.fromString("15.05.2023")
d = Date.fromDatetime(datetime.now())
```

#### Валидация
- Автоматическая проверка корректности даты
- Учет високосных годов

#### Операции с датами
```python
# Добавление дней
new_date = date + 10

# Разница между датами
days = date1 - date2

# Сравнение
if date1 > date2: ...
```

#### Полезные методы
- `weekday()` - день недели (0-6)
- `leapYear()` - проверка високосного года
- `daysUntil(otherDate)` - дней до указанной даты
- `addDays(days)` - новая дата через N дней

#### Сериализация
```python
date.save("date.json")  # сохранение
loaded = Date.load("date.json")  # загрузка
```

### Пример использования
```python
date = Date(1, 1, 2023)
print(date + 30)  # 31.01.2023
print(date.weekday())  # 6 (воскресенье)
```

## Требования
- Python 3.6+
- Для работы с датами: стандартная библиотека (datetime, json)

## Лицензия
MIT
```
```markdown
# Класс Date для работы с датами

Полнофункциональный класс для работы с датами на Python с валидацией, арифметическими операциями и сериализацией.

## 📌 Основные возможности

- Полная валидация дат (учет високосных годов, корректность дней в месяце)
- Арифметические операции с датами
- Сравнение дат
- Конвертация в/из datetime
- Сериализация в JSON
- Расчет разницы между датами
- Определение дня недели

## 🛠 Инициализация объекта

```python
# Тремя числами (день, месяц, год)
date1 = Date(15, 5, 2023)

# Из строки формата "dd.mm.yyyy"
date2 = Date.fromString("15.05.2023")

# Из объекта datetime
date3 = Date.fromDatetime(datetime.now())

# Загрузка из JSON файла
date4 = Date.load("date.json")
```

## 🔍 Свойства (properties)

```python
date = Date(15, 5, 2023)
date.day = 20    # Установка дня с валидацией
date.month = 6   # Установка месяца с валидацией
date.year = 2024 # Установка года с валидацией
```

## ➕ Арифметические операции

```python
# Добавление дней к дате
new_date = date + 10  # 25.05.2023

# Вычитание дней из даты
past_date = date - 15  # 30.04.2023

# Разница между датами в днях
days_diff = date1 - date2

# Сохранение в файл
date.save("my_date.json")
```

## 🔄 Методы преобразования

```python
# Преобразование в datetime
dt = date.toDatetime()

# Преобразование в строку
date_str = str(date)  # "15.05.2023"

# Получение дня недели (0-6, понедельник-воскресенье)
weekday = date.weekday()
```

## 📅 Полезные методы

```python
# Проверка на високосный год
is_leap = date.leapYear()

# Добавление дней с возвратом новой даты
new_date = date.addDays(30)

# Количество дней до другой даты
days_until = date.daysUntil(target_date)
```

## ⚠️ Валидация

Автоматически проверяет:
- Корректность месяца (1-12)
- Корректность дня для каждого месяца
- Високосные года для февраля

```python
try:
    invalid_date = Date(31, 4, 2023)  # Вызовет ValueError
except ValueError as e:
    print(e)  # "День должен быть от 1 до 30 для месяца 4"
```

## 📊 Сравнение дат

```python
date1 = Date(1, 1, 2023)
date2 = Date(15, 1, 2023)

date1 < date2   # True
date1 == date2  # False
date1 > date2   # False
```

## 💾 Сериализация

```python
# Сохранение даты в JSON файл
date.save("date.json")

# Загрузка даты из JSON файла
loaded_date = Date.load("date.json")
```

## 🏗 Пример использования

```python
today = Date.fromDatetime(datetime.now())
vacation_start = Date(1, 7, 2023)
days_until_vacation = today.daysUntil(vacation_start)

print(f"До начала отпуска: {days_until_vacation} дней")
```

## 📝 Особенности реализации

- Все операции возвращают новые объекты Date (иммутабельность)
- Полная поддержка pickle-сериализации через JSON
- Интеграция со стандартным datetime
- Подробные сообщения об ошибках валидации

## ⚠️ Ограничения

- Поддерживаются только григорианские даты
- Минимальная единица - день (без часов/минут)
- Диапазон годов ограничен возможностями datetime