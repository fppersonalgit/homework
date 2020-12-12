# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(value1, value2, value3):
    if value1 > value2 > value3:
        result = value1 + value2
        print(result)
        return result

    elif value2 > value1 > value3:
        result1 = value1 + value2
        print(result1)
        return result1

    elif value3 > value1 > value2:
        result3 = value1 + value3
        print(result3)
        return result3

    elif value3 > value2 > value1:
        result4 = value2 + value3
        print(result4)
        return result4

    elif value1 > value2 < value3:
        result5 = value1 + value3
        print(result5)
        return result5

    elif value3 > value2 > value1:
        result6 = value2 + value3
        print(result6)
        return result6

    elif value1 < value2 > value3:
        result7 = value3 + value2
        print(result7)
        return result7


a = my_func(12, 20, 50)
print(a)
