# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

list = ["яблоко", "банан", "киви", "арбуз"]

i = 1
for fruit in list:
    print('{}. {:>10}'.format(i, fruit))
    i = i + 1
print("Задание 1 выполнено")
print(" ")


# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# ВТОРОЙ СПОСОБ - позволяет не ограничивать кол-во символов в названии фруктов

fruits = ["яблоко", "банан", "киви", "арбуз", "маракуйямаракуйя"]

maxLen = 0
for i in fruits:
    if len(i) > maxLen:
        maxLen = len(i)
counter = 0
for i in fruits:
    needSpace = maxLen - len(i)
    spaceString = ""
    for n in range(needSpace):
        spaceString = spaceString + " "
    counter = counter + 1
    print(str(counter) + ". " + spaceString + i)

print("Задание 1 выполнено другим способом")
print(" ")

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке и выведите результат.

list1 = [1, 2, 3, 4, 5, 55, 19]
list2 = [55, 7, 8, 1]
result = set(list1) - set(list2)
print(result)
print("Задание 2 выполнено")
print(" ")

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# и выведите результат
list_old = [1, 10, 44, 17, 0]
list_new = [i/4 if i%2 == 0 else i*2 for i in list_old]
print(list_new)

print("Задание 3 выполнено")
print(" ")