profit = float(input("Введите выручку: "))
costs = float(input("Введите издержки: "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность: {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников: "))
    print(f"Прибыль в расчете на одного сторудника: {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")