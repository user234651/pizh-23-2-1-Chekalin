class bankDeposit:
    """Класс Депозита"""
    def __init__(self, name, minAmount, currency, periodMonths, rate):
        self.name = name
        self.minAmount = minAmount
        self.currency = currency
        self.periodMonths = periodMonths
        self.rate = rate  # годовая процентная ставка

    def calculateProfit(self, amount):
        """Метод подсчёта прибыли, переопределяется в дочерних классах"""
        raise NotImplementedError("Метод должен быть реализован в подклассах")

    def getConditions(self):
        """Метод, возвращающий статус программы"""
        return (f"{self.name}\n"
                f"Минимальная сумма: {self.minAmount:,} {self.currency}\n"
                f"Срок: {self.periodMonths} мес.\n"
                f"Ставка: {self.rate}% годовых")


class termDeposit(bankDeposit):
    """Срочный депозит"""
    def calculateProfit(self, amount):
        """Метод подсчёта прибыли"""
        if amount < self.minAmount:
            raise ValueError(f"Минимальная сумма для вклада {self.minAmount} {self.currency}")
        
        # Простые проценты: P = (P0 * r * t) / (12 * 100)
        profit = (amount * self.rate * self.periodMonths) / 12
        return round(profit, 2)

    def __str__(self):
        return self.getConditions() + "\nТип начисления: простые проценты"


class BonusDeposit(bankDeposit):
    """Бонусный депозит"""
    def __init__(self, name, minAmount, currency, periodMonths, rate, bonusThreshold, bonusRate):
        super().__init__(name, minAmount, currency, periodMonths, rate)
        self.bonusThreshold = bonusThreshold
        self.bonusRate = bonusRate  # % от прибыли

    def calculateProfit(self, amount):
        """Метод подсчёта прибыли"""
        if amount < self.minAmount:
            raise ValueError(f"Минимальная сумма для вклада {self.minAmount} {self.currency}")
        
        # Сначала считаем как обычный срочный вклад
        baseProfit = (amount * self.rate * self.periodMonths) / 12
        
        # Добавляем бонус если сумма превышает порог
        if amount >= self.bonusThreshold:
            bonus = baseProfit * (self.bonusRate / 100)
            baseProfit += bonus
        
        return round(baseProfit, 2)

    def __str__(self):
        return (self.getConditions() + 
                f"\nБонус: {self.bonusRate}% от прибыли при сумме > {self.bonusThreshold:,} {self.currency}")


class capDeposit(bankDeposit):
    """Депозит капитализации"""
    def calculateProfit(self, amount):
        """Метод подсчёта прибыли"""
        if amount < self.minAmount:
            raise ValueError(f"Минимальная сумма для вклада {self.minAmount} {self.currency}")
        
        # Сложные проценты с ежемесячной капитализацией:
        # P = P0 * (1 + r/(12*100))^n
        monthlyRate = self.rate / 12 / 100
        totalAmount = amount * (1 + monthlyRate) ** self.periodMonths
        profit = totalAmount - amount
        return round(profit, 2)

    def __str__(self):
        return self.getConditions() + "\nТип начисления: с капитализацией процентов"


class depositAdvisor:
    """Класс подбора депозита"""
    def __init__(self):
        self.deposits = [
            termDeposit("Срочный+", 10_000, "RUB", 12, 6.5),
            BonusDeposit("Бонусный", 50_000, "RUB", 12, 5.8, 100_000, 10),
            capDeposit("Капитализация", 20_000, "RUB", 12, 6.0),
            termDeposit("Надежный", 5_000, "USD", 6, 3.2),
            capDeposit("Международный", 1_000, "EUR", 24, 4.5)
        ]

    def findBestDeposit(self, amount, currency, period):
        """Метод подбора депозита"""
        suitable = []
        for deposit in self.deposits:
            if (deposit.currency == currency and 
                deposit.periodMonths == period and 
                amount >= deposit.minAmount):
                try:
                    profit = deposit.calculateProfit(amount)
                    suitable.append((deposit, profit))
                except ValueError:
                    continue
        
        if not suitable:
            return None
        
        # Сортируем по убыванию прибыли
        suitable.sort(key=lambda x: x[1], reverse=True)
        return suitable[0]

    def showAllDeposits(self):
        """Метод показа меню депозитов"""
        print("Доступные вклады:")
        for i, deposit in enumerate(self.deposits, 1):
            print(f"{i}. {deposit}\n")


def main():
    """Точка входа в программу"""
    advisor = depositAdvisor()
    
    while True:
        print("\n1. Показать все вклады")
        print("2. Подобрать лучший вклад")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            advisor.showAllDeposits()
        elif choice == "2":
            try:
                amount = float(input("Введите сумму вклада: "))
                currency = input("Введите валюту (RUB/USD/EUR): ").upper()
                period = int(input("Введите срок (мес.): "))
                
                result = advisor.findBestDeposit(amount, currency, period)
                if result:
                    deposit, profit = result
                    print(f"\nРекомендуем вклад: {deposit.name}")
                    print(f"Ваша прибыль за период: {profit:,} {currency}")
                    print(f"Итоговая сумма: {amount + profit:,} {currency}")
                else:
                    print("Подходящих вкладов не найдено")
            except ValueError:
                print("Ошибка ввода данных")
        elif choice == "3":
            break
        else:
            print("Некорректный выбор")


if __name__ == "__main__":
    main()