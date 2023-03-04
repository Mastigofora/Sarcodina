entered_list = input("Введите список чисел, разделенных пробелом: ").split()
num_list = list(map(int, entered_list))
print("Максимальное значение:", max(num_list))
print("Максимальное значение:", min(num_list))


print(*(x for x in input().split() if not int(x) % 3))
print(*(x for x in input().split() if not int(x) % 3 and int(x) % 5))

# На входе список из чисел, каждое число повторяется два раза, и только одно число повторяется 1 раз. Найти число, которое повторяется 1 раз.
# пример:
# 1 6 2 5 2 9 6 1 5
# вывести 9