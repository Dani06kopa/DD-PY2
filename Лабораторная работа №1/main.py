import doctest


class Perfume:
    def __int__(self, brand: str, volume: int):
        """
        Объект Парфюм: создание и подготовка к циклу
        :param brand: Название бренда
        :param volume: Объём флакона в мл
        Примеры:
        >>> perfume = Perfume("Nasomatto", 30)  # инициализация экземпляра класса
        """
     if not isinstance(brand, str):
        raise TypeError("Название должно быть типа str")
     self.brand = brand
    if not isinstance(volume, int):
        raise TypeError("Объём должен быть типа int")
     if volume < 0:
        raise ValueError("Объём должен быть положительным или равным 0")
     self.volume = volume

    def authenticity(self) -> bool:
         """
        Проверка на подлиность парфюма
        :return: присутсвуют ли идентификационные коды
        Примеры:
        >>> perfume = Perfume('Nasomatto', 30)
        >>> perfume.authenticity("Да")
        """
        ...


    def price_parfum(self, money: [int, float]):
        """
        Определение стоимости парфюма.
        :param money: цена
        :raise TypeError: Если введен неверный тип данных, возвращается ошибка
        :raise ValueError: Если цена отрицательная, возвращается ошибка
        :return: Цена парфюма
        Примеры:
        >>> perfume = Perfume('Nasomatto', 30)
        >>> perfume.price_parfum(9982)
        """
        ...

if __name__ == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации

