# This is my first Pyton homework. Lesson 1 Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

#Figher statistics
ko = 2
sub = 4
dec = 1

wins = ko + sub + dec

losses = 2


fights = wins + losses

#opponent = str()



print("Fighter Statistics")
print("Wins - ", (wins))
print("ko/kto - ", (ko))
print("sub - ", (sub))
print("dec - ", (dec))

print("Losses - ", (losses))
print("Total fights - ", (fights))

print("-------------------------------------")

round_prediction = int(input("Your prediction? In what round you see this fight will be ended?(from -1 to 3):\n"))

print("Users prediction -", round_prediction)
