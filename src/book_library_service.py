from src.book_library import BookLibrary
from src.data_storage_service import DataStorageService


class BookLibraryService:
    """
    Класс сервиса библиотеки
    """
    def __init__(self) -> None:
        self.data_storage_service = DataStorageService()
        self.book_library = BookLibrary(self.data_storage_service.read_file())

    def add_book(self) -> None:
        """
        Функция добавление экземпляра книги в библиотеку
        """
        print('Добавление книги')
        title = input('Введите название книги:')
        author = input('Введите автора книги:')
        try:
            year = int(input('Введите год издания книги:'))
            print(f'Добавлена книга: {self.book_library.add_book(title, author, year)}\n')
            self.write_library()
        except ValueError as err:
            print(f'\n{err}')
            print('!!!Год нужно писать цифрами!!!\n')

    def del_book(self) -> None:
        """
        Функция удаления из библиотеки книги
        """
        print('\nУдаление книги:')
        try:
            book_id: int = int(input('Введите id книги:'))
        except ValueError as err:
            print(f'\n{err}')
            print(f'id может быть только цифры\n')
            return None
        book = self.book_library.del_book(book_id)
        if book:
            print(f'Удалена книга ID:{book.get_id}, Название книги:{book.title}, Автор книги: {book.author}'
                  f', Год издания: {book.year}\n')
            self.write_library()
        else:
            print(f"Книга с id:{book_id} не найдена.\n")

    def search_book(self) -> None:
        """
        Функция поиска по году, автору и названию книг(и) в библиотеке
        """
        print('\nПоиск книги:')
        search_query = input('Введите название книги, автора или год:')
        search_response = self.book_library.search_book(search_query)
        if search_response:
            [print(book) for book in search_response]
            print('\n')
        else:
            print('По данному запросу нету книг\n')

    def list_book(self) -> None:
        """
        Функция списка всех книг в библиотеке
        """
        print('\nОтображение всех книг:')
        for book in self.book_library.list_book():
            print(book)
        print('\n')

    def edit_status_book(self) -> None:
        """
        Функция изменения статуса книги “в наличии” или “выдана”
        """
        print('\nИзменение статуса книги:')
        try:
            book_id: int = int(input('Введите id книги:'))
        except ValueError as err:
            print(f'\n{err}')
            print(f'id может быть только цифры\n')
            return None
        status: str = input('Введите статус книги(“в наличии” или “выдана”):')
        if status.lower() == "в наличии":
            status: bool = True
        elif status.lower() == "выдана":
            status: bool = False
        else:
            print('Статус может быть только “в наличии” или “выдана”\n')
            return None
        book = self.book_library.edit_status_book(book_id, status)
        if book:
            print(f'Изменен статус книги: {book}\n')
            self.write_library()
        else:
            print(f"Книга с id:{book_id} не найдена.\n")

    def write_library(self) -> None:
        """
        Функция преобразования экземпляра библиотеки и книг в список словарей
        """
        self.data_storage_service.write_file([one_book.book_dict() for one_book in self.book_library.list_book()])