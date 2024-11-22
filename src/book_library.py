from abc import ABC, abstractmethod

from src.book import Book


class BookLibraryABC(ABC):
    """
    Абстракция книжной библиотеки
    """
    @abstractmethod
    def add_book(self, title: str, author: str, year: int):
        pass

    @abstractmethod
    def del_book(self, _id: int):
        pass

    @abstractmethod
    def search_book(self, search_query: int|str):
        pass

    @abstractmethod
    def list_book(self):
        pass

    @abstractmethod
    def edit_status_book(self, _id: int, status: bool):
        pass


class BookLibrary(BookLibraryABC):

    def __init__(self, data_library: list[dict]) -> Book:
        """
        Инициализация книжной библиотеки и добавление экземпляров класса книг в библиотеку
        :param data_library:
        """
        self.__library = [Book(**book) for book in data_library]

    def add_book(self, title: str, author: str, year: int) -> Book:
        """
        Функция добавление экземпляра книги в библиотеку
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        :return: Вывод экземпляра класса книга
        """
        if self.__library:
            _id = self.__library[len(self.__library) - 1].get_id + 1
        else:
            _id = 1
        book = Book(_id, title, author, year)
        self.__library.append(book)
        return book

    def del_book(self, _id: int) -> Book|None:
        """
        Функция удаления из библиотеки книги
        :param _id: Уникальный идентификатор книги
        :return: Вывод статуса удаление книги из библиотеки
        """
        for book in self.__library:
            if book.get_id == _id:
                self.__library.remove(book)
                return book
        else:
            return None

    def search_book(self, search_query: str) -> list[Book]|list[None]:
        """
        Функция поиска по году, автору и названию книг(и) в библиотеке
        :param search_query: запрос поиска
        :return: вывод результата поиска
        """
        search_response = []
        for book in self.__library:
            if search_query.isdigit():
                if (int(search_query) == book.year or search_query.lower() in book.title.lower()
                        or search_query.lower() in book.author.lower()) :
                    search_response.append(book)
            else:
                if search_query.lower() in book.title.lower() or search_query.lower() in book.author.lower():
                    search_response.append(book)
        return search_response

    def list_book(self) -> list[Book]:
        """
        Функция списка всех книг в библиотеке
        :return: список книг
        """
        return self.__library

    def edit_status_book(self, _id: int, status: bool) -> Book|None:
        """
        Функция изменения статуса книги “в наличии” или “выдана”
        :param _id: Уникальный идентификатор книги
        :param status: статуса True(“в наличии”) или False(“выдана”)
        :return: Вывод результата изменения статуса книги из библиотеки
        """
        for book in self.__library:
            if book.get_id == _id:
                book.status = status
                return book
        else:
            return None
