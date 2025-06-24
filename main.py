import json

import csv
import pathlib
import logging


logging.basicConfig(level=logging.INFO, filename='py_log.log',filemode='w')

def compare(list1, list2):
    """list1- list2- """
    result = []
    x = list1
    for i in list2:
        if i in x:
            pass
        else:
            print(i)
            result.append(i)
    return result


class Comment:
    def __init__(self, symbol, position, flag_new):
        self.symbol = symbol
        self.position = position
        self.flag_new = flag_new


class FildComment:
    def __init__(self, path):
        self.path = path
        self.file = self.input_output()
        self.start = self.file['start']
        if self.start <= 0:
            logging.info("Ошибка! Колличество стартов меньше или равно 0")
            exit()
        self.position = {}
        for key_json in self.file['switch']:
            comment = self.add_pos(self.file['switch'][key_json])
            self.position[key_json] = comment

    def input_output(self, flag='r'):
        """Загрузка выгрузка"""
        if flag == 'r':
            with open(self.path, 'r', encoding='utf-8') as f:
                """Файл json c переключателями."""
                file_content = f.read()
            return json.loads(file_content)
        elif flag == 'w':
            file = {'start':self.start, 'switch':{}}
            for key in self.position:
                data = self.position.get(key)
                file['switch'][key] = [data.symbol, data.position, data.flag_new]
            with open(self.path, 'w', encoding='utf-8') as outfile:
                json.dump(file, outfile, ensure_ascii=False)

    def add_pos(self, data):
        """Добавление позиции."""
        return Comment(data[0], data[1], data[2])

    def edit_pos(self):
        """Изменение позиции."""
        pass

    def del_pos(self):
        """Удаление позиции."""
        pass

# Пути к файлам
input_file = pathlib.Path('input_file/40198_csv_wo_predstavitel_2025_06_18.csv')
json_file = pathlib.Path('fields.json')

booking_poss = 2  # C:

export_orgeo = []
file_base = []
template_com = []


com = FildComment(json_file)



with open(input_file, encoding='windows-1251') as csv_f:
    """Файл csv c выгрузкой из orgeo."""
    csv_file = csv.reader(csv_f, delimiter=';')
    for line in csv_file:
        export_orgeo.append(line)

count_firlds = 20 # Кол-во символов WinOrient в комменте

sets = set() # Показатели orgeo
for row in export_orgeo:
    # Забрал все показатели из csv
    for i in row[8].split(',')[1:]: # Убрал определение дней
        sets.add(i.strip())


keys_json = com.position.keys()


print('__Новые__')
new = compare(list(keys_json), list(sets))
print('___Невостребованные___')
old = compare(list(sets), list(keys_json))

def func(x):
    com.position[x] = com.add_pos(['', 0, True])

if len(new) > 1:
    for pos in new:
        func(pos)
elif len(new) == 1:
    func(new[0])

com.input_output('w')


while count_firlds != 0:
    """Подготовка позиций в комментарии. Создает строку с пробелами."""
    template_com.append('_')
    count_firlds -= 1

# input("Проверь показатели, внеси новые и нажми Enter")

# Работа с комментарием
for row in export_orgeo:
    comment_output = template_com[:]
    print(comment_output)
    # Работа с комментарием блок день позиции с 4 по 9 (-1)
    running_day = 0
    if com.start == 1:  # Однодневный старт.
        comment_output[3] = '1'
        running_day = 1
    else:
        # Нулевая позиция коментария равна С:1234
        comment = row[8].split(',')[:1]
        block_day = ''.join(comment)
        for day in range(1, com.start + 1):
            if str(day) in block_day:
                comment_output[day + 2] = str(day)
                running_day += 1
    # Работа с показателями
    for pos in com.position:
        if pos in row[8]:
            if com.position[pos].position in [10, 11]:
                comm_symbol = str(running_day)
            else:
                comm_symbol = com.position[pos].symbol
            comment_output[com.position[pos].position - 1] = comm_symbol
    result = ''.join(comment_output)
    print(result)
    row.append(result)
    # меняем местами
    row[8], row[9] = row[9], row[8]
    file_base.append(row)


with open('output_file/import_orgeo.csv', encoding='windows-1251', mode='w') as imp_org:
    spamwriter = csv.writer(imp_org, delimiter=';')
    spamwriter.writerows(file_base)
