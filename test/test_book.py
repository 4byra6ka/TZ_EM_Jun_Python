from src.book import Book
import unittest


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book_1 = Book(1, 'Преступление и наказание', 'Достоевский Федор Михайлович', 1866)
        self.book_2 = Book(2, 'Голова профессора Доуэля', 'Беляев Александр Романович', 1937)

    def test_str(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.assertEqual(self.book_1.__str__(),
                         'ID:1, Название книги:Преступление и наказание, Автор книги: Достоевский Федор Михайлович, Год издания: 1866, Cтатус книги: в наличии')
        self.assertEqual(self.book_2.__str__(),
                         'ID:2, Название книги:Голова профессора Доуэля, Автор книги: Беляев Александр Романович, Год издания: 1937, Cтатус книги: в наличии')

    def test_book_dict(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.assertEqual(self.book_1.book_dict(), {'_id': 1, 'author': 'Достоевский Федор Михайлович', 'status': True,
                                                   'title': 'Преступление и наказание', 'year': 1866})
        self.assertEqual(self.book_2.book_dict(), {'_id': 2, 'author': 'Беляев Александр Романович', 'status': True,
                                                   'title': 'Голова профессора Доуэля', 'year': 1937})

    def test_status_getter(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.assertEqual(self.book_1.status, 'в наличии')
        self.assertEqual(self.book_2.status, 'в наличии')

    def test_status_setter(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.book_1.status = False
        self.assertEqual(self.book_1.status, 'выдана')
        self.book_2.status = False
        self.assertEqual(self.book_2.status, 'выдана')

    def test_get_id(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.assertEqual(self.book_1.get_id, 1)
        self.assertEqual(self.book_2.get_id, 2)

    def test_title(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.assertEqual(self.book_1.title, 'Преступление и наказание')
        self.assertEqual(self.book_2.title, 'Голова профессора Доуэля')

    def test_author(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.assertEqual(self.book_1.author, 'Достоевский Федор Михайлович')
        self.assertEqual(self.book_2.author, 'Беляев Александр Романович')

    def test_year(self):
        print(f'Запуск теста {self._testMethodName} ...')
        self.assertEqual(self.book_1.year, 1866)
        self.assertEqual(self.book_2.year, 1937)


if __name__ == '__main__':
    unittest.main()
