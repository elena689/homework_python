#Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.


with open("file_hw3.txt", "w") as enter_text:
    for i in range(20):
        enter_text.write(str(i))
        enter_text.write("\n")
 
with open("file_hw3.txt", 'w') as del_text:
    for i in range(20):
        if int(str(i)) % 2 != 0:
            del_text.write(str(i))
            del_text.write("\n")
    

