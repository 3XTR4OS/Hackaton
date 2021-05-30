# Версионирование метаданных SAS
"""Так как я не смог полностью осилить инструцию, сделал 'локальную' программу, котороя будет имитировать то, чтобы
я сделал, если бы хватило навыков разобраться.

Сделать 'контроль версий' у меня времени не осталось, поэтому опишу идею так:
Я бы взял схему версионирования: major.maintenance
major - крупные изменения, либо изменения несовместимые с предыдущей версией;
maintenance - исправления.

Т.к в SAS все файлы - метаданные, то при изменении оных (изначально имеют версию 0.0), в "vers_control" шла бы такая 
запись:
Файл(текущая версия) § старая версия § тип изменения(major/maintenance) § произошедшие изменения
cars(0.1) § 0.0 § maintenance § Fixed incorrect data

!!! РАСКОМЕНТИРОВАТЬ 2 ПОСЛЕДНИХ СТРОКИ !!!
"""

import os
import shutil

FILE_FOR_EXPORT = 'C://Users//team53//PycharmProjects//I_am_POWER//For_export'


class Versioning:

    def __init__(self, data):
        """В data записывается path файла"""
        self.data = data  # Предположим, что это метаданные sas
        self.block_mark = None

    def data_block(self, mark_to_block):  # mark_to_block - путь, который запретит перемещать файл
        self.block_mark = mark_to_block
        return self.block_mark

    def export(self, mark='all'):  # Экспорт файлов куда-либо по метке

        block_mark = self.block_mark

        try:
            if self.block_mark == self.data:  # Проверка на доступ
                return 'Данный файл(ы) запрещены для перемещения.'

            elif mark == 'all':
                shutil.move(self.data, FILE_FOR_EXPORT)
                return f'Успешное перемещение в {FILE_FOR_EXPORT}'

            """Цикл, запрещающий отдельный файл"""
            for file in os.listdir(self.data):
                if file == block_mark and mark == file:
                    return 'Данный файл(ы) запрещены для перемещения.'

            else:
                shutil.move(self.data + '//' + mark, FILE_FOR_EXPORT)
                return 'Успешное перемещение', self.data + '//' + mark

        except FileNotFoundError:
            print(None)

    def git(self):  # идей нет
        pass

    def get_data_content(self):
        """Для себя"""

        try:
            with open(self.data, 'r') as file:
                read_file = file.read()
            return read_file

        except PermissionError:

            files = os.listdir(self.data)
            return files


def demonstration_data_block():
    """В данной демонстрации для взаимодействий запрещён весь каталог"""
    data1 = Versioning('C://Users//team53//PycharmProjects//I_am_POWER//my_files')
    data1.data_block('C://Users//team53//PycharmProjects//I_am_POWER//my_files')
    print(data1.export())  # метка автоматически стоит на all
    print(data1.export('cars12.txt'))


def demonstration_export():
    """В данной демонстрации для взаимодействий запрещён только один отдельный файл каталога
    + Экспорт файла в папочку For_export"""
    data2 = Versioning('C://Users//team53//PycharmProjects//I_am_POWER//my_files')
    data2.data_block('cars12.txt')
    print(data2.export('cars3.txt'))
    print(data2.export('cars12.txt'))

# demonstration_data_block()
# demonstration_export()
