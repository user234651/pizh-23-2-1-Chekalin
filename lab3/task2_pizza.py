class Pizza:
    def __init__(x):
        x.name = "Базовая пицца"
        x.dough = "обычное тесто"
        x.sauce = "кетчуп"
        x.toppings = []
        x.price = 0

    def prepare(x):
        print(f"Готовим {x.name}:")
        print(f" - замешиваем {x.dough} тесто")
        print(f" - добавляем {x.sauce} соус")
        print(" - добавляем начинку:", ", ".join(x.toppings))

    def bake(x):
        print("Выпекаем пиццу... Готово!")

    def cut(x):
        print("Нарезаем пиццу на 8 кусочков")

    def pack(x):
        print("Упаковываем пиццу в фирменную коробку")

    def __str__(x):
        return f"{x.name} ({x.price} руб.)"


class Pepperoni(Pizza):
    def __init__(x):
        super().__init__()
        x.name = "Пепперони"
        x.dough = "тонкое"
        x.sauce = "томатный"
        x.toppings = ["пепперони", "сыр моцарелла", "орегано"]
        x.price = 450


class Barbecue(Pizza):
    def __init__(x):
        super().__init__()
        x.name = "Барбекю"
        x.dough = "толстое"
        x.sauce = "барбекю"
        x.toppings = ["курица", "бекон", "лук", "сыр чеддер"]
        x.price = 550


class Seafood(Pizza):
    def __init__(x):
        super().__init__()
        x.name = "Дары моря"
        x.dough = "тонкое"
        x.sauce = "сливочный"
        x.toppings = ["креветки", "мидии", "лосось", "сыр пармезан"]
        x.price = 650


class Order:
    orderCounter = 0
    def __init__(x):
        Order.orderCounter += 1
        x.orderNumber = Order.orderCounter
        x.pizzas = []

    def addPizza(x, pizza):
        x.pizzas.append(pizza)

    def calculateTotal(x):
        return sum(pizza.price for pizza in x.pizzas)

    def execute(x):
        for pizza in x.pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()
        print(f"Заказ #{x.orderNumber} готов!")

    def __str__(x):
        if not x.pizzas:
            return "Заказ пуст"
        pizzasList = "\n".join(f" - {pizza}" for pizza in x.pizzas)
        return f"Заказ #{x.orderNumber}:\n{pizzasList}\nИтого: {x.calculateTotal()} руб."


class Terminal:
    def __init__(x):
        x.menu = [
            Pepperoni(),
            Barbecue(),
            Seafood()
        ]
        x.currentOrder = None

    def showMenu(x):
        print("Меню пиццерии:")
        for i, pizza in enumerate(x.menu, 1):
            print(f"{i}. {pizza}")

    def createOrder(x):
        x.currentOrder = Order()
        print("Создан новый заказ")

    def processCommand(x, choice):
        try:
            choice = int(choice)
            if 1 <= choice <= len(x.menu):
                selected_pizza = x.menu[choice - 1]
                x.currentOrder.addPizza(selected_pizza)
                print(f"Добавлено: {selected_pizza.name}")
            else:
                print("Некорректный номер пиццы")
        except ValueError:
            print("Пожалуйста, введите номер пиццы")

    def acceptPayment(x):
        if not x.currentOrder or not x.currentOrder.pizzas:
            print("Нет активного заказа")
            return False

        total = x.currentOrder.calculateTotal()
        print(f"К оплате: {total} руб.")
        
        while True:
            payment = input("Введите сумму для оплаты: ")
            try:
                payment = float(payment)
                if payment >= total:
                    if payment > total:
                        print(f"Ваша сдача: {payment - total} руб.")
                    print("Оплата принята. Спасибо!")
                    return True
                else:
                    print("Недостаточно средств")
            except ValueError:
                print("Пожалуйста, введите число")

    def run(x):
        print("Добро пожаловать в пиццерию!")
        x.showMenu()
        x.createOrder()

        while True:
            print("\n1. Добавить пиццу")
            print("2. Подтвердить заказ")
            print("3. Отменить заказ")
            choice = input("Выберите действие: ")

            if choice == "1":
                x.showMenu()
                pizza_choice = input("Выберите пиццу: ")
                x.processCommand(pizza_choice)
            elif choice == "2":
                if not x.currentOrder.pizzas:
                    print("Заказ пуст. Добавьте пиццу.")
                    continue
                print("\nВаш заказ:")
                print(x.currentOrder)
                if x.acceptPayment():
                    x.currentOrder.execute()
                    break
            elif choice == "3":
                print("Заказ отменен")
                break
            else:
                print("Некорректный выбор")


if __name__ == "__main__":
    terminal = Terminal()
    terminal.run()