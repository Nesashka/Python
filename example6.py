a = float(input("Введите результаты пробежки первого дня в км: "))
b = float(input("Введите общий результат в км: "))
day = 1
km = a
print(f'%.d день: %.1f км' % (day, km))
while km < b:
	a = a + 0.1 * a
	km = a + km
	day += 1
	print(f'%.d день: %.1f км' % (day, km))
	



