# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

for i in range(1, 10):
    new_dir = ('dir_{}'.format(i))
    os.mkdir(new_dir)

for i in range(1, 10):
    dir_delete = ('dir_{}'.format(i))
    os.rmdir(dir_delete)



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print(os.listdir("./"))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil

print(__file__)

shutil.copy(r'hw05_easy.py', r'hw05_easy_copy.py')