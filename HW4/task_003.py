# У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, выполняя следующие операции,
# для выполнения которых необходимо написать следующие функции:

# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта. withdraw(amount): Снятие денег. exit():
# Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

# Пополнение счета:
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
# Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
# Если сумма пополнения превышает RICHNESS_SUM, то начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

# Снятие средств:
# Функция withdraw(amount) позволяет клиенту снимать средства со счета.
# Сумма снятия также должна быть кратной MULTIPLICITY.
# При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

# Завершение работы:
# Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM,
# начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

# Проверка кратности суммы:
# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
# Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.

from decimal import Decimal, getcontext

# Установите точность для decimal
getcontext().prec = 10

# Константы
MULTIPLICITY = 10
RICHNESS_SUM = Decimal('10000.00')
RICHNESS_PERCENT = Decimal('0.05')
MIN_REMOVAL = Decimal('0.01')
MAX_REMOVAL = Decimal('0.1')


class BankAccount:
    def __init__(self):
        self.balance = Decimal('0.00')

    def check_multiplicity(self, amount):
        return amount % MULTIPLICITY == 0

    def deposit(self, amount):
        if self.check_multiplicity(amount):
            self.balance += amount
            if amount > RICHNESS_SUM:
                tax = amount * RICHNESS_PERCENT
                self.balance -= tax
                print(f"Налог на богатство: {tax}")
            print(f"Пополнение на сумму: {amount}")
        else:
            print("Ошибка: Сумма пополнения не кратна MULTIPLICITY")

    def withdraw(self, amount):
        if self.check_multiplicity(amount):
            if MIN_REMOVAL <= amount <= MAX_REMOVAL * self.balance:
                self.balance -= amount
                print(f"Снятие средств на сумму: {amount}")
            else:
                print("Ошибка: Сумма снятия вне диапазона или недостаточно средств")
        else:
            print("Ошибка: Сумма снятия не кратна MULTIPLICITY")

    def exit(self):
        if self.balance > RICHNESS_SUM:
            tax = self.balance * RICHNESS_PERCENT
            self.balance -= tax
            print(f"Налог на богатство при завершении: {tax}")
        print(f"Итоговый баланс: {self.balance}")


# Пример использования
account = BankAccount()
account.deposit(500)
account.withdraw(60)
account.deposit(11000)
account.withdraw(800)
account.exit()
