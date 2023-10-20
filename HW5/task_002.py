# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.
# Не забудьте распечатать в конце результат.

import timeit

code1 = """

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

result = {names[i]: round(
    salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)

"""
time1 = timeit.timeit(code1, number=1)

code2 = """
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

result = {name: bet * float(bonus.strip('%')) /
          100 for name, bet, bonus in zip(names, salary, bonus)}

print(result)
"""
time2 = timeit.timeit(code2, number=1)

if time1 < time2:
    print("Первый вариант быстрее.")
elif time1 > time2:
    print("Второй вариант быстрее.")
else:
    print("Варианты выполняются с одинаковой скоростью.")

print(f"Время_1: {time1} секунд")
print(f"Время_2: {time2} секунд")
