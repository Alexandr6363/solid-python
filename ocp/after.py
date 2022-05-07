"""
    Создавая новый класс остается возможность менять префикс при этом изменения в основной
    класс не вносится, что соответсвует принципу - Open-closed
"""

import sys
import time


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log(self, message):
        sys.stderr.write(f"{self.prefix} --> {message}\n")


class CustomerLogger(Logger):
    """
    Для переопределения формата отображения даты и времени
    Нужно создать новый класс и там переопределить метод __init__
    Указав нужный формат даты и вреамени
    =======================================
    Напрямую класс не модфицируется, а расшряется путём наследования
    """
    def __init__(self):
        super().__init__()
        self.prefix = time.strftime('%Y-%b-%d', time.localtime())


logger = Logger()
logger.log('An error has happen!')


logger_custom = CustomerLogger()
logger_custom.log('Custom message')