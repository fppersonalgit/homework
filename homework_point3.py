# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 +
# 33 + 333 = 369.

n = str(input("Enter digit - \n"))

nn = n + n
nnn = n + n + n

n_real = int(n)
nn_real = int(nn)
nnn_real = int(nnn)

n_sum = n_real + nn_real + nnn_real

print( n_real, "+", nn_real, "+", nnn_real, "=", n_sum)









