# Пользователь задает две строки. Определить количество вхождений одной строки в другой.

main_text = str(input("Введите основную строку:"))
symbol_text = str(input("Введите искомые символы:"))

def find_symbols (main_t,symbol_t):
   count = 0
   i = 0
   while i<(len(main_t)-len(symbol_t)+1):
       if symbol_t == main_t[i:i+len(symbol_t)]:
            count += 1
            i = i+len(symbol_t)
       else:
            i+=1
        
   print(count) 

find_symbols(main_text,symbol_text) 