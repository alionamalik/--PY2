# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class EyebrowPencil:
    def __init__(self, color_name:str, price:float):
        """
        Создание и подготовка к работе объекта "Карандаш для бровей"

        :param color_name: Название цвета
        :param price: Цена

        Примеры:
        >>> eyebrowpencil = EyebrowPencil('hazel brown', 699) # инициализация экземляра класса
    """
        if not isinstance(color_name, (str)):
            raise TypeError("Цвет должен быть задан в виде строки")
        if len(color_name) is 0:
            raise ValueError("Цвет должен быть заполнен")
        self.color_name = color_name

        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = price

    def if_brown(self) -> bool:
        """
        Функция, которая проверяет, является ли цвет карандаша оттенком коричневого

        :return Коричневый ли карандаш

        Примеры:
        >>> eyebrowpencil = EyebrowPencil('oak brown', 3200)
        >>> eyebrowpencil.if_brown()
        """
        ...

    def lower_price(self, price:float) -> None:
        """
        Уменьшение цены на процент.
        :param percent: Процент
        :raise ValueError: Если итоговая цена <= 0, то возвращается ошибка
        :raise ValueError: Если процент < 0, то возвращается ошибка

        Примеры:
        >>>eyebrowpencil = EyebrowPencil('obsidian black', 1990)
        >>>eyebrowpencil.lower_price(10)
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int, float")
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
