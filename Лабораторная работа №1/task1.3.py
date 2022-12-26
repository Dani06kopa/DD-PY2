import doctest

class Life:
    def __int__(self, happiness: int, duration: int):
        """
        Объект Жизнь: создание и подготовка к циклу
        :param happiness: Уровень счастья по шкале от 0 до 10
        :param duration: Продолжительность жизни в годах
       Примеры:
        >>> life = Life(5, 20)  # инициализация экземпляра класса
        """

        if not isinstance(happiness, int):
            raise TypeError("Уровень счастья должен идти в формате int")
        if happiness < 0:
            raise ValueError("Уровень счастья должен быть положитедьным или равен 0")
        self.happiness = happiness

        if not isinstance(duration, int):
            raise TypeError("Продолжительность должна идти в формате int")
        if duration < 0:
            raise ValueError("Продолжительность должна быть положительной или равна 0")
        self.duration = duration


    def life(self) -> bool:
        """
        Проверка, есть ли смысл в жизни
        :return: Есть ли смысл в жизни
        Примеры:
        >>> life = Life(5, 20)
        >>> life.life("Да")
        """


    def invite_meaning(self, aim: str) -> None:
        """
        Создание смысла в жизни
        :param aim: Цель
        :raise ValueError: ошибка, если цель не достижима
       Примеры:
        >>> life = Life(5, 20)
        >>> life.life("Получить 10/10")
        """


    def broadcast_life(self, happy_person: float) -> None:
        """
        Передача жизни другим людям путем пересадки органов
        :param happy_person: количество человек, которые получили новую жизнь
        :raise ValueError: ошибка, если пытаются спасти больше людей, принебрегая качеством жизни других
        :return: Сколько людей в итоге получили новую жизнь
        Примеры:
        >>> life = Life(5, 20)
        >>> life.life(0)
        """


if __name__ == "__main__":
    doctest.testmod()
