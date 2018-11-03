# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, pos):
    origin_number_as_str = str(number)
    numbers = origin_number_as_str.split(".")
    first_part = numbers[0]
    second_part = numbers[1]

    result = first_part + '.' + second_part[:pos-1]

    if int(second_part[pos+1]) >= 5:
        result = result + str(int(second_part[pos-1]) + 1)
    else:
        result = result + second_part[pos]

    return float(result)


print(my_round(12.828794678765, 2))







# Задание-2:q
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

ticket = int(input("Введите шестизначный номер билета: "))
f = lambda ticket : (lambda ticket : 'yes' if sum(ticket[:3]) == sum(ticket[3:]) else 'no')(list(map(int, list(str(ticket)))))
res = f(ticket)
print(res)



