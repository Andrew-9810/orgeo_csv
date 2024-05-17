# Меняем местами элементы списка
# original = ["x", "y"]
# original.append("z")
# print(original)
# original[1], original[2] = original[2], original[1]
# print(original)


# Добавление элементов в список опираясь на поля переключателя
# original = ["x", "y"]
# fild_swith = 3
# while fild_swith != 0:
#     original.append("")
#     print(original)
#     fild_swith -= 1
#
# print(original)

# original = ["x", "y"]
# template = original[:]
# print(template)
# print(original)
# template.append("1")
# print(template)
# print(original)

# original = ["x", "y"]
# print(str(original))
# stroka = ''
# for i in original:
#     stroka += f'{i}'
#
# print(stroka)

from decimal import *

comments = [
    'C:23', 'C:2', 'C:234', 'C:3', 'C:34', 'C:1',
    'C:1234', 'C:12', 'C:123', 'C:134', 'C:14'
]
start = 4
count_firlds = 2 + start + 4

comment_template = []
while count_firlds != 0:
    """Подготовка позиций в комментарии. Создает строку с пробелами."""
    comment_template.append(' ')
    count_firlds -= 1

comment_output = []

for comment in comments:
    comment_output = comment_template[:]
    poss = list(comment.lstrip('C:'))
    comment_output[0], comment_output[1] = 'C', ':'
    for i in poss:
        comment_output[int(i) - 1 + 2] = i
    print(comment_output)



