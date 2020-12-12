# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.


a = int(input("Enter value a = \n "))
b = int(input("Enter value b = \n"))
print(type(a))
print(type(b))


def calculation_values(value1, value2):
    if b == 0:
        print("No! Try Again")
    result = value1 / value2
    return result


total = calculation_values(a, b)
print(total)
