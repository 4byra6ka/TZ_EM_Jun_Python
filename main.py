from src.book_library_service import BookLibraryService


def main() -> None:
    """
    Запуск интерфейса системы управления библиотекой
    """
    book_library_service = BookLibraryService()
    text_menu_query = {
        1: 'Добавление книги ',
        2: 'Удаление книги',
        3: 'Поиск книги',
        4: 'Отображение всех книг',
        5: 'Изменение статуса книги',
        6: 'Выход'
    }
    while True:
        [print(f"{number_item}: {query_item}") for number_item, query_item in text_menu_query.items()]
        choice  = int(input("Введи номер:"))
        if choice  == 1:
            book_library_service.add_book()
        elif choice  == 2:
            book_library_service.del_book()
        elif choice  == 3:
            book_library_service.search_book()
        elif choice  == 4:
            book_library_service.list_book()
        elif choice  == 5:
            book_library_service.edit_status_book()
        elif choice == 6:
            print('\nВыход')
            break
        else:
            print('\nНету такого номера. Повторите попытку.')
            continue


if __name__ == "__main__":
    main()
