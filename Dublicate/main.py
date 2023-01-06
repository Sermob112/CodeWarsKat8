# Дан массив целых чисел. НАписать функцию, которая определяет, содерждит ли массив какие либо дубликаты.
# Возвращать тру если содержит или фалс если не содержит

# exeple_list = [3,4,6,2,3]
num = 42
stringus = 'pipka'
# exeple_list2 = [3,4,2,1,5]
#
# def contains_dublicates(exemple_list):
#     return len(set(exemple_list)) != len(exemple_list)
#
# print(contains_dublicates(exeple_list2))
#################################################################################################
# Данно положительное число.Найти сумму его цифрю
# Если не число,то вернуть кал
# def sum_of_digital(some_number):
#     try:
#         numbers_of_Digits = len(str(some_number))
#         result = 0
#         for digits in range(numbers_of_Digits):
#             result += int(str(some_number)[digits])
#         return print(result)
#     except ValueError:
#         return print('Samu gay')
# sum_of_digital(num)
##########################################
#Найти те элементы в списке, которые не повторяются с другими элементами в списке
#Мое решение
# list_Difference = []
# list_1 = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# list_2 = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# def contains_dublicates(list_1, list_2):
#     for element in list_2:
#         if element not in list_1:
#           return  list_Difference.append(element)
#
# contains_dublicates(list_1,list_2)
# print(list_Difference)
#равильное решение
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# birds =  ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# def goose_filter(birds):
#     return list(filter(lambda x: x not in geese, birds))
# print (goose_filter(birds))