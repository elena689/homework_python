#Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 

from random import randint

with open('file_hw4.txt','w') as create_rand_file:
    for i in range (10): create_rand_file.write(str(randint(1,100))+',')

with open('file_hw4.txt','r') as sort_file:
    a=sort_file.readline().split(',')
    a.pop()
    print (sorted(map(int, a)))

