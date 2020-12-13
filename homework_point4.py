# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

entered_number = int(input("Enter number. NOTE! It should be > 0 \n"))
r = -1
while entered_number > 0:
    d = entered_number % 10
    entered_number //= 10
    if d > r:
        r = d
print(r)


