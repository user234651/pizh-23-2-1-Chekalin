class BeeElephant:
    """Класс Пчелослон"""
    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part

    def fly(self):
        """Метод, возвращающий True, если часть пчелы больше части слона"""
        return self.bee_part >= self.elephant_part

    def trumpet(self):
        """Метод, возвращающий True, если часть слона больше части пчелы"""
        if self.elephant_part >= self.bee_part:
            return "tu-tu-doo-doo!"
        else:
            return "wzzzzzz"

    def eat(self, meal, value):
        """Метод поедания, который изменяет соотношение пчелы и слона в зависимости от поедаемой пищи"""
        if meal == "nectar":
            self.elephant_part -= value
            self.bee_part += value
        elif meal == "grass":
            self.elephant_part += value
            self.bee_part -= value

        # Ограничение значений в пределах от 0 до 100
        self.bee_part = max(0, min(self.bee_part, 100))
        self.elephant_part = max(0, min(self.elephant_part, 100))

    def get_parts(self):
        """Метод, возвращающий соотношение пчелы и слона"""
        return [self.bee_part, self.elephant_part]

print("Вариант 9")
# Пример 1
be = BeeElephant(3, 2)
print(be.fly())  # True
print(be.trumpet())  # wzzzzzz
be.eat('grass', 4)
print(be.get_parts())  # [0, 6]

# Пример 2
be = BeeElephant(13, 87)
print(be.fly())  # False
print(be.trumpet())  # tu-tu-doo-doo!
be.eat('nectar', 90)
print(be.trumpet())  # wzzzzzz
print(be.get_parts())  # [100, 0]