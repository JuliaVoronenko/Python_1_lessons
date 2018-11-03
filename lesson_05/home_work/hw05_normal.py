# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os, easy

current_path = os.getcwd()


def show_menu():
    print("Доступные действия:")
    print("1. Перейти в папку")
    print("2. Просмотреть содержимое текущей папки")
    print("3. Удалить папку")
    print("4. Создать папку")


def run_action(num):
    global current_path
    if num == 1:
        want_to_open_dir = input("Введите название папки, которую вы хотите открыть: ")
        current_path = current_path + "/" + want_to_open_dir
        print("Текущий путь: " + current_path)
    elif num == 2:
        easy.show_files(current_path)
    elif num == 3:
        want_to_del_dir = input("Введите название папки, которую вы хотите удалить: ")
        full_path_want_to_del_dir = current_path + "/" + want_to_del_dir
        easy.delete_dir(full_path_want_to_del_dir)
        print("Папка удалена")
    elif num == 4:
        want_to_create_dir = input("Введите название папки, которую вы хотите создать: ")
        full_path_want_to_create_dir = current_path + "/" + want_to_create_dir
        easy.create_dir(full_path_want_to_create_dir)
        print("Папка создана")
    elif num == 5:
        print
    else:
        print("Вы выбрали неверное действие")


show_menu()
while True:
    action_num = int(input("Выберите номер команды: "))
    run_action(action_num)
    print("  ")




