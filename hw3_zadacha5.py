#Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.


with open("file_hw3.txt", "w") as file:
    for i in range(20):
        file.write(str(i))
        file.write("\n")
 
with open("file_hw3.txt", 'w') as file_2:
    for i in range(20):
        if int(str(i)) % 2 != 0:
            file_2.write(str(i))
            file_2.write("\n")
    

