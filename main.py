# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Barbell:
    def __init__(self, max_weight:float, current_weight:float):
        """
        Создание и подготовка к работе объекта "Штанга"

        :param max_weight: Максимально возможный вес
        :param current_weight: Текущий вес

        Примеры:
        >>> barbell = Barbell(200, 60) # инициализация экземляра класса
    """
        if not isinstance(max_weight, (int, float)):
            raise TypeError("Максимальный вес должен быть типа int или float")
        if max_weight <= 0:
            raise ValueError("Максимальный должен быть положительным числом")
        self.max_weight = max_weight

        if not isinstance(current_weight, (int, float)):
            raise TypeError("Текущий вес должен быть int или float")
        if current_weight < 0:
            raise ValueError("Текущий вес не может быть отрицательным числом")
        self.current_weight = current_weight

    def if_more_weight(self) -> bool:
        """
        Функция, которая проверяет, можно ли добавить вес на штангу

        :return Можно ли добавить вес на штангу

        Примеры:
        >>> barbell = Barbell(200,200)
        >>> barbell.if_more_weight()
        """
        ...

    def add_weight(self, weight:float) -> None:
        '''
        Добавление веса на штангу.
        :param weight: Вес
        :raise ValueError: Если после добавления веса суммарный вес превышает максимально допустимый, то возвращается ошибка

        Примеры:
        >>>barbell = Barbell(200, 25)
        >>>barbell.add_weight(178.5)
        '''
        if not isinstance(weight, (int, float)):
            raise TypeError("Добавляемый вес должен быть типа int или float")
        if weight < 0:
            raise ValueError("Добавляемый вес должен быть положительным числом")
        ...

    def remove_weight(self, weight:float) -> float:
        '''
        Уменьшение веса на штанге.
        :param weight: Вес
        :raise ValueError: Если после уменьшения веса суммарный вес отрицательный, то возвращается ошибка

        :return Новый вес штанги

        Примеры:
        >>>barbell = Barbell(200, 160)
        >>>barbell.add_weight(188)
        '''
        if not isinstance(weight, (int, float)):
            raise TypeError("Вычитаемый вес должен быть типа int или float")
        if weight < 0:
            raise ValueError("Вычитаемый вес должен быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
