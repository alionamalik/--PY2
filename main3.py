# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Point:
    def __init__(self, x_axis:float, y_axis:float):
        """
        Создание и подготовка к работе объекта "Точка"

        :param x_axis: Значение по оси х
        :param y_axis: Значение по оси у

        Примеры:
        >>> point = Point(5.75, 1877) # инициализация экземляра класса
    """
        if not isinstance(x_axis, (int, float)):
            raise TypeError("Значение по оси х должно быть типа int или float")
        self.x_axis = x_axis

        if not isinstance(y_axis, (int, float)):
            raise TypeError("Значение по оси у должно быть типа int или float")
        self.y_axis = y_axis

    def slope_origin(self) -> float:
        """
        Функция, которая определяет коэффициент наклона прямой, проведённой через точку и начало координат

        :return Коэффициент наклона прямой, проведённой через точку и начало координат

        Примеры:
        >>> point = Point(300, 78)
        >>> point.slope_origin()
        """
        ...

    def lower_scaling(self, value: float) -> None:
        """
        Уменьшение координат точки в какое-то число раз.
        :param value: Число

        Примеры:
        >>>point = Point(200, 20)
        >>>point.lower_scaling(2)
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Число должно быть типа int или float")
        if value is 0:
            raise ValueError("Число не должно равняться 0")
        ...

    def if_line(self, a: float, b: float, c:float) -> bool:
        """
        Функция, которая проверяет принадлежность точки прямой.

        :param a: Коэффициент А в уравнении прямой
        :param b: Коэффициент B в уравнении прямой
        :param c: Коэффициент C в уравнении прямой

        :return Принадлежит ли точка прямой

        Примеры:
        >>>point = Point(3, 4)
        >>>point.if_line(7, 9, 12)
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Значение коэффициента А должно быть типа int или float")
        if not isinstance(b, (int, float)):
            raise TypeError("Значение коэффициента В должно быть типа int или float")
        if not isinstance(c, (int, float)):
            raise TypeError("Значение коэффициента С должно быть типа int или float")
        ...



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
