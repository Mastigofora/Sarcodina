y = input("Введите список чисел, разделенных пробелом: ").split()
print("Введенный список:", y)
x = list(map(int, y))
z = []
for i in y:
    if y.count(i) ==1:
        z.append(i)
print("Не повторяющееся число", *z)