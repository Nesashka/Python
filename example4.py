num = abs(int(input('Ввдите плоложительное число: ')))
max = num % 10
while num >= 1:
	num = num //10
	if num % 10 > max:
		max = num % 10
	if num > 9:
		continue
	else:
		print('Максимальная цифра в числе: ',max)
		break