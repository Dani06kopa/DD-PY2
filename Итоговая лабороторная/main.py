class Music:

    """Класс для музыки"""

    def __init__(self, name: str, length_in_sec: int, performers: list):
        """Конструктор, в который передается название, длина трека и список исполнителей"""
        self.name = name
        self.length_in_sec = length_in_sec
        self.is_listened = False
        self.performers = performers

    def __repr__(self) -> str:
        """Возвращает длину трека"""
        return str(self.length_in_sec) + " секунд"

    def __str__(self) -> str:
        """Дает информацию о музыкальном треке"""
        return 'Название трека: ' + self.name + ', длина трека: ' + repr(self)

    def set_listened(self):
        """Устанавливает значение, что музыкальный трек прослушан"""
        self.is_listened = True

    def print_performers(self):
        """Выводит список исполнителей"""
        print('Исполнители:')
        for performers in self.performers:
            print(performers)



class Classik(Music):

    """Класс для классической музыки"""

    def __init__(self, name: str, is_for_girls: bool):
        """Конструктор, в который передается название классической музыки и информация, подходят ли она для девушек"""
        self.name = name
        self.is_for_girls = is_for_girls

    def __repr__(self) -> str:
        """Возвращает текстовое значение для переменной is_for_girls"""
        if self.is_for_girls:
            return 'подходит для девушек'
        else:
            return 'не подходит для девушек'

    def __str__(self) -> str:
        """Выводит основную информацию о классической музыке"""
        return 'Название классической музыки: ' + self.name + ', ' + repr(self)

    def print_limitation(self):
        """В названии нет запрещенных слов, поэтому можно использовать в медиа"""
        print('Нет запрещенных слов')


music = Music("Холостяк", 144, ["Егор Крид, Feduk"])
print(music)
print(repr(Music))
print("Трек прослушан: " + str(music.is_listened))
music.set_listened()
print("Трек прослушан: " + str(music.is_listened))
music.print_performers()

print()

Classik = Classik("By stepping on your fears as", False)
print(Classik)
print(repr(Classik))
Classik.print_limitation()

