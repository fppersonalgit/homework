# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.

def x_y_pow(x, y):
    x = int(input("Enter 1 number should be > 0 and + \n"))
    y = int(input("Enter 2 number should be < 0 and - \n"))

    if y > 0:
        print ("Please try again")

    c = abs(y)
    pow_1 = x ** c
    pow_2 = 1 / pow_1

    print(pow_2)

    return pow_2


x_y_pow(-2, -5)