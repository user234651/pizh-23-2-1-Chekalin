```markdown
# Класс BeeElephant

Реализация гибрида пчелы и слона на Python.

## Методы класса

### `__init__(bee_part, elephant_part)`
Конструктор класса. Инициализирует объект с заданными пропорциями.

**Параметры:**
- `bee_part` (int) - начальная часть пчелы (0-100)
- `elephant_part` (int) - начальная часть слона (0-100)

**Пример:**
```python
be = BeeElephant(30, 70)
```

### `fly() -> bool`
Определяет способность существа летать.

**Возвращает:**
- `True` - если часть пчелы ≥ части слона
- `False` - в противном случае

**Логика:**
```python
return self.bee_part >= self.elephant_part
```

**Пример:**
```python
print(be.fly())  # False (30 < 70)
```

### `trumpet() -> str`
Издает характерный звук существа.

**Возвращает:**
- `"tu-tu-doo-doo!"` - если часть слона ≥ части пчелы
- `"wzzzzzz"` - в противном случае

**Логика:**
```python
if self.elephant_part >= self.bee_part:
    return "tu-tu-doo-doo!"
else:
    return "wzzzzzz"
```

**Пример:**
```python
print(be.trumpet())  # "tu-tu-doo-doo!"
```

### `eat(meal: str, value: int) -> None`
Изменяет пропорции существа в зависимости от пищи.

**Параметры:**
- `meal` - тип пищи:
  - `"nectar"` - увеличивает часть пчелы
  - `"grass"` - увеличивает часть слона
- `value` - величина изменения

**Логика:**
```python
if meal == "nectar":
    self.elephant_part -= value
    self.bee_part += value
elif meal == "grass":
    self.elephant_part += value
    self.bee_part -= value

# Ограничение значений
self.bee_part = max(0, min(self.bee_part, 100))
self.elephant_part = max(0, min(self.elephant_part, 100))
```

**Пример:**
```python
be.eat('nectar', 20)
print(be.get_parts())  # [50, 50]
```

### `get_parts() -> list[int]`
Возвращает текущие пропорции существа.

**Возвращает:**
- Список `[bee_part, elephant_part]`

**Логика:**
```python
return [self.bee_part, self.elephant_part]
```

**Пример:**
```python
print(be.get_parts())  # [30, 70]
```
```