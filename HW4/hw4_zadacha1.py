# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

from random import randint

def up_list (a):
    b=[]
    max_num = 0
    i=0
    while i<len(a):
        if a[i] > max_num:
            max_num = a[i]
            b.append(max_num)
            i = randint(1,len(a)-1)
        else:
            i+=1
    print(b)

spisok = [1, 5, 2, 3, 4, 6, 1, 7]
up_list(spisok)
