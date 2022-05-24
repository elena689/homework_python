# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.  
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def mult_dual_element (list_a):
    n = 0
    if len(list_a) % 2 == 0:
        n = len(list_a)//2
    else:
        n = len(list_a)//2+1
    multiplic = list(range(0,n))
    for i in range(0,n):
        multiplic[i] = list_a[0] * list_a[len(list_a)-1]
        if i == n-1:
            del list_a[-1]
            
        else:
            del list_a[-1]
            del list_a[0] 
    print (multiplic)



spisok = [2, 3, 5, 6]
mult_dual_element(spisok)