# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


def get_line_segment_length_by_coordinates(x1, y1, x2, y2) -> float:
    """
    Вычисляет длину отрезка, заданного двумя координатам
    :param x1: int Абсцисса первой координаты
    :param y1: int Ордината первой координаты
    :param x2: int Абсцисса второй координата
    :param y2: int Ордината второй координата
    :return: float Длина отрезка
    """
    result = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    return result


class Triangle:
    point_a = (0, 0)
    point_b = (0, 0)
    point_c = (0, 0)

    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def get_length_ab(self) -> float:
        """
        Возвращает длину стороны треугольника AB
        :return: int
        """
        return get_line_segment_length_by_coordinates(self.point_a[0], self.point_a[1],
                                                      self.point_b[0], self.point_b[1])

    def get_length_bc(self) -> float:
        """
        Возвращает длину стороны треугольника BC
        :return: int
        """
        return get_line_segment_length_by_coordinates(self.point_b[0], self.point_b[1],
                                                      self.point_c[0], self.point_c[1])

    def get_length_ca(self) -> float:
        """
        Возвращает длину стороны треугольника CA
        :return: int
        """
        return get_line_segment_length_by_coordinates(self.point_c[0], self.point_c[1],
                                                      self.point_a[0], self.point_a[1])

    def get_square(self) -> float:
        semi_perimeter = self.get_perimeter() / 2
        square = math.sqrt(
            (semi_perimeter - self.get_length_ab()) * (semi_perimeter - self.get_length_bc()) * (semi_perimeter - self.get_length_ca()) * semi_perimeter)
        return square

    def get_height(self) -> float:
        """
        Возвращает высоту треугольника. Считается, что основание треугольника - сторона между первой и третей вершиной
        :return: float
        """
        height = 2 * self.get_square() / self.get_length_ca()
        return height

    def get_perimeter(self) -> float:
        """
        Возвращает периметр треугольника
        :return: float
        """
        perimeter = self.get_length_ab() + self.get_length_bc() + self.get_length_ca()
        return perimeter


print(" ")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EquilateralTrapezium:
    point_a = (0, 0)
    point_b = (0, 0)
    point_c = (0, 0)
    point_d = (0, 0)

    def __init__(self, point_a, point_b, point_c, point_d):
        # Провека: у равнобедренной трапеции диагонали должны быть равны
        if get_line_segment_length_by_coordinates(point_a[0], point_a[1], point_c[0], point_c[1]) != get_line_segment_length_by_coordinates(point_b[0], point_b[1], point_d[0], point_d[1]):
            raise Exception("Создаваемая трапеция не является равнобедренной, проверьте координаты!")

        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def get_length_ab(self) -> float:
        """
        Возвращает длину стороны трапеции AB
        :return: int
        """
        return get_line_segment_length_by_coordinates(self.point_a[0], self.point_a[1],
                                                      self.point_b[0], self.point_b[1])

    def get_length_bc(self) -> float:
        """
        Возвращает длину стороны трапеции BC
        :return: int
        """
        return get_line_segment_length_by_coordinates(self.point_b[0], self.point_b[1],
                                                      self.point_c[0], self.point_c[1])

    def get_length_cd(self) -> float:
        """
        Возвращает длину стороны трапеции CD
        :return: int
        """
        return get_line_segment_length_by_coordinates(self.point_c[0], self.point_c[1],
                                                      self.point_d[0], self.point_d[1])

    def get_length_da(self) -> float:
        """
        Возвращает длину стороны трапеции DA
        :return: int
        """
        return get_line_segment_length_by_coordinates(self.point_d[0], self.point_d[1],
                                                      self.point_a[0], self.point_a[1])

    def get_perimeter(self) -> float:
        """
        Возвращает периметер трапеции
        :return: float
        """
        perimeter = self.get_length_ab() + self.get_length_bc() + self.get_length_cd() + self.get_length_da()
        return perimeter

    def get_height(self) -> float:
        """
        Возвращает высоту трапеции
        :return: float
        """
        # через формулу геометрическую, высота равнобедренной трапеции
        height = math.sqrt(self.get_length_ab()**2 - (self.get_length_da()-self.get_length_bc())**2/4)
        return height

    def get_square(self) -> float:
        """
        Возвращает площадь трапеции
        :return:
        """
        # через формулу геометрическую, площадь равнобедренной трапеции. S=½h(a+b)
        square = self.get_height()/2*(self.get_length_bc()+self.get_length_da())
        return square


# Проверка кода
my_tri = Triangle((0, 0), (5, 5), (10, 0))
print(my_tri.get_height())
