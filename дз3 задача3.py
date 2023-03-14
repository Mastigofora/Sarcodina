# напишите функцию change(list) которая принимает список и меняет местами его первый и последний элемент.
# в исходном списке минимум 2 значения

list = (input('Введите список в одну строку через пробел: ').split())
print("Вы ввели :", *list)

def change(list):
    list[0], list[-1] = list[-1], list[0]
    return list
change(list)
print(*list)

