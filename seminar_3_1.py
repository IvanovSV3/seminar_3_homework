# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

number_2 = int(input("веыдите количестов элементов списка "))
print(number_2)

def List_1(number_1):
    a = []
    for i in range(number_1):
        i = int(i)
        a.insert(i, i+3)
    # print(a)
    return a

# b = List_1(number_2)
# print(b)

# bb = len(b)
# print('bb = ', bb)

def summa_1(sum_1):
    aa = len(sum_1)
    sum_2 = 0
    for j in range(aa):
        if j % 2 != 0:
            k = int(sum_1[j])
            # print('k=',k)
            sum_2 = sum_2 + k
    print("СУММА = ", sum_2)

b = List_1(number_2)
print('список = ',b)
summa_1(b)