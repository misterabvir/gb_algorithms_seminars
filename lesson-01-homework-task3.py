# Домашняя работа (задание 3) проверка алгоритма
# К первому занятию курсу лекций  "Введение в программирование (семинары)"
# Автор: Мазалов Алексей https://gb.ru/users/8831713

index = 0
sum = 0
count = 4
number = 0
while index < count:
    number = int(input("Type number: "))
    sum = sum + number
    index = index + 1
adv = sum / count
print(adv)