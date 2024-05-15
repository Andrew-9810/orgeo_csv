import json

import csv
import pathlib
import logging

logging.basicConfig(level=logging.INFO, filename='py_log.log',filemode='w')

# Пути к файлам
input_file = pathlib.Path('input_file/34694_csv_wo_predstavitel_2024_05_15.csv')
json_file = pathlib.Path('fields.json')
export_orgeo = []
file_base = []
comment_template = []

with open(json_file) as json_f:
    """Файл json c переключателями."""
    file_content = json_f.read()
    fields_switch = json.loads(file_content)


with open(input_file, encoding='windows-1251') as csv_f:
    """Файл csv c выгрузкой из orgeo."""
    csv_file = csv.reader(csv_f, delimiter=';')
    for line in csv_file:
        export_orgeo.append(line)


count_firlds = len(fields_switch)

while count_firlds != 0:
    """Подготовка позиций в комментарии."""
    comment_template.append(' ')
    count_firlds -= 1


for row in export_orgeo:
    comment_output = comment_template[:]
    # C: 23, 800, Оплачено,
    comment = row[8].split(',')

    for field in fields_switch:

        if field in comment:
            comment_volume = fields_switch[field][0]
            comment_position = fields_switch[field][1]
            comment_output[comment_position] = comment_volume
        else:
            continue

    comment_str = ''
    for i in comment_output:
        comment_str += f'{i}'
    row[9] = comment_str

    row[8], row[9] = row[9], row[8]
    logging.info(row)
    file_base.append(row)

logging.info(file_base)



