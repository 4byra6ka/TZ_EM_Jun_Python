import unittest

from src.book_library import BookLibrary


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book_library_1 = BookLibrary([{'_id': 1, 'author': 'Достоевский Федор Михайлович', 'status': True,
                                            'title': 'Преступление и наказание', 'year': 1866},
                                           {'_id': 2, 'author': 'Беляев Александр Романович', 'status': True,
                                            'title': 'Голова профессора Доуэля', 'year': 1937}])

    def test_add_book(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.book_library_1.add_book('Программирование на Python. Том II. 4-е издание', 'Лутц Марк'
                                     , 2018)
        self.assertEqual(len(self.book_library_1.list_book()), 3)

    def test_del_book(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.book_library_1.del_book(2)
        self.assertEqual(len(self.book_library_1.list_book()), 1)

    def test_search_book(self):
        print(f'Запуск теста {self._testMethodName} ...')
        search_book = self.book_library_1.search_book('1937')
        self.assertEqual(search_book[0].book_dict(), {'_id': 2, 'author': 'Беляев Александр Романович', 'status': True,
                                                      'title': 'Голова профессора Доуэля', 'year': 1937})

    def test_list_book(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.assertEqual(len(self.book_library_1.list_book()), 2)

    def test_edit_status_book(self):
        print(f'Запуск теста {self._testMethodName} ...')
        book_1 = self.book_library_1.edit_status_book(1, False)
        self.assertEqual(book_1.book_dict()['status'], False)
        book_2 = self.book_library_1.edit_status_book(3, False)
        self.assertEqual(book_2, None)


if __name__ == '__main__':
    unittest.main()
