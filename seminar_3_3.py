# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
number = random.randint(4, 21)
print(number)

def list_1(number): # создание списка с дробной частью
    a = []
    for i in range(number):
        a.insert(i,round(i/7, 2))
        #print(a)
    a[0] = round(number/7,2) # убрать нулевой элемент
    return a

list_work = list_1(number)
print('Исходный лист = ', list_work)

def remains(list_): # создание списка дробных частей
    temp_ = []
    temp_ready = []
    for i in range(len(list_)):
        temp_.insert(i, int(list_[i]))
        temp_ready.insert(i, round(list_[i] - temp_[i],2))
    print('temp_ready =', temp_ready)
    return temp_ready

list_remains = remains(list_work)
print("remains = ",list_remains)

def subtraction_maks_min(list_): # сортировка от мин к макс
    for j in range(len(list_)-1):
        for i in range(len(list_)-1):
            if list_[i] > list_[i+1]:
                k = list_[i+1]
                list_[i+1] = list_[i]
                list_[i] = k
    return list_

igogo = subtraction_maks_min(list_remains)
print('igogo = ', igogo)

subtraction = igogo[len(igogo) - 1] - igogo[0]
print('разница между максимальным и минимальным значением = ', subtraction)
            



