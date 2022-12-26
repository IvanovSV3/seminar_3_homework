# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number_ = int(input('введите чило - '))
# print(type(number_))
number_01 = []

if number_ == 0:
    number_01 = number_
    print('двоичное число: ', number_01)
    exit()
elif number_ == 1:
    number_01 =  number_
    print('двоичное число: ', number_01)
    exit()


def number_0011(number_): # список получаемый при делении на 2
    k_1 = number_
    itog = []
    while k_1 >= 1:
        k = k_1 % 2
        # print('k=',k)
        if k == 0:
            itog.append(0)
        else:
            itog.append(1)
        k_1 = k_1 // 2
    # print('k1=', k_1)
    return itog

number_revers = number_0011(number_)
# print("itog_revers = ", number_revers)

def number_final(temp): # реверс списка на 2
    num = int(len(temp))
    # print('num', num)
    temp_1 = range(num)
    temp_2 = []
    j = 0
    for i in temp_1:
        temp_2.insert(j, temp[num -1 - i])
        j = j + 1
        # print("i-",temp_2)
    # print('temp_2', temp_2)
    return temp_2

print("двоичное = ", number_final(number_revers))