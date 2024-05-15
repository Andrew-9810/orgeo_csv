import csv
import pathlib
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")

input_file = pathlib.Path('input_file/34694_csv_wo_predstavitel_2024_05_15.csv')

with open(input_file, encoding='windows-1251') as f:
    spamreader = csv.reader(f, delimiter=';')
    for row in spamreader:
        comment = row[8].split(',')
        valie = ' Оплачено'
        if valie in comment:
            logging.info(comment)
