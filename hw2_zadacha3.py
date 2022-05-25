#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
#Пример: [1.1, 1.21, 3.15, 5, 10.07] => 0.19


spisok_float = [1.1, 1.21, 3.15, 5, 10.07]
for i in range (0,len(spisok_float)):
    spisok_float[i] %= 1
    
spisok_float.remove (0)
diff = max(spisok_float) - min(spisok_float)
print(round(diff,2))