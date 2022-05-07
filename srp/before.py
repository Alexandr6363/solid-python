class ExportCsv:
    """
        Данные класс нарушает принцип SRP
        Один класс покрывает сразу 2 зоны ответсвенности
    """
    def __init__(self, raw_data):
        self.data = self.prepare(raw_data)

    def prepare(self, raw_data):
        """
        Потому что здесь сразу форматруются данные и подготавливаются для вывода куда-то
        Тут не указывается куда идёт вывод
        """
        result = ''
        for item in raw_data:
            new_line = ','.join(
                (
                    item['name'],
                    item['surname'],
                    item['occupation']
                )
            )
            result += f"{new_line}\n"
        return result

    def write_file(self, filename):
        """
        Метод который записывает что-то в файл
        """
        with open(filename, 'w', encoding='UTF8') as f:
            f.write(self.data)


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

exporter = ExportCsv(data)
exporter.write_file('out.csv')