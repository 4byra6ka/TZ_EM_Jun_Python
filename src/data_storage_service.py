import json
import os


class DataStorageService:
    def __init__(self, name_file: str = 'book_library.json'):
        """
        Инициализация экземпляра класс хранения данных
        :param name_file: имя файла
        """
        self.name_file = name_file
        self.check_file()

    def check_file(self) -> None:
        """Проверка файла на существование"""
        if not os.path.exists(self.name_file):
            with open(self.name_file, 'w') as w_file:
                json.dump({}, w_file, indent=4)

    def read_file(self) -> list[dict]:
        """
        Чтения файла в json формате
        :return: Список словарей книг
        """
        with open(self.name_file, "r") as r_file:
            return json.load(r_file)

    def write_file(self, data: list[dict]) -> None:
        """
        Запись файла в json формате
        :param data:Список словарей книг
        """
        with open(self.name_file, "w") as w_file:
            json.dump(data, w_file, indent=4)
