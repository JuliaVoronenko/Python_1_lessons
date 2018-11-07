# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import re


class Worker:
    first_name = ""
    second_name = ""
    monthly_hours = 0
    monthly_salary = 0

    def __init__(self, first_name, second_name, monthly_rate_hours, monthly_rate_salary):
        self.first_name = first_name
        self.second_name = second_name
        self.monthly_hours = int(monthly_rate_hours)
        self.monthly_salary = int(monthly_rate_salary)

    def get_hourly_rate(self) -> float:
        return self.monthly_salary / self.monthly_hours

    def get_salary(self, worked_hours) -> float:
        if worked_hours > self.monthly_hours:
            salary = self.monthly_hours * self.get_hourly_rate() + (worked_hours - self.monthly_hours) * self.get_hourly_rate() * 2
        else:
            salary = self.get_hourly_rate() * worked_hours
        return round(salary, 2)


class WorkerRepo:
    workers_list = {}

    @staticmethod
    def add(worker):
        h = WorkerRepo.__get_hash(worker.first_name, worker.second_name)
        WorkerRepo.workers_list.update({h: worker})

    @staticmethod
    def get(first_name, second_name):
        h = WorkerRepo.__get_hash(first_name, second_name)
        return WorkerRepo.workers_list.get(h)

    @staticmethod
    def __get_hash(first_name, second_name):
        return hash(first_name + second_name)


class FileReader:
    @staticmethod
    def open(path):
        regex = r"\ +"
        file_as_string = open(path).read()
        csv = re.sub(regex, ',', file_as_string)
        rows = csv.split("\n")
        titles = rows.pop(0).split(',')

        result_list = []
        for row in rows:
            values = row.split(',')
            n = 0
            new_item = {}
            for value in values:
                new_item.update({titles[n].lower(): value})
                n = n + 1
            result_list.append(new_item)
        return result_list


workers_list = FileReader.open('data/workers')
for worker_dict in workers_list:
    worker_obj = Worker(worker_dict.get('имя'),
                        worker_dict.get('фамилия'),
                        worker_dict.get('норма_часов'),
                        worker_dict.get('зарплата'))
    WorkerRepo.add(worker_obj)

hours_list = FileReader.open('data/hours_of')
for statement in hours_list:
    worker = WorkerRepo.get(statement.get('имя'), statement.get('фамилия'))
    current_salary = worker.get_salary(int(statement.get('отработано')))
    print(worker.first_name + " " + worker.second_name + " отработал " + statement.get('отработано') + " часов и должен получить зарплату " + str(current_salary))


