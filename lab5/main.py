from task2_hierarchy import bankTransfer, postalTransfer, currencyTransfer

if __name__ == "__main__":
    print("=== Тестирование банковского перевода ===")
    bank = bankTransfer(5000, "Иван Иванов", "Петр Петров", "Сбербанк")
    bank.execute()
    bank.showReport()
    print("Статус:", bank.status)
    
    print("\n=== Тестирование почтового перевода ===")
    postal = postalTransfer(3000, "Сергей Сидоров", "Алексей Кузнецов", "ул. Ленина, 123")
    postal.execute()
    postal.showReport()
    
    print("\n=== Тестирование валютного перевода ===")
    currency = currencyTransfer(100, "John Smith", "Анна Иванова", "USD", 75.5)
    currency.showExchangeRate()
    currency.execute()
    currency.showReport()