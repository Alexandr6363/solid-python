"""
    Данный пример не соответсвуте принципу, потому что если нужно внести изменения
    ( изменить формат отображение времени ), то они буду происходить напрямую, что нарушает
    прнцип  Open-closed
"""

import sys
import time


class Logger:
    """
        Класс с помощью которого выводится сообщение в консоль
    """
    def log(self, message):
        """
         Метод который получает дату и время в данный момент и выводит
         сообщение + время

        :param message: Сообщение которое передаётся методу

        :return: Возвращается ответ в виде вывода сообщения в консоль +
        отформатированное время
        """
        current_time = time.localtime()
        sys.stderr.write(f"{time.strftime('%Y-%b-%d %H:%M:%S', current_time)} --> {message}\n")


logger = Logger()
logger.log('An error has happened!')