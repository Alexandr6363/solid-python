class FormatData:
    """
        Данные класс нарушает принцип SRP
        Один класс покрывает сразу 2 зоны ответсвенности
    """
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def prepare(self):
        """
        Потому что здесь сразу форматруются данные и подготавливаются для вывода куда-то
        Тут не указывается куда идёт вывод
        """
        result = ''
        for item in self.raw_data:
            new_line = ','.join(
                (
                    item['name'],
                    item['surname'],
                    item['occupation']
                )
            )
            result += f"{new_line}\n"
        return result


class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        """
        Метод который записывает что-то в файл
        """
        with open(self.filename, 'w', encoding='UTF8') as f:
            f.write(data)


data = [
    {
        'name': 'Sherlock',
        'surname': 'Holmes',
        'occupation': 'private detective'
    },
    {
        'name': 'John',
        'surname': 'Watson',
        'occupation': 'doctor'
    }
]

formatter = FormatData(data)
formatted_data = formatter.prepare()

writer = FileWriter('out.csv')
writer.write(formatted_data)