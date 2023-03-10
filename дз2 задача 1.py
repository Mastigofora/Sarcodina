month = input('Введите номер месяца: ')

if month.isnumeric() == False:
    print('Можно вводить только числа')
else:
    month = int(month)

    if month > 12 or month < 1:
        print('Нет такого месяца')
    else:
        print('Вы ввели:', month)
        y = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
        print("Месяц:", y[month - 1])
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    month28 = [2]
    if month in month31:
        print("Дней:", 31)
    elif month in month30:
        print("Дней:", 30)
    elif month in month28:
        print("Дней:", 28, "или", 29, "в высокосном году")