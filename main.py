# Задача: Версионирование метаданных SAS
import shutil
import os

PATH_FOR_EXPORT = 'C://Users//team53//PycharmProjects//I_am_POWER//For_export'


class Versioning:

    def __init__(self, data):
        """В data записывается path исходного файла"""
        self.data = data  # Предположим, что это метаданные sas
        self.block_mark = None

    def data_block(self, mark_to_block):
        """метка, которая запретит экспортировать файл каталога"""
        self.block_mark = mark_to_block
        return self.block_mark

    def export(self, mark='all'):

        block_mark = self.block_mark

        try:
            if self.block_mark == self.data:  # Проверка файла на доступ
                return 'Данный файл(ы) запрещены для перемещения.'

            elif mark == 'all':
                shutil.move(self.data, PATH_FOR_EXPORT)
                return f'Успешное перемещение в {PATH_FOR_EXPORT}'

            """Цикл, проверяющий отдельный файл каталога на запрет к перемещению."""
            for file in os.listdir(self.data):
                if file == block_mark and mark == file:
                    return 'Данный файл(ы) запрещены для перемещения.'

            else:
                shutil.move(self.data + '//' + mark, PATH_FOR_EXPORT)
                return 'Успешное перемещение', self.data + '//' + mark

        except FileNotFoundError:
            print(None)

    def git(self):
        pass

    def get_data_content(self):
        """Функция, возвращающая содержимое txt файла"""

        try:
            with open(self.data, 'r') as file:
                read_file = file.read()
            return read_file

        except PermissionError:

            files = os.listdir(self.data)
            error_message = 'Файл не найден.'
            return files


def demonstration_data_block():
    """В данной демонстрации для взаимодействий запрещён весь каталог"""
    data1 = Versioning('C://Users//team53//PycharmProjects//I_am_POWER//my_files')
    data1.data_block('C://Users//team53//PycharmProjects//I_am_POWER//my_files')
    print(data1.export())  # метка автоматически стоит на all
    print(data1.export('cars12.txt'))


def demonstration_export():
    """В данной демонстрации для взаимодействий запрещён только один отдельный файл каталога
    + Экспорт файла в папку For_export"""
    data2 = Versioning('C://Users//team53//PycharmProjects//I_am_POWER//my_files')
    data2.data_block('cars12.txt')
    print(data2.export('cars3.txt'))
    print(data2.export('cars12.txt'))
#
# demonstration_data_block()
# demonstration_export()
