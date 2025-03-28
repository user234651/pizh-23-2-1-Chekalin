from abc import ABC, abstractmethod
from datetime import datetime
import json

class moneyTransfer(ABC):
    """Абстрактный базовый класс для всех типов денежных переводов"""
    def __init__(self, amount: float, sender: str, recipient: str):
        self._amount = amount  # защищенное поле
        self._sender = sender
        self._recipient = recipient
        self.__creationDate = datetime.now()  # приватное поле
        self._status = "Created"  # защищенное поле
    
    @abstractmethod
    def execute(self) -> None:
        """Абстрактный метод выполнения перевода"""
        pass
    
    def logAction(self, action: str) -> None:
        """Защищенный метод для логирования действий"""
        print(f"[Журнал] {datetime.now()}: {action}")
    
    def generateReport(self) -> dict:
        """Приватный метод для генерации отчета"""
        return {
            "type": self.__class__.__name__,
            "amount": self._amount,
            "sender": self._sender,
            "recipient": self._recipient,
            "date": self.__creationDate.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self._status
        }
    
    def showReport(self) -> None:
        """Общедоступный метод для отображения отчета"""
        report = self.generateReport()
        print("Отчет о переводе:")
        print(json.dumps(report, indent=2, ensure_ascii=False))
    
    @property
    def status(self) -> str:
        """Свойство для получения статуса"""
        return self._status

class bankTransfer(moneyTransfer):
    """Класс для банковских переводов""" 
    def __init__(self, amount: float, sender: str, recipient: str, bank: str):
        super().__init__(amount, sender, recipient)
        self.__bank = bank
        self.__accountNumber = None
    
    def execute(self) -> None:
        """Реализация выполнения банковского перевода"""
        self.__accountNumber = f"ACC{datetime.now().timestamp()}"
        self._status = "Processing"
        self.logAction(f"Банковский перевод на сумму {self._amount}")
        
        # Имитация обработки перевода
        print(f"Банковский перевод через {self.__bank} выполняется...")
        print(f"Счет получателя: {self.__accountNumber}")
        self._status = "Completed"
        print("Банковский перевод успешно выполнен!")

class postalTransfer(moneyTransfer):
    """Класс для почтовых переводов"""
    def __init__(self, amount: float, sender: str, recipient: str, address: str):
        super().__init__(amount, sender, recipient)
        self.__address = address  # приватное поле
        self.__trackingCode = None  # приватное поле
    
    def execute(self) -> None:
        """Реализация выполнения почтового перевода"""
        self.__trackingCode = f"POST{datetime.now().timestamp()}"
        self._status = "Sent"
        self.logAction(f"Почтовый перевод на сумму {self._amount}")
        
        print(f"Почтовый перевод на адрес {self.__address} отправлен...")
        print(f"Код отслеживания: {self.__trackingCode}")
        
        self._status = "Delivered"
        print("Почтовый перевод успешно доставлен!")

class currencyTransfer(moneyTransfer):
    """Класс для валютных переводов"""
    def __init__(self, amount: float, sender: str, recipient: str, currency: str, rate: float):
        super().__init__(amount, sender, recipient)
        self.__currency = currency
        self.__exchangeRate = rate
        self.__operationId = None
    
    def execute(self) -> None:
        """Реализация выполнения валютного перевода"""
        self.__operationId = f"FX{datetime.now().timestamp()}"
        self._status = "Converting"
        self.logAction(f"Валютный перевод на сумму {self._amount} {self.__currency}")
        
        amountInRub = self._amount * self.__exchangeRate
        print(f"Конвертация {self._amount} {self.__currency} по курсу {self.__exchangeRate}...")
        print(f"Итого: {amountInRub:.2f} RUB")
        
        self._status = "Completed"
        print("Валютный перевод успешно выполнен!")
    
    def showExchangeRate(self) -> None:
        """Дополнительный метод для отображения курса"""
        print(f"Текущий курс {self.__currency}: {self.__exchangeRate}")