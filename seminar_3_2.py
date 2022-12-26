# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:- [2, 3, 4, 5,  6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

import random
number = random.randint(4, 21)
print(number)

def list_1(number): 
    a = []
    for i in range(number):
        a.insert(i,i)
    return a

list_work = list_1(number)
print('Исходный лист = ', list_work)

# list_temp = []
# print(type(number))
# print("номер = ", number)
# for j in list_work:
#     j = int(j)
#     if j - (number - j) < 0:
#         print(list_work[j])
#         k = number - 1 - j
#         print("k =", k)
#         print("лист к =",list_work[k])
#         multi = list_work[j] * list_work[k]
#         list_temp.insert(j, multi)

# print("list_temp = ",list_temp)

def multi_list(number, list_work):
    list_temp = []
    for j in list_work:
        j = int(j)
        if j - (number-j) < 0:
            multi = list_work[j] * list_work[number-1-j]
            list_temp.insert(j, multi)
    return list_temp

print('Итоговый лист = ', multi_list(number, list_work))