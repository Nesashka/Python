time = int(input('Введите время в секундах: '))
h = time // 3600
m = (time - h * 3600) // 60
c = time - (h * 3600 + m * 60)
print(f'Время ч:м:с = {h} : {m} : {c}')