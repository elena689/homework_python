#Найти НОК двух чисел

import math
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print (f"НОК равен: {(num1 * num2) // math.gcd(num1 , num2)}")