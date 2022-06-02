
first_spisok = [5, 2, 3, 4, 6, 1, 7]
 
finish_spisok = []
buf_spisok = []
j = 1
 
while j < len(first_spisok): #выделение максимальной части списка по возрастанию в буферный список
    i = j
    copy_first_spisok = first_spisok[:]
    while i < len(copy_first_spisok)-1:
        if copy_first_spisok[i] < copy_first_spisok[i+1]: 
            buf_spisok.append(copy_first_spisok[i])
            i += 1
        else:
            copy_first_spisok.pop(i+1)  
  
    j+=1
    if len(finish_spisok) < len(buf_spisok): # запись внутренней возрастающей части списка из буферного в финальный список
        finish_spisok = buf_spisok
    buf_spisok=[]
  
if first_spisok[-1] > finish_spisok[-1]: # запись последнего значения в финальный список
    finish_spisok.append(first_spisok[-1])
  
if first_spisok[0] < finish_spisok[0]: # запись первого значения в финальный список
    finish_spisok.insert(0, first_spisok[0])
  
print(finish_spisok)
