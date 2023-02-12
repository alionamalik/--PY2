if __name__ == "__main__":
    class Cat:
        def __init__(self, weight: float, color: str):
            """
            Создание и подготовка к работе объекта "Кошка"

            :param weight: Вес. Инкапсулирован для проверки на корректность введённого значения.
            :param color: Цвет. Инкапсулирован для проверки на корректность введённого значения.
            Примеры:
                >>> cat = Cat(15.4, 'black')  # инициализация экземпляра класса
            """
            self._color = color
            self._weight = weight

        @property
        def color(self) -> str:
            return self._color

        @color.setter
        def color(self, new_color: str) -> None:
            if not isinstance(new_color, str):
                raise TypeError("Цвет должен быть типа str")

        @property
        def weight(self) -> float:
            return self._weight

        @weight.setter
        def weight(self, new_weight: float) -> None:
            if not isinstance(new_weight, float):
                raise TypeError("Вес должен быть типа float")
            if new_weight <= 0:
                raise ValueError("Вес должен быть положительным числом")
            self._weight = new_weight

        def __str__(self):
            """
            Метод отображает информацию об объекте класса для пользователей.
            """
            return f"{self.__class__.__name__}. Weight: {self._weight}. Color: {self._color}."

        def __repr__(self):
            """
            Метод возвращает строку, показывающую, как может быть инициализирован экземпляр.
            """
            return f"{self.__class__.__name__}(color={self._color!r}, weight={self._weight!r})"

        def add_weight(self, added_weight) -> None:
            """
            Добавление веса.
            :param added_weight: Добавляемый вес
            :raise ValueError: Если добавляемый вес меньше 0, то вызываем ошибку
            Примеры:
            >>> cat = Cat(23, 'white')
            >>> cat.add_weight(3.5)
            """
            ...

        def appearance(self) -> str:
            """
            Описание внешности.
            Примеры:
            >>> cat = Cat(23, 'white')
            >>> cat.appearance()
            """
            return f'Color is {self._color}.'

    class Lion(Cat):
        def __init__(self, weight: float, color: str, leader: bool):
            """
            Создание и подготовка к работе объекта "Лев"
            :param weight: Вес. Инкапсулирован для проверки на корректность введённого значения.
            :param color: Цвет. Инкапсулирован для проверки на корректность введённого значения.
            :param leader: Является ли вожаком прайда
            Примеры:
                >>> lion = Lion(170.7, 'light-sand', False)  # инициализация экземпляра класса
            """
            super().__init__(weight, color)
            self.leader = leader

        def __str__(self):
            """
            Метод отображает информацию об объекте класса для пользователей. Перегружен, т.к. появляется новый
            атрибут leader.
            """
            new_str = super().__str__()
            return new_str + f" Leader: {self.leader}."

        def __repr__(self):
            """
            Метод возвращает строку, показывающую, как может быть инициализирован экземпляр. Перегружен,
            т.к. появляется новый атрибут leader.
            """
            new_repr = super().__repr__()
            return new_repr + f"leader={self.leader!r})"


    class Tiger(Cat):
        def __init__(self, weight: float, color: str, pattern: str):
            """
            Создание и подготовка к работе объекта "Тигр"
            :param weight: Вес. Инкапсулирован для проверки на корректность введённого значения.
            :param color: Цвет. Инкапсулирован для проверки на корректность введённого значения.
            :param pattern: Узор. Инкапсулирован для проверки на корректность введённого значения.
            Примеры:
            >>> tiger = Tiger(146, 'white', ' thick stripes')  # инициализация экземпляра класса
            """
            super().__init__(weight, color)
            self._pattern = pattern

        @property
        def pattern(self) -> str:
            return self._pattern

        @pattern.setter
        def pattern(self, new_pattern: str) -> None:
            if not isinstance(new_pattern, str):
                raise TypeError("Узор должен быть типа str")

        def appearance(self) -> str:
            """
            Перегружаем метод описания внешности, т.к. учитываем новый атрибут pattern.
            Примеры:
            >>> tiger = Tiger(190, 'red', 'thin stripes')
            >>> tiger.appearance()
            """
            return f'The {self.__class__.__name__} is {self._color} with {self.pattern}.'

        def __str__(self):
            """
            Метод отображает информацию об объекте класса для пользователей. Перегружен, т.к. появляется новый
            атрибут pattern.
            """
            return f"{self.__class__.__name__}. Weight: {self._weight}. Color: {self._color}. Pattern: {self.pattern}"

        def __repr__(self):
            """
            Метод возвращает строку, показывающую, как может быть инициализирован экземпляр. Перегружен,
            т.к. появляется новый атрибут pattern.
            """
            return f"{self.__class__.__name__}(color={self._color!r}, weight={self._weight!r}), pattern={self.pattern!r}"


    lion1 = Lion(120, 'sand', True)
    tiger1 = Tiger(130, 'ginger', 'stripes')
    print(lion1)
    print(tiger1)
    print(lion1.appearance())
    print(tiger1.appearance())

pass
