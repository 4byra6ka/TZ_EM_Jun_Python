class Book:
    def __init__(self, _id: int, title: str, author: str, year: int, status: bool = True) -> None:
        """
        Инициализация экземпляра класса книги
        :param _id: Уникальный идентификатор книги
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        :param status: Статус книги: “в наличии”, “выдана”
        """
        self.__id = _id
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = status

    def __str__(self) -> str:
        """
        Магический метод str для вывода полной информации о книги
        """
        return (f'ID:{self.__id}, Название книги:{self.__title}, Автор книги: {self.__author}'
                f', Год издания: {self.__year}, Cтатус книги: {self.status}')

    def book_dict(self) -> dict:
        """
        Функция для вывода книги в формате словарь
        """
        return {'_id': self.__id, 'title': self.__title, 'author': self.__author, 'year': self.__year
            , 'status': self.__status}

    @property
    def status(self) -> str:
        """
        Геттер статуса книги в пользовательском читабельном виде
        """
        if self.__status:
            book_status = 'в наличии'
        else:
            book_status = 'выдана'
        return book_status

    @status.setter
    def status(self, status: bool) -> None:
        """
        Сеттер для изменения статуса книги
        """
        self.__status = status

    @property
    def get_id(self) -> int:
        """
        Геттер для получения id экземпляра книги
        """
        return self.__id

    @property
    def title(self) -> str:
        """
        Геттер для получения title экземпляра книги
        """
        return self.__title

    @property
    def author(self) -> str:
        """
        Геттер для получения author экземпляра книги
        """
        return self.__author

    @property
    def year(self) -> int:
        """
        Геттер для получения year экземпляра книги
        """
        return self.__year
