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

original = ["x", "y"]
print(str(original))
stroka = ''
for i in original:
    stroka += f'{i}'

print(stroka)