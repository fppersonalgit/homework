# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

shortlist_1 = input(str("Enter elements for list - \n"))

l1 = list(shortlist_1.split(" "))
print(l1)

print(l1[1])

k = 0
for number_l1 in range(int(len(l1) / 2)):
<<<<<<< Updated upstream
    
=======

>>>>>>> Stashed changes
    l1[k], l1[k + 1] = l1[k + 1], l1[k]

    k += 2

print(l1)














