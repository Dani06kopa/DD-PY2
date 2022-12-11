import doctest

class TV_series:
    def __int__(self, timing: int, episodic: int):
        """
        Объект Сериал: создание и подготовка к циклу
        :param timing: хронометраж
        :param episodic: количество эпизодов
        """

        if not isinstance(timing, int):
            raise TypeError("Хронометраж должен идти в формате int")
        if timing < 0:
            raise ValueError("Хронометраж должен быть положительным или равен 0")
        self.timing = timing

        if not isinstance(episodic, int):
            raise TypeError("Количество эпизодов должно идти в формате int")
        if episodic < 0:
            raise ValueError("Количество эпизодов должно быть положительным или равным 0")
        self.episodic = episodic


    def TV_series_genre(self) -> str:
        """
        Определение жанра сериала
        :return: "Слово, отражающее информацию о жанре"
        """


    def is_fatherland_casket(self) -> bool:
        """
        Функция, проверяющая, является ли сериал отечественным
        :return: "Да/Нет"
        """


if __name__ == "__main__":
    doctest.testmod()