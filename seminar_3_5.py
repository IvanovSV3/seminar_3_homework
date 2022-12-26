# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def plus_fiba(number):
    plus_list = [1,1]
    for i in range(number - 2):
        plus_list.append(plus_list[-2] + plus_list[-1])
    return plus_list

# print(plus_fiba(8))

def minus_fiba(number):
    minus_list = [0,1]
    for i in range(number - 1):
        minus_list.append(minus_list[-2] - minus_list[-1])
    return minus_list[:: -1]

# print(plus_fiba(8))
print(minus_fiba(8) + plus_fiba(8))