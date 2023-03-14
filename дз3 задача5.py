#Дан список упорядоченный по неубыванию элементов в нем. Определите сколько в нем различных элементов


nums = input("Введите список чисел, разделенных пробелом: ").split()
def counting_numbers(nums):
    count = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            count += 1
    print("В списке", count, "различных элементов.")

counting_numbers(nums)