# Найти сумму чисел списка стоящих на нечетной позиции Пример:[1,2,3,4] -> 4



def sum_nechet_i (list):
    sum = 0
    for i in range(0,len(list)):
        if i % 2 == 0:
            sum += list[i]
    print(sum)

spisok = [2,5,1,2,4]
sum_nechet_i(spisok)