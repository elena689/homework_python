# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 

import math

d = float(input("Ввести "))
print(math.pi)

def count_symbols (num):
    stroka = str(num)
    if '.' in stroka:
        return abs(stroka.find('.') - len(stroka)) - 1
    else:
        return 0


print(round(math.pi,count_symbols(d)))

